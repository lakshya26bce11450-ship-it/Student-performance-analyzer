"""Logging setup (non-functional requirement: logging / monitoring)."""
import logging

from analyzer import config


def get_logger(name="analyzer"):
    """Return a logger that writes to logs/app.log (created on first use)."""
    logger = logging.getLogger(name)
    if logger.handlers:            # already configured
        return logger
    logger.setLevel(logging.INFO)
    try:
        config.LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(config.LOG_FILE, encoding="utf-8")
    except OSError:                # never crash the app because of logging
        handler = logging.NullHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    logger.addHandler(handler)
    return logger
