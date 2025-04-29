# Mount Linker

[![License: Apache v2](https://img.shields.io/badge/License-APACHEv2-D32228.svg)](https://opensource.org/license/apache-2-0)

A Linux utility that automatically creates convenient symlinks in your home directory for newly mounted block devices.

## Features

- 🔍 Monitors `/run/media/$USER` (or custom directory) for new mount events
- 🔗 Creates symbolic links in your home directory (e.g., `~/_usbdrive`)
- 🧹 Automatically removes links when devices are unmounted
- 🐧 Python implementation using `inotify`
- ⚙️ Configurable mount point and link naming

## Installation

### Prerequisites
- Python 3.11+
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

### Configuration

# Run in foreground
```bash
mount-linker
```

### Systemd Service (Autostart)
```bash
cp systemd/mount-linker.service ~/.config/systemd/user/
systemctl --user enable --now mount-linker.service
```

## Configuration

Configure through `~/.config/mount-linker/config.yml`:

```yaml
# ~/.config/mount-linker/config.yml
# IMPORTANT: Environment variables are used to demonstrate the default values!
# Use absolute links when specifying directories to watch.

mount_point: /run/media/$USER # Directory to monitor for mounts
prefix: mnt_                  # Prefix for created symlinks
target_dir: $HOME             # Where to create symlinks
```

## Example

When you insert a USB drive that mounts to `/run/media/$USER/MY_USB`, the tool will:
1. Detect the new mount
2. Create a symlink at `~/_MY_USB`
3. Remove the link when unmounted

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)

## Recommended GitHub Enhancements

1. **Add these badges** (create a new release first):
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
