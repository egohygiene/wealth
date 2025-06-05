# devtools

Uses Nix packages [asdf-vm](https://asdf-vm.com/) and [go-task](https://taskfile.dev/#/) and installs the [MegaLinter Runner](https://github.com/oxsecurity/megalinter) inside the dev container.

## Example Usage

```json
"./features/devtools": {
  "asdf_version": "latest",
  "taskfile_version": "latest"
}
```

## Options

| Option Id | Description | Type | Default |
|-----------|-------------|------|---------|
| `asdf_version` | **Ignored** - asdf is provided via Nix. | string | `latest` |
| `taskfile_version` | **Ignored** - Taskfile is provided via Nix. | string | `latest` |

## OS Support

The feature should work on most Debian/Ubuntu, RedHat, Fedora and Alpine based images. `bash` is required to execute the install script.
