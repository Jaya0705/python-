class Shape:
    def __new__(cls, sides, *args, **kwargs):
        if sides == 3:
            return Triangle(*args, **kwargs)
        else:
            return Square(*args, **kwargs)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length*self.length


o=Shape()
o1=Shape()
o2=Square(5)

print o2.area()