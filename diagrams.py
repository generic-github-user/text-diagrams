import uuid

shading = '░█'

with open('./generated-diagram.txt', 'w') as file:
    file.write('test')

class Diagram:
    """A diagram containing some graphical elements and their relationships."""

    def __init__(self, objects):
        self.objects = objects if objects else []
        self.id = uuid.uuid4()
