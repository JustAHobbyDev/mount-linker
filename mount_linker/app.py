import os
import time
import logging
from journal_logger import get_logger
from watchdog.observers import Observer
from watchdog.events import (
    FileSystemEventHandler,
    DirCreatedEvent,
    FileCreatedEvent,
    DirDeletedEvent,
    FileDeletedEvent,
)
from config import load_config

logger = get_logger(__name__)
config = load_config()

class WatchForDevices(FileSystemEventHandler):
    def __init__(self, config):
        self.target_dir = config.get('TARGET_DIR')
        self.prefix = config.get('PREFIX')
        super().__init__()

    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        _, name = os.path.split(event.src_path)
        link_path = self.target_dir / name

        if not os.path.exists(link_path):
            try:
                os.symlink(event.src_path, link_path)
            except OSError as e:
                logging.error(f"Failed to create link: {e.strerror}", extra={
                    'SYSLOG_INDENTIFIER': 'mount_linker',
                    'PRIORITY': 3, # err
                    'CUSTOM_FIELD': 'error'
                })

    def on_deleted(self, event: DirDeletedEvent | FileDeletedEvent) -> None:
        _, name = os.path.split(event.src_path)
        link_path = self.target_dir / name

        if os.path.lexists(link_path) and not os.path.exists(link_path):
            try:
                os.unlink(link_path)
            except OSError as e:
                logging.error(f"Failed to remove link: {e.strerror}", extra={
                    'SYSLOG_INDENTIFIER': 'mount_linker',
                    'PRIORITY': 3, # err
                    'CUSTOM_FIELD': 'error'
                })

class MountLinker():
    def run(self):
        event_handler = WatchForDevices()
        observer = Observer()
        observer.schedule(event_handler, MOUNT_POINT)
        observer.start()

        logging.info("Watching mount points...", extra={
            'SYSLOG_INDENTIFIER': 'mount_linker',
            'PRIORITY': 6,
            'CUSTOM_FIELD': 'startup'
        })

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nmount-linker: Exiting...")
        finally:
            observer.stop()
            observer.join()
