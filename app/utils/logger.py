import logging
from pathlib import Path

from app.core.config import BASE_DIR


LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "gs1scanner.log"


def setup_logger():

    LOG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    logger = logging.getLogger(
        "GS1Scanner"
    )

    logger.setLevel(
        logging.INFO
    )

    if logger.handlers:
        return logger


    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )


    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(
        formatter
    )


    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )


    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )


    return logger


logger = setup_logger()