import os
import sys
from mount_linker.journal_logger import get_logger
from mount_linker.app import MountLinker

logger = get_logger(__name__)

def main():
    ml = MountLinker()
    try:
        logger.info('Starting...')
        ml.run()
    except Exception:
        logger.critical("Failed to run", exc_info=True)


if __name__ == "__main__":
    main()
