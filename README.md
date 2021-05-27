[![Build Status](https://travis-ci.org/stdevel/ansible-drawio.svg?branch=master)](https://travis-ci.org/stdevel/ansible-drawio)

# drawio

This role installs draw.io.

## Requirements

The system needs access to the internet.

## Role Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `drawio_package_name` | `drawio` | Name of the package to download (*might be `draw.io` for some platforms/formats*) |
| `drawio_version` | `14.6.13` | Particular draw.io version |
| `drawio_use_appimage` | `false` | Use AppImage rather than OS package |


## Dependencies

No dependencies.

## Example Playbook

Refer to the following example:

```yaml
    - hosts: clients
      roles:
         - stdevel.drawio
```

Set variables if required, e.g.:

```yaml
    - hosts: clients
      roles:
        - role: stdevel.drawio
          drawio_package_name: "draw.io"
          drawio_version: "13.5.7"
          drawio_use_appimage: true
```

## License

Apache 2.0

## Author Information

Christian Stankowic (info@cstan.io)
