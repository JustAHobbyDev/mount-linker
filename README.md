# Mount Linker

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Linux utility that automatically creates convenient symlinks in your home directory for newly mounted block devices.

## Features

- 🔍 Monitors `/media` (or custom directory) for new mount events
- 🔗 Creates symbolic links in your home directory (e.g., `~/mnt-usbdrive`)
- 🧹 Automatically removes links when devices are unmounted
- 🐧 Lightweight Python implementation using `inotify`
- ⚙️ Configurable mount point and link naming

## Installation

### Prerequisites
- Python 3.7+
- Linux with inotify support

### Method 1: PIP Install
```bash
pip install git+https://github.com/JustAHobbyDev/mount-linker.git
```

### Method 2: Manual Installation
```bash
git clone https://github.com/JustAHobbyDev/mount-linker.git
cd mount-linker
pip install .
```

## Usage

### Basic Usage
```bash
mount-linker
```

### Options (via environment variables)
```bash
# Change monitored directory (default: /media)
export MOUNT_LINKER_MOUNT_POINT="/mnt"

# Change link prefix (default: "mnt-")
export MOUNT_LINKER_PREFIX="drive-"

# Run in foreground
mount-linker
```

### Systemd Service (Autostart)
```bash
cp systemd/mount-linker.service ~/.config/systemd/user/
systemctl --user enable --now mount-linker.service
```

## Configuration

Configure through environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `MOUNT_LINKER_MOUNT_POINT` | `/media` | Directory to monitor for mounts |
| `MOUNT_LINKER_PREFIX` | `mnt-` | Prefix for created symlinks |
| `MOUNT_LINKER_HOME_DIR` | `$HOME` | Where to create symlinks |

## Example

When you insert a USB drive that mounts to `/media/user/MY_USB`, the tool will:
1. Detect the new mount
2. Create a symlink at `~/mnt-MY_USB`
3. Remove the link when unmounted

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)

## Recommended GitHub Enhancements

1. **Add these badges** (create a new release first):
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![Tests](https://github.com/JustAHobbyDev/mount-linker/actions/workflows/tests.yml/badge.svg)

2. **Add a screenshot** (create an `assets/` folder):
## Demo
![Demo GIF](assets/demo.gif)

### Debug Mode
```bash
MOUNT_LINKER_DEBUG=1 mount-linker
```
