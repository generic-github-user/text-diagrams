import numpy as np
import math

class Point:
    pos: np.ndarray
    precision: int

    def __init__(self, pos:list, p:int=8):
        """
        Create a new Point instance

        Params:
            pos: The new point's position in the coordinate system
            p: The level of precision to store the point's position with
        """
        self.pos = np.array(pos, dtype=float)
        self.precision = p

    def move(self, delta:list):
        """
        Translate the point

        Params:
            delta: A list of offsets to move the point along each axis in space by
        """
        self.pos += np.array(delta)
        return self

    def rotate(self, a:list, theta:int, rad:float=None):
        theta = float(theta)
        # Convert to radians
        if not rad:
            theta = theta * math.pi / 180
        # Create a rotation matrix to apply a rotation to the point
        rotation_matrix = [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ]
#         print(rotation_matrix)
#         self.pos *= rotation_matrix

        # Move the point so its coordinate is relative to the origin
        self.move(-a.pos)
        # Apply the rotation matrix
        self.pos = np.dot(self.pos, rotation_matrix)
        # Move point back
        self.move(a.pos)
        # Round to specified precision
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
