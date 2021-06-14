import importlib, inspect
import datetime
import json
import random
import glob
import os

module_name = 'main'
docs_directory = './docs'
d_ = docs_directory
output = d_+'/main.md'
result = ''

class Section:
    def __init__(self, template_content):
        """Create a new Section object"""
        self.helpers = Documentation()
        self.template_content = template_content

    def generate(self, stype, object, replacements):
        """Generate the content for this section"""

        docstring = object.__doc__
        if docstring is None:
            docstring = 'Not yet documented'
        if stype in ['class', 'method']:
            doc_info = self.helpers.extract_info(docstring)
            replacements.append(('{docstring}', doc_info['text']['val'][0]))
        else:
            doc_info = object
        content = self.template_content[stype]
        for r in replacements:
            content = content.replace(*r)

        if stype == 'method':
            param_list = []
            if 'params' in doc_info:
                for k, v in doc_info['params'].items():
                    if k[0] in '!':
                        k = k[1:] + ' [required]'
                    if k[0] in '~':
                        k = k[1:] + ' [optional]'

                    param_content = generate_section('parameter', v, [('{parameter}', k)])
                    param_list.append(param_content)
            content = content.replace('[params]', '\n'.join(param_list))
        elif stype == 'parameter':
            # content = ''
            label = doc_info[0]['label']

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
            for t in doc_info:
                print(t)
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

        return content

class ParseData:
    def __init__(self, **kwargs):
        self.children = []
        for k, v in kwargs.items():
            setattr(self, k, v)

    def names(self):
        return [c.type for c in self.children]


class Documentation:
    """Documentation"""

    def __init__(self, source_path='./*.py', template_path='./docs/templates/*_template.md'):
        """Create a new Documentation object"""

        template_files = glob.glob(template_path)
        # filename = t.split('/')[-1]
        self.sources = {os.path.basename(s).split('.')[0]: os.path.normpath(s) for s in glob.glob(source_path)}
        self.templates = {os.path.basename(t).split('_')[0]: os.path.normpath(t) for t in template_files}

        self.template_content = {}
        for k, v in self.templates.items():
            path = v
            with open(path, 'r') as template_file:
                self.template_content[k] = template_file.read()

        self.text = ''
        self.classes = []

    def indent_width(self, string):
        """Count the number of leading tabs in a string (e.g., a line of code)"""
        indent = len(string) - len(string.lstrip())
        return indent

    def clean_tabs(self, text):
        """Remove leading tabs from a string"""

        lines = text.split('\n')
        if not lines[0]:
            lines = lines[1:]
        tabs = self.indent_width(lines[0])
        return '\n'.join([l[tabs:] for l in lines])

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
            # for c in doc_classes:
            self.classes.append([doc_module, doc_classes])

    def extract_info(self, docstring):
        """Parse a docstring and return a dictionary of its structured data"""

        # Temporary dictionary to hold hierarchy of parsed data
        info = {}
        docstring = self.clean_tabs(docstring)
        # Split docstring by lines
        lines = docstring.split('\n')
        section = 'text'
        subsection = ''
        # Loop through the lines in the docstring
        for l in lines:
            t = self.indent_width(l)
            if t == 0:
                # Detect section tag
                if l and l[0] == '@':
                    section = l[1:]

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
                label = parts[1]
                type_info = parts[0][1:-1].replace(' ','').split(',')
                arg_info = {
                    'type': type_info,
                    'label': label
                }
                info[section][subsection].append(arg_info)
        # Return dict
        return info

    def generate(self):
        self.text = ''
        self.import_modules()

        for module, c in self.classes:
            class_section = Section(self.template_content)
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
                    section_content = class_section.generate('class', cls, [('{class}', name)])
                    # print(section_content)

                    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
                    # print(methods)
                    method_info = ''
                    for m in methods:
                        subsection_content = class_section.generate('method', m[1], [('{method}', m[0])])
                        method_info += subsection_content + '\n'
                        # print(extract_info(mstring))
                    section_content = section_content.replace('[methods]', method_info)
                    section_content = section_content.replace('{timestamp}', str(datetime.datetime.now()))

                    self.text += section_content + '\n'

    def write(self):
        # result = result.replace('{CA}', 'cellular automata')
        # result = result.replace('{planned}', '`[not yet implemented]`')

        with open(output, 'r') as file:
            current_content = file.read()

        # Update the header containing the current version of the documentation
        firstline = current_content.split('\n')[0]
        print(firstline.split(' '))
        if 'Docs version' in firstline:
            # Increment version
            version = int(firstline.split(' ')[-1])+1
        else:
            version = 0
        result = 'Docs version ' + str(version) + '\n\n' + result

        with open(output, 'w') as file:
            file.write(result)

Docs = Documentation()
print(Docs.templates, Docs.sources)
Docs.generate()



symbols = {
    '<': 'less than',
    '>': 'greater than',
    '<=': 'less than or equal to',
    '>=': 'greater than or equal to',
}


data_types = ['int', 'str', 'float', 'bool', 'func', 'array']








# print(result)
# print('{}% of classes and {}% of methods documented')
