class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def format(self, string):
        return f"\033[38;2;{self.r};{self.g};{self.b}m{string}\033[0m"


col = {
    "dark_orange": Color(255, 145, 0),
    "orange_red": Color(255, 69, 0),
    "red": Color(255, 0, 0),
    "green": Color(0, 255, 0)
}
