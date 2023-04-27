class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def format(self, string):
        return f"\033[38;2;{self.r};{self.g};{self.b}m{string}\033[0m"