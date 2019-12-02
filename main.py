import sys

from utils.args_parser import create_parser
from utils.check_input import check_file_path
from utils.read_input import InputSourceFile
from utils.sys_logger import init_sys_logger


def main():
    parser = create_parser()
    args = parser.parse_args()

    input_file = args.input_file
    window = args.window_size
    input_file_is_valid = check_file_path(input_file)
    if not input_file_is_valid:
        sys.exit('Input file is not valid. Please, check')

    input_obj = InputSourceFile(input_file)
    with input_obj:
        for line in input_obj:
            print(line)


if __name__ == '__main__':
    main()
