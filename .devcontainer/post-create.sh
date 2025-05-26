#!/bin/bash
set -e

SSH_DIR="/home/vscode/.ssh"
mkdir -p "$SSH_DIR"
sudo chown -R vscode:vscode "$SSH_DIR"
sudo chmod 700 "$SSH_DIR"

DOCKER_CFG_DIR="/home/vscode/.docker"
CONFIG_JSON="$DOCKER_CFG_DIR/config.json"
mkdir -p "$DOCKER_CFG_DIR"
[ -f "$CONFIG_JSON" ] || echo '{}' > "$CONFIG_JSON"
sudo chown -R vscode:vscode "$DOCKER_CFG_DIR"

python3 <<'PY'
import json, os, pathlib
cfg_path = pathlib.Path("${CONFIG_JSON}")
try:
    cfg = json.load(cfg_path.open())
except Exception:
    cfg = {}
proxies = cfg.setdefault('proxies', {}).setdefault('default', {})
for env_var, key in [('HTTP_PROXY','httpProxy'),('HTTPS_PROXY','httpsProxy'),('NO_PROXY','noProxy')]:
    val = os.environ.get(env_var) or os.environ.get(env_var.lower())
    if val:
        proxies[key] = val
cfg_path.write_text(json.dumps(cfg, indent=2))
PY

DAEMON_JSON="/etc/docker/daemon.json"
sudo mkdir -p /etc/docker
[ -f "$DAEMON_JSON" ] || echo '{}' | sudo tee "$DAEMON_JSON" > /dev/null
DNS_VAL="${DOCKER_DNS:-8.8.8.8}"

sudo python3 <<PY
import json, os, pathlib
path = pathlib.Path("${DAEMON_JSON}")
try:
    data = json.load(path.open())
except Exception:
    data = {}
dns = "${DNS_VAL}"
if data.get('dns') != [dns]:
    data['dns'] = [dns]
    path.write_text(json.dumps(data, indent=2))
PY

sudo mkdir -p /etc/systemd/system/docker.service.d
ENV_FILE="/etc/systemd/system/docker.service.d/http-proxy.conf"
if [ ! -f "$ENV_FILE" ]; then
  sudo bash -c "cat > $ENV_FILE <<EOF_PROXY
[Service]
Environment=\"HTTP_PROXY=${HTTP_PROXY}\" \"HTTPS_PROXY=${HTTPS_PROXY}\" \"NO_PROXY=${NO_PROXY}\"
EOF_PROXY"
fi
sudo systemctl daemon-reload || true
