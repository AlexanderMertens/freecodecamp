MAX_LENGTH = 50


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if max(self.width, self.height) > MAX_LENGTH:
            return "Too big for picture."
        result = ''
        for _ in range(self.height):
            result = ''.join((result, '*' *  self.width, '\n'))
        return result

    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def set_side(self, side):
        self.side = side
        self.height = side
        self.width = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.side})"
