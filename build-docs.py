import importlib, inspect
import datetime
import json
import random
import glob
import os
import time

module_name = 'main'
docs_directory = './docs'
d_ = docs_directory
output = d_+'/main.md'
result = ''

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


class Documentation:
    """Documentation"""

    def __init__(self,
        source_path='./*.py',
        template_path='./docs/templates/*_template.md',
        output_path='./docs/documentation.md',
        ignore=['extra']
    ):
        """
        Create a new Documentation object

        Params:
            source_path: A pattern matching the relative file path of all files that classes, functions, and documentation should be gathered from
            template_path: A pattern matching the paths of documentation template files; the template name will be extracted from everything before `'_template.md'`
            output_path: The path to save the output to
        """

        template_files = glob.glob(template_path)
        # filename = t.split('/')[-1]
        self.sources = {os.path.basename(s).split('.')[0]: os.path.normpath(s) for s in glob.glob(source_path) if not any(i in s for i in ignore)}
        self.templates = {os.path.basename(t).split('_')[0]: os.path.normpath(t) for t in template_files}
        self.output_path = output_path

        self.template_content = {}
        for k, v in self.templates.items():
            path = v
            with open(path, 'r') as template_file:
                self.template_content[k] = template_file.read()

        self.text = ''
        self.classes = []
        self.headers = ['Params', 'Returns', 'Attributes']
        self.hierarchy = [
            'class',
            'method',
            'parameter',
            'pinfo',
            'extra'
        ]
        self.tab_length = 6

    def indent_width(self, string):
        """
        Count the number of leading tabs in a string (e.g., a line of code)

        Params:
            string: The input string
        """
        if string.startswith(' '*self.tab_length):
            string = string.replace(' '*self.tab_length, '\t')
        # elif string.startswith('')
        indent = len(string) - len(string.lstrip())
        # indent = string.count('\t')
        return indent

    def clean_tabs(self, text):
        """
        Remove leading tabs from a string

        Params:
            text: The input string
        """

        if text:
            # lines = text.split('\n')
            lines = text.splitlines()
            lines = [l for l in lines if l]

            # if not lines[0]:
            #     lines = lines[1:]

            # if not lines[0].startswith(' ') and not lines[0].startswith('\t') and len(lines) > 1:
            #     q = self.indent_width(lines[1])
            #     lines[0] = ('\t' * q) + lines[0]
            #     print(q, 523523)

            # if not lines[0]:
            # if len(lines[0]) < 2:
            #     lines = lines[1:]
            # y = lines[0] if len(lines) < 2 else lines[1]
            y = lines[0]
            # print(lines[0].count('\t'))
            tabs = self.indent_width(y)
            return '\n'.join([l[tabs:] for l in lines])
        else:
            return ''

    def isnum(self, x):
        """
        Check if a given character is numeric
        """

        return x in '1234567890.-'

    def split_numeric(self, text, parse=True):
        """
        Separate a string into numeric and alphabetical substrings

        Params:
            text: The text to parse
            parse: ?

        Returns:
            output: A list of substrings
        """

        block = ''
        block_numeric = self.isnum(text[0])
        output = []
        for t in text:
            if self.isnum(t) == block_numeric:
                block += t
            else:
                if block_numeric:
                    block = float(block)
                output.append(block)
                block = t
                block_numeric = self.isnum(t)
        if block_numeric:
            block = float(block)
        output.append(block)
        return output

    def import_modules(self):
        """
        Import each of the modules to be documented
        """
        for k, v in self.sources.items():
            module_name = k
            doc_module = importlib.import_module(module_name)
            doc_classes = inspect.getmembers(doc_module, inspect.isclass)
            for c in doc_classes:
                self.classes.append([doc_module, c])

    def extract_info(self, docstring):
        """
        Parse a docstring and return a dictionary of its structured data
        """
        pass

    def parent(self):
        pass

    def generate(self):
        self.text = ''
        self.import_modules()

        current_section = Section(type_='main', templates=self.template_content)
        self.root = current_section
        for module, classname in self.classes:
            # print(self.classes)
            new_section = Section(type_='class', templates=self.template_content, title=classname[0], module=module.__name__, methods='children', params='children')
            current_section.add(new_section)
            current_section = new_section
            # print(classname)
            methods = inspect.getmembers(classname[1], predicate=inspect.isfunction)
            for name, method in methods:
                # print(name, method, True)
                new_section = Section(type_='method', templates=self.template_content, title=name, methods='children', params='children', module=module.__name__)
                current_section.add(new_section)
                current_section = new_section

                # print(method)

                # Temporary dictionary to hold hierarchy of parsed data
                # info = ParseData(hierarchy=self.hierarchy)
                docstring = method.__doc__
                if docstring:
                    docstring = docstring.replace(' '*self.tab_length, '\t')
                    docstring = self.clean_tabs(docstring)
                else:
                    docstring = ''
                # Split docstring by lines
                # lines = docstring.split('\n')
                lines = docstring.splitlines()
                section = 'text'
                subsection = ''
                # t = self.indent_width(lines[0])

                # Loop through the lines in the docstring
                for i, l in enumerate(lines):
                    l = l.replace(' '*self.tab_length, '\t')

                    # Detect section tag
                    # if l and l[0] == '@':
                    #     section = l[1:]
                    # New tag format (e.g., 'Params: ...')
                    t = self.indent_width(l)
                    l = self.clean_tabs(l)
                    print(i, l, t, self.indent_width(l), len(self.hierarchy), True)
                    section_type = self.hierarchy[t]
                    if any(l.startswith(h) for h in self.headers):
                        # print(l[:-1])
                        section = l[:-1].lower()
                        current_section = Section(type_=section_type, templates=self.template_content, title=l[:-1], params='children', parameter=l.split(':')[0])
                    else:
                        # print(t, l)
                        new_section = Section(content=l.split(':'), type_=section_type, parent=current_section, templates=self.template_content, params='children', parameter=l.split(':')[0])
                        current_section.add(new_section)
                        # current_section = new_section

        self.text = self.root.generate()

        return self

    def write(self):
        # result = result.replace('{CA}', 'cellular automata')
        # result = result.replace('{planned}', '`[not yet implemented]`')

        try:
            with open(self.output_path, 'r') as result_file:
                current_content = result_file.read()

            # Update the header containing the current version of the documentation
            firstline = current_content.split('\n')[0]
            print(firstline.split(' '))
            if 'Docs version' in firstline:
                # Increment version
                version = int(firstline.split(' ')[-1])+1
            else:
                version = 0
            self.text = 'Docs version ' + str(version) + '\n\n' + self.text
        except:
            pass

        with open(self.output_path, 'w') as result_file:
            result_file.write(self.text)

Docs = Documentation()
print(Docs.templates, Docs.sources)
Docs.generate().write()
print(Docs.template_content)
breakpoint()
# print(Docs.text)


symbols = {
    '<': 'less than',
    '>': 'greater than',
    '<=': 'less than or equal to',
    '>=': 'greater than or equal to',
}


data_types = ['int', 'str', 'float', 'bool', 'func', 'array']

# TODO: link to relevant git commits + source code


# print(result)
# print('{}% of classes and {}% of methods documented')
