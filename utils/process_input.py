from datetime import datetime, timedelta
import os
from typing import Tuple, Optional

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def check_file_path(file_path: str) -> bool:
    """
    Checks if file is file and non empty
    Args:
        file_path: path to file that needs to be validated

    Returns: Bool

    """
    logger.info(f'checking if filepath "{file_path}" is valid and file is not empty')
    try:
        return all([os.path.isfile(file_path), os.stat(file_path).st_size != 0])
    except FileNotFoundError:
        return False


def get_timestamp_from_string(timestamp_string: str) -> Tuple[bool, Optional[datetime, None]]:
    """
    Gets timestamp from string (if can), validates it and rounds it to next minute
    Args:
        timestamp_string: string containing time in format '%Y-%m-%d %H:%M:%S.%f'

    Returns: bool if string has time with valid format or not and datetime or None

    """
    try:
        return True, datetime.strptime(timestamp_string, '%Y-%m-%d %H:%M:%S.%f').replace(second=0, microsecond=0) + \
               timedelta(minutes=1)
    except (ValueError, TypeError):
        logger.info(f'timestamp "{timestamp_string}" is not valid')
        return False, None


def get_duration_from_string(duration: str) -> float:
    """
    Gets float from string (if can) and validates it
    Args:
        duration: string of seconds

    Returns: bool if string has float or not and float itself or None

    """
    try:
        return True, float(duration)
    except (ValueError, TypeError):
        logger.info(f'duration "{duration}" is not valid')
        return False, None
