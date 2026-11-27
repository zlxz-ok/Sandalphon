# Sandalphon

**Sandalphon** is a toolkit built with multiple Python libraries for everyday use.

## Features

- QR Code Generator (v1.0.0 supports PNG output only)

- Password Generator

- Metadata File Inspector (currently basic; improvements planned for future versions)

## Third-party libraries

Sandalphon is not affiliated with, endorsed by, or officially connected to the
developers or maintainers of the third-party libraries it uses. All product
names and trademarks belong to their respective owners.

See the [third-party notices](THIRD-PARTY-NOTICES.md) for the libraries used
and their license information.

## How to install

Sandalphon is distributed through [pipx](https://pipx.pypa.io/).

**Requirements:** Python 3.12+, pipx.

### Linux

Install pipx:

```bash
# Fedora
sudo dnf install pipx

# Ubuntu
sudo apt update && sudo apt install pipx
```

Configure and install RaphaelDL:

```bash
pipx ensurepath
pipx install git+https://github.com/zlxz-ok/Sandalphon.git
```

Restart your terminal, then run:

```bash
sandal
```

### Windows

Open PowerShell:

```powershell
py -m pip install --user pipx
py -m pipx ensurepath
```

Restart PowerShell, then install and run:

```powershell
pipx install git+https://github.com/zlxz-ok/Sandalphon.git
rpdl
```

### Uninstall

On either platform:

```bash
pipx uninstall sandalphon
```
