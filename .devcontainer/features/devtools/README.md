# devtools

Installs [asdf](https://asdf-vm.com/), the [Taskfile](https://taskfile.dev/#/) binary, and the [MegaLinter Runner](https://github.com/oxsecurity/megalinter) inside the dev container.

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
| `asdf_version` | Version of asdf to install. | string | `latest` |
| `taskfile_version` | Version of Taskfile binary to install. | string | `latest` |

## OS Support

The feature should work on most Debian/Ubuntu, RedHat, Fedora and Alpine based images. `bash` is required to execute the install script.
