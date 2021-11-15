class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return int(self.x)

    def get_y(self):
        return int(self.y)

    def get_coords(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            # Если это не Точка то нет смысла сравнивать
            return False
        if self.name == other.name and self.x == other.x and self.y ==other.y:
            return True
        return False 

    def __gt__(self, other):
        return self.x > other

    def __lt__(self, other):
        return self.x < other

    def __ge__(self, other):
        return self.x >= other

    def __le__(self, other):
        return self.x <= other

    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def __repr__(self):
        return "Point('{}', {}, {})".format(self.name, self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)
