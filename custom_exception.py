class DataNotFoundException(Exception):
    """
    This is the custom exception class
    """
    def __init__(self, message, *args):
        super().__init__(args)
        self.data = message

    def __str__(self):
        return f'exception handled {self.data}'


class PatternError(Exception):
    """
    This is the custom exception class
    """
    def __init__(self, message, *args):
        super().__init__(args)
        self.data = message

    def __str__(self):
        return f'exception handled {self.data}'
