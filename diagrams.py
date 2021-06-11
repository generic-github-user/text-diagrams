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
        self.text = '\n'.join(''.join(row) for row in self.canvas)

        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.text)

TestDiagram = Diagram()
TestDiagram.render()
