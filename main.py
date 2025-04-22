import os
import logging
from mount_linker.app import MountLinker


def main():
    ml = MountLinker()
    try:
        ml.run()
    except Exception as e:
        logging.critical(f"Error: {e.with_traceback}")
        os._exit(1)


if __name__ == "__main__":
    main()
