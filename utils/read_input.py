class InputSourceFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.input_source = None
        self.check_input()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.input_source)

    def __enter__(self):
        self.input_source = open(self.file_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.input_source.close()

    def check_input(self):
        pass
