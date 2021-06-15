import datetime

class Section:
    def __init__(self, content=None, type_=None, data=None, templates=None, parent=None, **kwargs):
        """
        Create a new section

        Params:
            type_: The type of section
            templates: A dictionary pairing template names to their contents
            parent: The parent section
            **kwargs: Additional arguments and/or data for the section
        """
        defaults = {
            'classes': 'children',
            'methods': 'children',
            'params': 'children',
            'types': 'children',
            'timestamp': str(datetime.datetime.now()),
            'class_info': 'Class not yet documented',
            'module': 'Main',
            'module_info': 'Module not yet documented'
        }
        self.parent = parent
        self.children = []
        self.content = content if content else []
        self.data = data if data else {}
        self.text = ''
        self.templates = templates
        self.type = type_

        defaults |= kwargs
        self.kwargs = defaults

    def names(self):
        return [c.type for c in self.children]

    def add(self, x):
        self.children.append(x)
        return x

    def set(self, a, b):
        """
        Set a property of the section

        Params:
            a: The name of the property
            b: The value to set the property to
        """
        self.kwargs[a] = b

    def generate(self):
        # s = Section(section_type=self.type, template_content=template)
        # self.text = ' | '.join(self.content)
        self.text = self.templates[self.type]


        combined = '\n'.join([c.generate() for c in self.children if c is not self])
        # print(self.kwargs)
        # ???
        for r in self.kwargs:
            h = self.kwargs[r]
            if h == 'children':
                if self.children:
                    h = combined
                else:
                    h = ''
            for q in ['{{{}}}', '[{}]']:
                self.text = self.text.replace(q.format(r), h)

        # print(self.kwargs, self.text)
        # print(self.children)
        # print(len(self.children))
        # print([c.text for c in self.children])
        # time.sleep(0.01)

        return self.text
