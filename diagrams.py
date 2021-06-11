import uuid

shading = '░█'


class Element:
    """A generic element to be added to a diagram"""

    def __init__(self, pos):
        self.pos = pos if pos else [0, 0]
        self.x, self.y = self.pos

class Text(Element):
    """Simple text element to add to a diagram"""

    def __init__(self, pos, text):
        super(Text, self).__init__(pos)
        self.text = text
        self.box = [len(self.text), 1]
        self.w, self.h = self.box

    def render(self):
        return list(self.text)


class Diagram:
    """A diagram containing some graphical elements and their relationships."""

    def __init__(self, objects=None, dims=[30, 30], background='░'):
        self.objects = objects if objects else []
        self.id = uuid.uuid4()
        self.canvas = []
        self.dims = dims
        self.x, self.y = self.dims
        self.background = background

    def render(self, path='./generated-diagram.txt'):
        self.canvas = [[self.background for i in range(self.x)] for j in range(self.y)]
        for o in self.objects:
            t = o.render()
            if t and type(t[0]) not in [list, tuple]:
                t = [t]
            for row in t:
                self.canvas[o.y][o.x:o.x+o.w] = row

        self.text = '\n'.join(''.join(row) for row in self.canvas)

        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.text)

TestDiagram = Diagram()
TestDiagram.render()
