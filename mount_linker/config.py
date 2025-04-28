import os
import yaml
from pathlib import Path
from mount_linker.journal_logger import get_logger

logger = get_logger(__name__)

def from_config(data):
    return data

def load_config():
    user = os.getenv('USER')
    home = Path(os.path.expanduser('~'))
    xdg_config_home = os.getenv('XDG_CONFIG_HOME') or Path(home) / '.config'
    config_path = Path(xdg_config_home) / 'mount-linker' / 'config.yml'
    default_mount_point = Path(f"/run/media/{user}")
    mount_point = default_mount_point
    target_dir = home
    prefix = '_'

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

            potential_mount_point = config.get('mount_point', mount_point)
            if os.path.isdir(potential_mount_point):
                logger.info(f"Setting MOUNT_POINT from {mount_point} to {potential_mount_point}")
                mount_point = potential_mount_point
            else:
                logger.warning("Config Error: mount_point is not a directory. Falling back to default.")

            potential_target_dir = config.get('target_dir', target_dir)
            if os.path.isdir(potential_target_dir):
                target_dir = potential_target_dir
            else:
                logger.warning("Config Error: target_dir is not a directory. Falling back to default.")

            prefix = config.get('prefix', prefix)

            c = {
                'MOUNT_POINT': Path(mount_point),
                'TARGET_DIR': Path(target_dir),
                'PREFIX': prefix,
            }

            print(f"c: {c}")
            return from_config(c)

    except FileNotFoundError:
        logger.warning(f"Config file not found at {config_path}")
        return from_config({
            'MOUNT_POINT': default_mount_point,
            'TARGET_DIR': home,
            'PREFIX': prefix,
        })
    except yaml.YAMLError as e:
        logger.warning(f"Error parsing yaml file: {e}")
        return from_config({
            'MOUNT_POINT': default_mount_point,
            'TARGET_DIR': home,
            'PREFIX': prefix,
        })
