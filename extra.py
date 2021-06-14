def parse_tags(tag_list):
    result = '**'
    for i, t in enumerate(tag_list):
        if i < len(tag_list) - 1:
            next = tag_list[i+1]
        else:
            next = None

        if t in data_types:
            result += '`{}`'.format(t)
            if type(next) is list:
                if t in ['str']:
                    result += ' in `{}`'.format(', '.join(next))
                    tag_list.remove(next)
                elif t in ['func']:
                    result += ' (`{}` -> `{}`)'.format(*next)
                    tag_list.remove(next)
        elif '-' in str(t):
            limits = t.split('-')
            result += ' between `{}` and `{}`'.format(*limits)
        elif type(t) is not list and t in symbols:
            # elif any(s in t for s in symbols):
            result += ' {} {}'.format(symbols[t], next)
        elif type(t) is list and t[0] in data_types:
            if type(t[1]) in [int, float, str]:
                t[1] = [t[1]]
            result += '`{}` array of shape `{}`'.format(*t)
    result += '**'
    return result


for l in []:
    t = self.indent_width(l)
    print(t, l)
    if t == 0:
        # Detect section tag
        if l and l[0] == '@':
            section = l[1:]
        # New tag format (e.g., 'Params: ...')
        elif l[:-1] in self.headers:
            section = l[:-1]

        if section not in info:
            info[section] = {}
        if section == 'text':
            if 'val' not in info['text']:
                info['text']['val'] = []
            info[section]['val'].append(l)
    elif t in [1, 4]:
        subsection = self.clean_tabs(l)
        if subsection not in info[section]:
            info[section][subsection] = []
    elif t in [2, 8]:
        parts = self.clean_tabs(l).split(': ')
        print(parts)
        if len(parts) >= 2:
            label = parts[1]
            type_info = parts[0][1:-1].replace(' ','').split(',')
            arg_info = {
                'type': type_info,
                'label': label
            }
            info[section][subsection].append(arg_info)




class Section:
    def __init__(self, template_content, section_type):
        """Create a new Section object"""
        self.helpers = Documentation()
        self.template_content = template_content
        self.section_type = section_type
        self.stype = self.section_type
        self.children = []

    def generate(self, object=None, replacements=None, source=None):
        """Generate the content for this section"""

        if replacements is None:
            replacements = []

        if source:
            doc_info = source
        else:
            docstring = object.__doc__
            if docstring is None:
                docstring = 'Not yet documented'

            doc_info = self.helpers.extract_info(docstring)
        #     print(8, docstring)
        # print(6, source, bool(source))

        try:
            k = list(doc_info.hierarchy.keys())[0]
        except:
            k = 'parameter'
        self.stype = k
        # print(self.stype)

        if self.stype in ['class', 'method']:

            # replacements.append(('{docstring}', doc_info['text']['val'][0]))
            # (not c.children and True)
            m = ''.join([c.label for c in doc_info.children if True])
            # print(m)
            replacements.append(('{docstring}', m))
        # else:
        #     doc_info = object
        # WARNING

        content = self.template_content[self.stype]
        for r in replacements:
            content = content.replace(*r)

        # print(self.stype)
        if self.stype == 'method':
            pass
        elif self.stype == 'parameter':
            # param_list = []
            # print(doc_info.names())
            # if 'params' in doc_info.names():
                # print(True)
                # for k, v in doc_info['params'].items():
            # k = doc_info.label:
            #     if k[0] in '!':
            #         k = k[1:] + ' [required]'
            #     if k[0] in '~':
            #         k = k[1:] + ' [optional]'
            #
            #     param_content = generate_section('parameter', v, [('{parameter}', k)])
            #     param_list.append(param_content)
            content = content.replace('[params]', '\n'.join(param_list))

            # content = ''
            # label = doc_info[0]['label']
            label = doc_info.label

            if '{ex' in label:
                examples = []
                ex_options = label[label.find('{ex'): label.find('}')+1]
                # print(ex_options)
                ex_options_ = [float(f) for f in ex_options.split(':')[1][:-1].split(',')]
                ex_options_ = ex_options_ + [1., 1., 20.][-(3-len(ex_options_)):]
                print(ex_options_)
                for l in range(int(ex_options_[0])):
                    bounds = ex_options_[1:3]
                    # if ex_options_[1] % 1. == 0:
                    if ex_options_[1].is_integer():
                        ex = random.randint(*bounds)
                    else:
                        ex = random.uniform(*bounds)

                    examples.append(str(ex))

                examples = 'Examples: {}'.format('; '.join(['`{}`'.format(e) for e in examples]))
                label = label.replace(ex_options, examples)
                doc_info[0]['label'] = label
            content = content.replace('{label}', label)

            type_list = []
            for t in []:
                # print(t, 't')
                try:
                    # print('[{}]'.format(','.join(t['type'])))
                    y = [str(v) for v in t['type']]
                    z = '[{}]'.format(','.join(y))
                    print(z)
                    z = z.replace("'", '"')
                    # type_tags = set(json.loads(z))
                    type_tags = json.loads(z)
                    typestring = parse_tags(type_tags)
                    print(True)
                except Exception as e:
                    print(e)
                    typestring = ''
                    for req in t['type']:
                        if req in ['int', 'str', 'float', 'bool']:
                            typestring += '`{}`'.format(req)
                        elif req[0] == 'r':
                            if ':' in req:
                                limits = req[1:].split(':')
                                typestring += ' between `{}` and `{}`'.format(*limits)
                                # elif any(c in req for c in '<>')
                                # elif '<' in req:
                            elif any(s in req for s in symbols):
                                typestring += ' {} {}'.format(symbols[req[1]], req[-1])

                type_list.append('- {}: {}'.format(typestring, t['label']))

            content = content.replace('[types]', '\n'.join(type_list))

        # print(doc_info.children)
        for c in doc_info.children:
            content += c.generate(template=self.template_content) + '\n'

        return content

