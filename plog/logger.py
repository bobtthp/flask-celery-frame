import logging
import sys
import os
from plog.config import Env

from logging import StreamHandler
from logging.handlers import RotatingFileHandler


def setting_logger(instance_name):
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(process)s %(pathname)s %(lineno)d - %(message)s")
    formatter_simplified = logging.Formatter("%(asctime)s %(levelname)s %(process)s - %(message)s")

    console_handler = StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(Env.LOGGER_LEVEL)

    app_rotate_handler = RotatingFileHandler(os.path.join(Env.LOGGER_DIR, instance_name + '.log'),
                                             maxBytes=10 * 1024 * 1024, backupCount=5)
    app_rotate_handler.setFormatter(formatter_simplified)
    app_rotate_handler.setLevel(Env.LOGGER_LEVEL)

    app_logger = logging.getLogger(instance_name)
    app_logger.addHandler(console_handler)
    app_logger.addHandler(app_rotate_handler)
    app_logger.setLevel(Env.LOGGER_LEVEL)




