import os
from mount_linker.journal_logger import get_logger
from mount_linker.app import MountLinker

logger = get_logger(__name__)

def main():
    ml = MountLinker()
    try:
        ml.run()
    except Exception:
        logger.critical("Failed to run")
        os._exit(1)


if __name__ == "__main__":
    main()
