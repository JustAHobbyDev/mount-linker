import os
import yaml
from pathlib import Path
from journal_logger import get_logger

logger = get_logger(__name__)

def load_config():
    user = os.getenv('USER')
    home = os.path.expanduser('~')
    xdg_config_home = os.getenv('XDG_CONFIG_HOME') or Path(home) / '.config'
    config_path = Path(xdg_config_home) / 'mount-linker' / 'config.yml'
    run_media_user_dir = Path(f"/run/media/{user}")
    target_dir = home
    prefix = '_'

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

            mount_point = config.get('mount_point', run_media_user_dir)
            if not os.path.isdir(mount_point):
                logger.error("Config Error: mount_point is not a directory. Falling back to default.", extra={
                                            'SYSLOG_INDENTIFIER': 'mount_linker',
                                            'PRIORITY': 3, # err
                                            'CUSTOM_FIELD': 'config_error'
                                        })
                mount_point = run_media_user_dir
            target_dir = config.get('target_dir', target_dir)
            if not os.path.isdir(target_dir):
                logger.error("Config Error: target_dir is not a directory. Falling back to default.", extra={
                                            'SYSLOG_INDENTIFIER': 'mount_linker',
                                            'PRIORITY': 3, # err
                                            'CUSTOM_FIELD': 'config_error'
                                        })
                target_dir = home
            prefix = config.get('prefix', prefix)

            return {
                'MOUNT_POINT': mount_point,
                'TARGET_DIR': target_dir,
                'PREFIX': prefix,
            }

    except FileNotFoundError:
        logger.error(f"Config file not found at {config_path}", extra={
                            'SYSLOG_INDENTIFIER': 'mount_linker',
                            'PRIORITY': 3, # err
                            'CUSTOM_FIELD': 'io_error'
                        })
    except yaml.YAMLError as e:
        logger.error(f"Error parsing yaml file: {e}", extra={
                            'SYSLOG_INDENTIFIER': 'mount_linker',
                            'PRIORITY': 3, # err
                            'CUSTOM_FIELD': 'yaml_error'
                        })
