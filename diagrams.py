import uuid
import math
import unicodedata
import random

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
        # The bounding box of the rendered text
        self.box = [round(self.l*self.rx+1), round(self.l*self.ry+1)]
        # Aliases for the text's bounding box's width and height
        self.w, self.h = self.box
        self.canvas = [[None for i in range(self.w)] for j in range(self.h)]

        self.style = style
        # A list of style shortcuts and their corresponding standard Unicode names (certain properties like capitalization and letter are automatically inserted)
        self.styles = {
            'circled': '{} latin {} letter {}',
            'squared': '{} latin {} letter {}',
            'math-bold-script': 'mathematical bold script {} {}'
        }

    def render(self, capitalization='inherit'):
        for i, c in enumerate(self.text):
            # Multiply the ratios generated from the text orientation by the character index (and round) to determine the necessary x and y shift
            xc, yc = round(self.rx*i), round(self.ry*i)
            # print(xc, yc, self.box)
            if self.style:
                if capitalization in ['small', 'capital']:
                    chartype = capitalization
                elif capitalization == 'inherit':
                    chartype = 'capital' if c.isupper() else 'small'
                elif capitalization == 'random':
                    chartype = random.choice(['small', 'capital'])

                s = self.style
                if s == 'squared':
                    chartype = 'capital'
                elif s == 'random':
                    s = random.choice(['circled', 'squared', 'math-bold-script'])
                style_string = self.styles[s]
                num_fields = style_string.count('{}')
                args = [s, chartype, c][-num_fields:]
                # Attempt to retrieve the Unicode character from its name
                c = get_char(style_string.format(*args))
            # Set the character in the canvas
            self.canvas[yc][xc] = c
        return self.canvas


class Diagram:
    """A diagram containing some graphical elements and their relationships."""

    def __init__(self, objects=None, dims=[30, 30], background='random'):
        self.objects = objects if objects else []
        self.id = uuid.uuid4()
        self.canvas = []
        self.dims = dims
        self.x, self.y = self.dims
        self.background = background

        self.shades = ['light {}', 'medium {}', 'dark {}', 'full block']
        for i, s in enumerate(self.shades):
            num_fields = s.count('{}')
            if num_fields == 1:
                self.shades[i] = s.format('shade')
            self.shades[i] = get_char(self.shades[i])

    def render(self, path='./generated-diagram.txt', **kwargs):
        # Generate the "canvas"; a two-dimensional list storing the character at each position
        bg = self.background
        self.canvas = [[(self.shades[random.randint(0, 3)] if bg == 'random' else bg) for i in range(self.x)] for j in range(self.y)]
        # Render each object and add it to the canvas
        for o in self.objects:
            t = o.render(**kwargs)
            # If a 1D list is provided, add a wrapper list around it
            if t and type(t[0]) not in [list, tuple]:
                t = [t]
            # Add each character from the rendered element
            for i, row in enumerate(t):
                for j, c in enumerate(row):
                    if c:
                        self.canvas[o.y+i][o.x+j] = c

        # Combine canvas characters into an exportable string
        self.text = '\n'.join(''.join(map(str, row)) for row in self.canvas)

        # Write the string to a file
        with open(path, 'w', encoding='utf-8') as file:
            file.write(self.text)
        return self

    def add(self, element):
        self.objects.append(element)
        return self

TestDiagram = Diagram(background=' ')
TestDiagram.add(Text([5,5], 'Hello World', style='random')).render(capitalization='random')


# TODO: animated diagrams
# TODO: templates
