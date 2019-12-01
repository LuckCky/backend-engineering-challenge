from utils.args_parser import create_parser
from utils.sys_logger import init_sys_logger
from utils.read_input import InputSourceFile


def main():
    parser = create_parser()
    args = parser.parse_args()

    input_file = args.input_file
    window = args.window_size

    input_obj = InputSourceFile(input_file)
    with input_obj:
        for line in input_obj:
            print(line)


if __name__ == '__main__':
    main()
