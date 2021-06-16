import importlib, inspect
import datetime
import json
import random
import glob
import os
import time
from dill.source import getsource

from section import Section
from argtype import ArgType

module_name = 'main'
docs_directory = './docs'
d_ = docs_directory
output = d_+'/main.md'
result = ''


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
            # 'class',
            'method',
            'parameter',
            'pinfo',
            'extra'
        ]
        self.tab_length = 4
        self.tab = ' '*self.tab_length
        self.current = {}
        self.previous = []

    def indent_width(self, string):
        """
        Count the number of leading tabs in a string (e.g., a line of code)

        Params:
            string: The input string
        """
        if string.startswith(' '*self.tab_length):
            string = string.replace(' '*self.tab_length, '\t')
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
            lines = text.replace(self.tab, '\t').splitlines()
            lines = [l for l in lines if l]
            # print(lines[0].count('\t'))
            tabs = self.indent_width(lines[0])
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

        current_section = Section(type_='module', templates=self.template_content)
        self.current['module'] = current_section
        # self.root = current_section
        for module, classname in self.classes:
            # print(self.classes)
            new_section = Section(
                type_='class',
                parent=current_section,
                templates=self.template_content,
                class_name=classname[0],
                module=module.__name__,
                methods='children',
                params='children',
                source_code = '\n'+getsource(classname[1])+'\n'
            )
            self.current['module'].add(new_section)
            current_section = new_section
            self.current['class'] = new_section
            # print(classname)
            methods = inspect.getmembers(classname[1], predicate=inspect.isfunction)
            for name, method in methods:
                source_code = '\n'+getsource(method)+'\n'
                includes = []
                for m, c in self.classes:
                    class_methods = inspect.getmembers(c[1], predicate=inspect.isfunction)
                    for n, me in class_methods:
                        method_str = c[0] + '.' + n
                        self_str = 'self.' + n
                        link = f'[{method_str}](#{name})'
                        # link = f'<a href="#{n}">{method_str}</a>'

                        # source_code = source_code.replace(method_str, link)
                        # source_code = source_code.replace(self_str, link)
                        if method_str in source_code or (self_str in source_code and classname[0] == c[0]):
                            includes.append(f'- {link}')
                includes = '\n'.join(includes) if includes else 'None available'

                # print(inspect.getsourcelines(method)[0])
                # print(name, method, True)
                new_section = Section(
                    type_='method',
                    templates=self.template_content,
                    parent=current_section,
                    method_name=name,
                    methods='children',
                    params='children',
                    module=module.__name__,
                    # source_code=inspect.getsource(method)
                    # source_code=''.join(inspect.getsourcelines(method)[0]).encode('UTF-8')
                    source_code = source_code,
                    includes = includes
                )
                self.current['class'].add(new_section)
                current_section = new_section
                self.current['method'] = new_section

                # print(method)

                # Temporary dictionary to hold hierarchy of parsed data
                # info = ParseData(hierarchy=self.hierarchy)
                docstring = method.__doc__
                # print(docstring)
                if docstring:
                    docstring = docstring.replace(' '*self.tab_length, '\t')
                    docstring = self.clean_tabs(docstring)

                    # Split docstring by lines
                    # lines = docstring.split('\n')
                    lines = docstring.splitlines()
                    section = 'text'
                    subsection = ''

                    # Loop through the lines in the docstring
                    for i, l in enumerate(lines):

                        # Detect section tag
                        # if l and l[0] == '@':
                        #     section = l[1:]
                        # New tag format (e.g., 'Params: ...')
                        t = self.indent_width(l)
                        l = self.clean_tabs(l)
                        # print(i, l, t, self.indent_width(l), len(self.hierarchy), True)
                        section_type = self.hierarchy[t]
                        # print(section_type, self.current[section_type].type)
                        print(section_type, l)
                        if any(l.startswith(h) for h in self.headers):
                            # print(l[:-1])
                            section = l[:-1].lower()
                            new_section = Section(
                                type_='parameter',
                                # parent=self.current[section_type],
                                templates=self.template_content,
                                title=l[:-1],
                                params='children',
                                parameter=l.split(':')[0]
                            )
                            self.current['method'].add(new_section)
                            # current_section.add(new_section)
                            current_section = new_section
                            self.current[section_type] = new_section
                        elif t == 0 and l:
                            self.current[section_type].set('class_info', l)
                            self.current[section_type].set('method_info', l)
                        else:
                            # print(t, l)
                            label = l.split(':')[1] if len(l.split(':')) > 1 else ''
                            parameter_name = l.split(':')[0]
                            similar = [x for x in self.previous if x[-2] == parameter_name]
                            if similar:
                                label = label.replace('$$', similar[0][-1] + f' (inserted from docs for `{classname[0]}.{name}#{parameter_name}`)')

                            self.previous.append([classname[0], name, parameter_name, label])
                            new_section = Section(
                                content=l.split(':'),
                                type_=section_type,
                                # parent=self.current[section_type],
                                templates=self.template_content,
                                params='children',
                                parameter=parameter_name,
                                parameter_info=label,
                                pinfo=l
                            )
                            # current_section.add(new_section)
                            # self.current[new_section.parent.type].add(new_section)
                            self.current[self.hierarchy[t-1]].add(new_section)
                            self.current[section_type] = new_section
                            # current_section = new_section
                else:
                    docstring = 'Not yet documented'
                    current_section.set('method_info', docstring)

        self.root = self.current['module']
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

        with open(self.output_path, 'w', encoding='UTF-8') as result_file:
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
