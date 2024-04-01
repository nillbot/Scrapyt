""" Module used for handling errors and logging"""

import logging

class logger:
    def __init__(self) -> None:
        pass

    def _setup_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger
