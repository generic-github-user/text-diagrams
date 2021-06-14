import numpy as np

try:
    from point import Point
except:
    from point.py import Point

class Line:
    def __init__(self, a, b):
        """Create a new line

        Params:
            a: The start point of the line
            b: The end point of the line
        """
        self.a = a
        self.b = b

    def move(self, delta):
        """Translate the line

        Params:
            delta: The amount (in each direction/axis) to move the line by
        """
        for p in [self.a, self.b]:
            p.move(delta)
        return self

    def rotate(self, *args, **kwargs):
        for p in [self.a, self.b]:
            p.rotate(*args, **kwargs)
        return self

    def divide(self, n:int=1) -> list['Line']:
        """Split the line into several smaller line segments

        Params:
            n: The number of sections to divide the line into
        """
#         return [Line(Point(np.average([self.a, self.b], weights=[]))) for i in range(n)]
        sections = []
        for i in range(n):
            a_ = np.average([self.a(), self.b()], weights=[i, n-i], axis=0)
            b_ = np.average([self.a(), self.b()], weights=[i+1, n-i-1], axis=0)
            s = Line(
                Point(a_),
                Point(b_)
            )
            sections.append(s)
        return sections

    def __str__(self):
        return 'Line\n\t' + '\n\t'.join(str(v) for v in [self.a, self.b])

l = Line(
    Point([0, 2]),
    Point([0, 1])
)
# l.rotate(t, 90).a.pos
print(l.divide(3)[2])
