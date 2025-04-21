from operator import le
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import (
    FileSystemEventHandler,
    FileSystemEvent,
    DirCreatedEvent,
    FileCreatedEvent,
    DirDeletedEvent,
    FileDeletedEvent,
)

HOME = os.path.expanduser("~")
_, USER = os.path.split(HOME)
MOUNT_POINT = f"/run/media/{USER}"
LINK_PREFIX = "_"

class WatchForDevices(FileSystemEventHandler):
    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        _, name = os.path.split(event.src_path)
        link_name = f"{LINK_PREFIX}{name}"
        link_path = f"{HOME}/{link_name}"
        if not os.path.exists(link_path):
            try:
                os.symlink(event.src_path, link_path)
            except OSError as e:
                print(f"mount-linker: Failed to create link {link_path}. {e.strerror}")

    def on_deleted(self, event: DirDeletedEvent | FileDeletedEvent) -> None:
        _, name = os.path.split(event.src_path)
        link_name = f"{LINK_PREFIX}{name}"
        link_path = f"{HOME}/{link_name}"
        if os.path.lexists(link_path) and not os.path.exists(link_path):
            try:
                os.unlink(link_path)
            except OSError as e:
                print(f"mount-linker: Failed to unlink {link_path}. {e.strerror}")

def run():
    event_handler = WatchForDevices()
    observer = Observer()
    observer.schedule(event_handler, MOUNT_POINT)
    observer.start()

    print(f"mount-linker started: watching {MOUNT_POINT}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nmount-linker: Exiting...")
    finally:
        observer.stop()
        observer.join()
