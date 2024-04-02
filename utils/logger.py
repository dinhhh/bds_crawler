import logging


def get_logger() -> logging.Logger:
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    return log
