from datetime import datetime
import os

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def check_file_path(file_path):
    logger.info(f'checking if filepath "{file_path}" is valid')
    return os.path.isfile(file_path)


def get_timestamp_from_string(timestamp_string):
    try:
        return True, datetime.strptime(timestamp_string, '%Y-%m-%d %H:%M:%S.%f')
    except (ValueError, TypeError):
        logger.info(f'timestamp "{timestamp_string}" is not valid')
        return False, None


def get_duration_from_string(duration):
    try:
        return True, float(duration)
    except (ValueError, TypeError):
        logger.info(f'duration "{duration}" is not valid')
        return False, None
