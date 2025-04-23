import logging
from systemd.journal import JournalHandler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    journal_handler = JournalHandler()
    journal_fomatter = logging.Formatter(
        '[%(levelname)s] [%(module)s] [%(message)s]'
    )
    journal_handler.setFormatter(journal_fomatter)
    logger.addHandler(journal_handler)

    return logger
