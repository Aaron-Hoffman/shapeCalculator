class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if (self.width or self.height) > 50:
            return ("Too big for picture.")
        else:
            return (('*' * self.width) + '\n') * self.height

    def get_amount_inside(self, rect):
        amount_inside = (self.width // rect.width) * \
            (self.height // rect.height)
        return amount_inside


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.height = side
        self.width = side

    def set_width(self, side):
        self.width = side
        self.height = side


rec = Rectangle(10, 2)
rect = Rectangle(2, 2)
print(rec.get_amount_inside(rect))
