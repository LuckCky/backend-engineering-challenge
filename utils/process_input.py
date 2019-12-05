from datetime import datetime, timedelta
import os

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def check_file_path(file_path):
    logger.info(f'checking if filepath "{file_path}" is valid and file is not empty')
    try:
        return all([os.path.isfile(file_path), os.stat(file_path).st_size != 0])
    except FileNotFoundError:
        return False


def get_timestamp_from_string(timestamp_string):
    try:
        return True, datetime.strptime(timestamp_string, '%Y-%m-%d %H:%M:%S.%f').replace(second=0, microsecond=0) + timedelta(minutes=1)
    except (ValueError, TypeError):
        logger.info(f'timestamp "{timestamp_string}" is not valid')
        return False, None


def get_duration_from_string(duration):
    try:
        return True, float(duration)
    except (ValueError, TypeError):
        logger.info(f'duration "{duration}" is not valid')
        return False, None
