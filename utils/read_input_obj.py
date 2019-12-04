from utils.sys_logger import init_sys_logger

logger = init_sys_logger(__name__)


class InputSourceFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.input_source = None
        logger.info(f'input object for file {self.file_path} is initialised')

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.input_source)

    def __enter__(self):
        logger.info(f'opening input object for file {self.file_path}')
        self.input_source = open(self.file_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info(f'closing input object for file {self.file_path}')
        self.input_source.close()

    def first_line(self):
        with open(self.file_path) as file:
            return file.readline()
