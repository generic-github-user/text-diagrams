import numpy as np
import math

class Point:
    def __init__(self, pos, p=8):
        self.pos = np.array(pos, dtype=float)
        self.precision = p

    def move(self, delta):
        self.pos += np.array(delta)
        return self

    def rotate(self, a, theta, rad=False):
        theta = float(theta)
        if not rad:
            theta = theta * math.pi / 180
        rotation_matrix = [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ]
#         print(rotation_matrix)
#         self.pos *= rotation_matrix
        self.move(-a.pos)
        self.pos = np.dot(self.pos, rotation_matrix)
        self.move(a.pos)
        self.pos = self.pos.round(self.precision)
        return self

    def __call__(self):
        return self.pos

    def print(self):
        print(self)
        return self

    def __str__(self):
        return 'Point ' + str(self.pos)


p = Point([0, 2])
t = Point([0, 1])
p.print()
t.print()
p.rotate(t, 90).pos
