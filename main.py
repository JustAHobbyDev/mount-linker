import os
from mount_linker.app import run


def main():
    try:
        run()
    except Exception as e:
        print(f"Error: {e.with_traceback}")
        os._exit(0)


if __name__ == "__main__":
    main()
