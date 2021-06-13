from point import Point

class Polygon:
    def __init__(self, vertices=None):
        if not vertices:
            vertices = []
        self.vertices = vertices
        self.v = self.vertices

    def __str__(self):
        return 'Polygon\n\t' + '\n\t'.join(str(v) for v in self.v)

class RegularPolygon(Polygon):
    def __init__(self, r=1, n=4, c=None):
        super().__init__()
        self.v.append(Point([0, r]))
        if not c:
            c = Point([0, 0])
        self.center = c
        for i in range(n-1):
            self.v.append(Point(self.v[-1].pos).rotate(c, 360 / n))

r = RegularPolygon()
print(r)
