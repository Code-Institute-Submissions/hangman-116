class Color:
    """
    A class representing a color in RGB format.
    """
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def format(self, string):
        """
        Return the given string formatted with the RGB color values.
        """
        return f"\033[38;2;{self.r};{self.g};{self.b}m{string}\033[0m"


# Define a dictionary of color objects for convenience
col = {
    "dark_orange": Color(255, 145, 0),
    "orange_red": Color(255, 69, 0),
    "red": Color(255, 0, 0),
    "green": Color(0, 255, 0)
}
