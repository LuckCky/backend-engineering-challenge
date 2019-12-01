import argparse


def create_parser():
    """
    creates parser for arguments
    :return: parser with provided arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True,
                        help="path to file with input data")
    parser.add_argument("--window_size", type=int, required=True,
                        help="size of window in minutes to calculate moving average for")
    return parser
