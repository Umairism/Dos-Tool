import logging
import os
from datetime import datetime

def setup_logger(log_path=None):
    if not log_path:
        os.makedirs("logs", exist_ok=True)
        log_path = os.path.join("logs", f"whistler_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    else:
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    logger = logging.getLogger("WhistlerLogger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        fh = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
