import uuid
import math
import unicodedata

shading = '░█'


def get_char(name):
    try:
        return unicodedata.lookup(name)
    except:
        return None

class Element:
    """A generic element to be added to a diagram"""

    def __init__(self, pos):
        self.pos = pos if pos else [0, 0]
        self.x, self.y = self.pos

class Text(Element):
    """Simple text element to add to a diagram"""

    def __init__(self, pos, text, angle=15, style=None):
        super(Text, self).__init__(pos)
        self.text = text
        self.l = len(self.text)
        self.angle = angle
        # self.ratio = math.sin(math.radians(self.angle))
        r = math.radians(self.angle)
        self.rx = math.cos(r)
        self.ry = math.sin(r)
        self.box = [round(self.l*self.rx+1), round(self.l*self.ry+1)]
        self.w, self.h = self.box
        self.canvas = [[None for i in range(self.w)] for j in range(self.h)]

        self.style = style
        self.styles = {
            'circled': '{} latin {} letter {}',
            'squared': '{} latin {} letter {}'
        }

    def render(self):
        for i, c in enumerate(self.text):
            xc, yc = round(self.rx*i), round(self.ry*i)
            # print(xc, yc, self.box)
            if self.style:
                chartype = 'capital' if c.isupper() else 'small'
                s = self.style
                if s == 'squared':
                    chartype = 'capital'
                c = get_char(self.styles[s].format(s, chartype, c))
            self.canvas[yc][xc] = c
        return self.canvas


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
        # Generate the "canvas"; a two-dimensional list storing the character at each position
        self.canvas = [[self.background for i in range(self.x)] for j in range(self.y)]
        # Render each object and add it to the canvas
        for o in self.objects:
            t = o.render()
            # If a 1D list is provided, add a wrapper list around it
            if t and type(t[0]) not in [list, tuple]:
                t = [t]
            # Add each character from the rendered element
            for i, row in enumerate(t):
                for j, c in enumerate(row):
                    if c:
                        self.canvas[o.y+i][o.x+j] = c

        # Combine canvas characters into an exportable string
        self.text = '\n'.join(''.join(row) for row in self.canvas)

        # Write the string to a file
        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.text)
        return self

    def add(self, element):
        self.objects.append(element)
        return self

TestDiagram = Diagram()
TestDiagram.add(Text([5,5], 'Hello World', style='squared')).render()


# TODO: animated diagrams
# TODO: templates
