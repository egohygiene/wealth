#!/usr/bin/env bash

init() {
    TASKFILE_VERSION="latest"

    declare -A KNOWN_PLUGINS=(
        [nodejs]=node
        [python]=python3
        [poetry]=poetry
        [pnpm]=pnpm
        [ruby]=ruby
        [go]=go
        [java]=java
        [rust]=rustc
        [yarn]=yarn
        [terraform]=terraform
        [direnv]=direnv
        [awscli]=aws
        [kubectl]=kubectl
    )

verify_installation() {
    local cmd=$1
    local name=${2:-$cmd}
    local expected_path=""
    local resolved_cmd=""

    if [[ "$USE_LOCAL" == true ]]; then
        case "$name" in
        asdf) expected_path="${ASDF_DIR}/bin/asdf" ;;
        task) expected_path="${TASKFILE_HOME_DIR}/task" ;;
        *) expected_path="${ASDF_SHIMS_DIR}/${cmd}" ;;
        esac

        if [[ -x "$expected_path" ]]; then
            resolved_cmd="$expected_path"
        else
            log "❌ $name not found in expected local path: $expected_path"
            exit 1
        fi
    else
        resolved_cmd="$(command -v "$cmd" || true)"
        if [[ -z "$resolved_cmd" ]]; then
            log "❌ $name is not installed or not on global PATH."
            exit 1
        fi
    fi

    local version
    version=$("$resolved_cmd" --version 2>/dev/null || "$resolved_cmd" -v 2>/dev/null || echo "Version info not available")
    log "✅ $name is available at $resolved_cmd: $version"
}

has_asdf_plugin() {
    grep -q "^$1\$" < <(asdf plugin list 2>/dev/null)
}

# Path to the asdf installation directory
asdf::home() {
    echo "${ASDF_DIR:-"$HOME/.asdf"}"
}

# Verify that asdf is installed and print its version
asdf::verify() {
    local binary_path
    binary_path="$(asdf::home)/bin/asdf"
    if [[ -x "$binary_path" ]]; then
        local version
        version="$("$binary_path" --version 2>/dev/null || echo "Version info not available")"
        log "✅ ASDF installed at $binary_path: $version"
    else
        log "❌ ASDF not found at $binary_path"
        return 1
    fi
}

install_asdf() {
    local repo_url="https://github.com/asdf-vm/asdf"
    local binary_path="${ASDF_DIR}/bin/asdf"
    local version="${ASDF_VERSION:-latest}"

    if [[ "$version" == "latest" ]]; then
        log "🔍 Fetching latest ASDF version..."
        version="$(curl --fail --silent --show-error --location -o /dev/null -w '%{url_effective}' "${repo_url}/releases/latest" | sed 's#.*/tag/##')"
    fi

    # If it exists, try to run it
    if [[ -x "$binary_path" ]]; then
        if "$binary_path" --version &>/dev/null; then
            log "✅ ASDF already installed at $binary_path"
            return
        else
            log::warn "⚠️ Detected existing ASDF, but it failed to execute. Reinstalling..."
            rm -rf "$ASDF_DIR"
        fi
    fi

    log "📥 Downloading asdf $version..."
    curl --fail --silent --show-error --location \
        "${repo_url}/releases/download/${version}/asdf-${version}-${OS}-${ARCH}.tar.gz" \
        --output asdf.tar.gz

    tar -xzf asdf.tar.gz
    mkdir -p "$(dirname "$binary_path")"
    chmod +x asdf
    mv asdf "$binary_path"
    rm -f asdf.tar.gz

    log "✅ ASDF installed to $binary_path"
    asdf::verify
}

install_asdf_plugin() {
    local plugin_name=$1

    if ! has_asdf_plugin "$plugin_name"; then
        log "📥 Adding plugin: $plugin_name"
        if ! asdf plugin add "$plugin_name"; then
            log "❌ Failed to add plugin: $plugin_name"
            return 1
        fi
        log "✅ Plugin added: $plugin_name"
    else
        log "🔁 Plugin already exists: $plugin_name"
    fi
}

sort_plugins_by_known_plugins() {
    local -n input_plugins=$1
    local -a sorted_plugins=()

    # First: install all plugins from KNOWN_PLUGINS in order of declaration
    for plugin in "${!KNOWN_PLUGINS[@]}"; do
        for i in "${!input_plugins[@]}"; do
            if [[ "${input_plugins[$i]}" == "$plugin" ]]; then
                sorted_plugins+=("${input_plugins[$i]}")
                unset 'input_plugins[i]'
            fi
        done
    done

    # Then: install remaining unknown plugins (alphabetically)
    for plugin in "${input_plugins[@]}"; do
        sorted_plugins+=("$plugin")
    done

    input_plugins=("${sorted_plugins[@]}")
}

install_asdf_plugins() {
    log "🔍 Gathering plugins from .tool-versions files..."

    local tool_files
    if git rev-parse --is-inside-work-tree &>/dev/null; then
        mapfile -t tool_files < <(
            git ls-files --cached --others --exclude-standard '*.tool-versions' |
                while read -r f; do realpath "$f"; done
        )
    else
        mapfile -t tool_files < <(
            find . -type f -name ".tool-versions" -not -path "*/.*/*" |
                while read -r f; do realpath "$f"; done
        )
    fi

    if [[ ${#tool_files[@]} -eq 0 ]]; then
        log "⚠️ No .tool-versions files found."
        return
    fi
    log "📁 Found ${#tool_files[@]} .tool-versions files."

    for file in "${tool_files[@]}"; do
        log "📄 Processing .tool-versions file: $file"

        local dir
        dir="$(dirname "$file")"

        pushd "$dir" >/dev/null
        log "📍 Moved into: $(pwd) to install dependencies from $file"

        local all_plugins=()
        local seen=()

        while IFS= read -r line || [[ -n "$line" ]]; do
            [[ "$line" =~ ^#.*$ || -z "$line" ]] && continue

            local plugin
            plugin=$(awk '{print $1}' <<<"$line")

            if [[ ! " ${seen[*]} " =~ " $plugin " ]]; then
                seen+=("$plugin")
                all_plugins+=("$plugin")
            fi
        done <"$file"
        log "🔧 Found plugins: ${all_plugins[*]}"

        sort_plugins_by_known_plugins all_plugins
        log "🔧 Sorted plugins: ${all_plugins[*]}"

        for plugin in "${all_plugins[@]}"; do
            install_asdf_plugin "$plugin"
        done

        log "✅ All plugins installed from $file"

        # Install dependencies now that plugins are installed
        for plugin in "${all_plugins[@]}"; do
            local version
            version=$(awk -v plugin="$plugin" '$1 == plugin {print $2}' "$file")
            if [[ -n "$version" ]]; then
                log "📦 Installing $plugin version: $version"
                asdf install "$plugin" "$version"
                log "✅ Installed $plugin version: $version"
            else
                log "⚠️ No version specified for $plugin in $file"
            fi
        done

        popd >/dev/null
    done
}

main() {
    init "$@"
    install_asdf
    install_asdf_plugins
    install_taskfile
}

main "$@"
