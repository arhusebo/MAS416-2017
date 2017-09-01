import math

class Vec2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vec2(self.x/other, self.y/other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def angle(self, other=0):
        dX = self.x - other.x
        dY = self.y - other.y
        return math.atan2(dY, dX)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        return self/mag

    def normal(self):
        return Vec2(self.y, -self.x)

    def distance(self, other):
        return math.sqrt((other.x-self.x)**2+(other.y-self.y)**2)
