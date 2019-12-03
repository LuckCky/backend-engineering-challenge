import argparse

from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


def create_parser():
    """
    creates parser for arguments
    :return: parser with provided arguments
    """
    logger.info('creating arguments parser')
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True,
                        help="path to file with input data")
    parser.add_argument("--window_size", type=int, required=True,
                        help="size of window in minutes to calculate moving average for")
    return parser
