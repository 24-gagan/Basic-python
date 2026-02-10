class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Operator overloading for +
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"Point({self.x}, {self.y})")

p1 = Point(3, 4)
p2 = Point(5, 6)

p3 = p1 + p2   # Calls __add__()
p3.display()
