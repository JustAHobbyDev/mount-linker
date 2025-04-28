import logging
from systemd.journal import JournalHandler

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    logger.addHandler(handler)
    # handler = JournalHandler()
    # logger.addHandler(handler)

    return logger