class ParseData:
    def __init__(self, parent=None, **kwargs):
        self.parent = parent
        self.children = []
        for k, v in kwargs.items():
            setattr(self, k, v)

        if hasattr(self, 'hierarchy'):
            k = list(self.hierarchy.keys())[0]
            self.type = k
        else:
            self.type = 'class'

    def names(self):
        return [c.type for c in self.children]

    def add(self, x):
        if self.hierarchy:
            k = list(self.hierarchy.keys())[0]
            x.hierarchy = self.hierarchy[k]
        self.children.append(x)
        return self

    def generate(self, template=None):
        s = Section(section_type=self.type, template_content=template)
        return s.generate(source=self)


                # arg_info = ParseData(type=section, label='empty')

            else:
                parts = self.clean_tabs(l).split(': ')
                # print(parts)
                # if len(parts) >= 2:
                # label = parts[1]
                label = parts[1] if len(parts) > 1 else ''
                arg_info = {
                    'type': parts[0],
                    # 'label': (parts[1] if (len(parts) > 1)),
                    'label': label,
                    'hierarchy': self.hierarchy
                }

            t2 = self.indent_width(l)
            print(l, t2)
            if t2 > t and arg_info:
                current_section.add(arg_info)
                # current_section = arg_info
            elif t2 == t and arg_info:
                # print(arg_info.type)
                # if current_section.parent:
                    # current_section.parent.add(arg_info)
                    # current_section = arg_info
                current_section.add(arg_info)
            elif t2 < t and arg_info:
                if current_section.parent:
                    current_section = current_section.parent
                    current_section.add(arg_info)
            else:
                print('???')
            current_section = arg_info
            print(current_section)

            t = t2


        for module, c in self.classes:
            class_section = Section(self.template_content, section_type='class')
            for name, cls in c:
                # if cls.__module__ == module_name:
                if True:

                    # print(name, cls)
                    # print(docstring)
                    # try:
                    #     print(cls.__annotations__)
                    # except:
                    #     pass

                    # section_content = section_content.replace('{class}', name)
                    # section_content = section_content.replace('{docstring}', docstring)
                    section_content = class_section.generate(cls, [('{class}', name)])
                    # print(section_content)

                    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
                    # print(methods)
                    method_info = ''
                    for m in methods:
                        method_section = Section(self.template_content, section_type='method')
                        subsection_content = method_section.generate(m[1], [('{method}', m[0])])
                        method_info += subsection_content + '\n'

                        # print(extract_info(mstring))
                    section_content = section_content.replace('[methods]', method_info)
                    section_content = section_content.replace('{timestamp}', str(datetime.datetime.now()))

                    self.text += section_content + '\n'




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
        defaults = {
            'methods': 'children',
            'params': 'children',
            'timestamp': str(datetime.datetime.now())
        }
        self.parent = parent
        self.children = []
        self.content = content if content else []
        self.data = data if data else {}
        self.text = ''
        self.templates = templates
        self.type = type_

        # for k, v in kwargs.items():
        #     setattr(self, k, v)

        # if hasattr(self, 'hierarchy'):
        #     k = list(self.hierarchy.keys())[0]
        #     self.type = k
        # else:
        #     self.type = 'class'

        kwargs |= defaults
        self.kwargs = kwargs

    def names(self):
        return [c.type for c in self.children]

    def add(self, x):
        self.children.append(x)
        return self

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
                    h = 'none'
            for q in ['{{{}}}', '[{}]']:
                self.text = self.text.replace(q.format(r), h)

        # for c in self.children:
        #     if c is not self:
        #         self.text += '\n'+c.generate()

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
        """Count the number of leading tabs in a string (e.g., a line of code)"""
        if string.startswith(' '*self.tab_length):
            string = string.replace(' '*self.tab_length, '\t')
        # elif string.startswith('')
        indent = len(string) - len(string.lstrip())
        # indent = string.count('\t')
        return indent

    def clean_tabs(self, text):
        """
        Remove leading tabs from a string
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
        """Check if a given character is numeric"""

        return x in '1234567890.-'

    def split_numeric(self, text, parse=True):
        """Separate a string into numeric and alphabetical substrings"""

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
        for k, v in self.sources.items():
            module_name = k
            doc_module = importlib.import_module(module_name)
            doc_classes = inspect.getmembers(doc_module, inspect.isclass)
            for c in doc_classes:
                self.classes.append([doc_module, c])

    def extract_info(self, docstring):
        """Parse a docstring and return a dictionary of its structured data"""
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
