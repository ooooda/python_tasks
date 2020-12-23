import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.sides = []

        self.create_side(a, b)
        self.create_side(b, c)
        self.create_side(a, c)

        self.sides = sorted(self.sides)
        self.is_correct = False

        if self.sides[0] == self.sides[1] or self.sides[1] == self.sides[2]:
            self.is_correct = True
        if self.sides[0] + self.sides[1] < self.sides[2]:
            self.is_correct = False

    def create_side(self, point1, point2):
        side = ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
        self.sides.append(side)

    def find_square(self):
        p = sum(self.sides) * 0.5
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5


if __name__ == "__main__":
    lines = []
    triangles = []
    with open(sys.argv[1], "r") as f:
        for i, line in enumerate(f.read().splitlines()):
            splitted = line.split(' ')
            if len(splitted) != 6:
                print(f'Incorrect number of points line {i}')
            else:
                points = list(map(int, splitted))
                a = Point(points[0], points[1])
                b = Point(points[2], points[3])
                c = Point(points[4], points[5])
                triangles.append(Triangle(a, b, c))

    res = 0
    best = None
    for t in triangles:
        square = t.find_square()
        if t.is_correct and square > res:
            res = square
            best = t

    if res == 0:
        raise ValueError('No such correct triangles!')
    else:
        with open(sys.argv[2], "w") as f:
            f.write(' '.join(map(str, [best.a.x, best.a.y, best.b.x, best.b.y, best.c.x, best.c.y])))
