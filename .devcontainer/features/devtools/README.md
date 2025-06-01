
# devtools

Install asdf version 

## Example Usage

```json
    "./features/devtools": {
        "asdf_version": "latest"
    }
```

## Options

| Options Id | Description | Type | Default Value |
|-----|-----|-----|-----|
| asdf_version | Select or enter a Git version. | string | os-provided |
| asdf_version | Install from PPA if available (only supported for Ubuntu distributions) | boolean | true |



## OS Support

This Feature should work on recent versions of Alpine, Debian/Ubuntu, RedHat Enterprise Linux, Fedora, Alma, and RockyLinux distributions with the `apk`, `apt`, `yum`, `dnf`, or `microdnf` package manager installed.

`bash` is required to execute the `install.sh` script.


---

_Note: This file was auto-generated from the [devcontainer-feature.json](https://github.com/devcontainers/features/blob/main/src/git/devcontainer-feature.json).  Add additional notes to a `NOTES.md`._
