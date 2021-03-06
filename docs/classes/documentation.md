<!-- ## Documentation -->

<details>
<summary>
Documentation
</summary>

Class

*module `build-docs`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new Documentation object


#### Parameters

##### `Params`

{parameter_info}

##### `source_path`

 A pattern matching the relative file path of all files that classes, functions, and documentation should be gathered from



##### `template_path`

 A pattern matching the paths of documentation template files; the template name will be extracted from everything before `'_template.md'`



##### `output_path`

 The path to save the output to





#### Source

<details>
<summary>View source</summary>

```python


    def __init__(self,
        source_path='./*.py',
        template_path='./docs/templates/*_template.md',
        output_dir='./docs',
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
        self.output_dir = output_dir
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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>clean_tabs</code></h2></summary> -->
<summary>
clean_tabs
</summary>
<!-- ### `clean_tabs` -->
Method

Remove leading tabs from a string


#### Parameters

##### `Params`

{parameter_info}

##### `text`

 The input string





#### Source

<details>
<summary>View source</summary>

```python


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



```

</details>

#### References

- [Documentation.indent_width](#indent_width)

</details>


<details>
<!-- <summary><h2><code>create_links</code></h2></summary> -->
<summary>
create_links
</summary>
<!-- ### `create_links` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def create_links(self, code, class_, method_):
        methods_linked = []
        includes = []
        for m, c in self.classes:
            class_methods = inspect.getmembers(c[1], predicate=inspect.isfunction)
            for n, me in class_methods:
                method_str = c[0] + '.' + n
                self_str = 'self.' + n
                link = f'[{method_str}](#{n.lower()})'
                # link = f'<a href="#{n}">{method_str}</a>'

                # source_code = source_code.replace(method_str, link)
                # source_code = source_code.replace(self_str, link)
                if method_str in code or (self_str in code and class_[0] == c[0]):
                    if method_str not in methods_linked:
                        includes.append(f'- {link}')
                        methods_linked.append(method_str)
        includes = '\n'.join(includes) if includes else 'None available'
        return includes



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>extract_info</code></h2></summary> -->
<summary>
extract_info
</summary>
<!-- ### `extract_info` -->
Method

Parse a docstring and return a dictionary of its structured data


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def extract_info(self, docstring):
        """
        Parse a docstring and return a dictionary of its structured data
        """
        pass



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>generate</code></h2></summary> -->
<summary>
generate
</summary>
<!-- ### `generate` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


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
                includes = self.create_links(source_code, classname, name)

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



```

</details>

#### References

- [Documentation.clean_tabs](#clean_tabs)
- [Documentation.create_links](#create_links)
- [Documentation.import_modules](#import_modules)
- [Documentation.indent_width](#indent_width)

</details>


<details>
<!-- <summary><h2><code>import_modules</code></h2></summary> -->
<summary>
import_modules
</summary>
<!-- ### `import_modules` -->
Method

Import each of the modules to be documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>indent_width</code></h2></summary> -->
<summary>
indent_width
</summary>
<!-- ### `indent_width` -->
Method

Count the number of leading tabs in a string (e.g., a line of code)


#### Parameters

##### `Params`

{parameter_info}

##### `string`

 The input string





#### Source

<details>
<summary>View source</summary>

```python


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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>isnum</code></h2></summary> -->
<summary>
isnum
</summary>
<!-- ### `isnum` -->
Method

Check if a given character is numeric


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def isnum(self, x):
        """
        Check if a given character is numeric
        """

        return x in '1234567890.-'



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>parent</code></h2></summary> -->
<summary>
parent
</summary>
<!-- ### `parent` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def parent(self):
        pass



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>save</code></h2></summary> -->
<summary>
save
</summary>
<!-- ### `save` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def save(self, split_by='class'):
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

        if split_by == 'class':
            # print(self.root.children[0].__dir__())
            for part in self.root.children:
                Path('./docs/classes').mkdir(parents=True, exist_ok=True)
                self.text = part.generate()
                class_name = part.kwargs['class_name'].lower()
                self.write(self.output_dir+'/classes/'+class_name+'.md')
        else:
            self.write(self.output_path)



```

</details>

#### References

- [Documentation.write](#write)

</details>


<details>
<!-- <summary><h2><code>split_numeric</code></h2></summary> -->
<summary>
split_numeric
</summary>
<!-- ### `split_numeric` -->
Method

Separate a string into numeric and alphabetical substrings


#### Parameters

##### `Params`

{parameter_info}

##### `text`

 The text to parse



##### `parse`

 ?



##### `Returns`

{parameter_info}

##### `output`

 A list of substrings

- recommended to use under Unix.

- passing to system calls.

- even if the path doesn't point to anything.

- No normalization is done, i.e. all '.' and '..' will be kept along.

- Use resolve() to get the canonical path to a file.

- 

- slashes.





#### Source

<details>
<summary>View source</summary>

```python


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



```

</details>

#### References

- [Documentation.isnum](#isnum)

</details>


<details>
<!-- <summary><h2><code>write</code></h2></summary> -->
<summary>
write
</summary>
<!-- ### `write` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def write(self, path):
        with open(path, 'w', encoding='UTF-8') as result_file:
            result_file.write(self.text)



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:07:07.544809

<details>
<summary>View source</summary>

```python

class Documentation:
    """Documentation"""

    def __init__(self,
        source_path='./*.py',
        template_path='./docs/templates/*_template.md',
        output_dir='./docs',
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
        self.output_dir = output_dir
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

    def create_links(self, code, class_, method_):
        methods_linked = []
        includes = []
        for m, c in self.classes:
            class_methods = inspect.getmembers(c[1], predicate=inspect.isfunction)
            for n, me in class_methods:
                method_str = c[0] + '.' + n
                self_str = 'self.' + n
                link = f'[{method_str}](#{n.lower()})'
                # link = f'<a href="#{n}">{method_str}</a>'

                # source_code = source_code.replace(method_str, link)
                # source_code = source_code.replace(self_str, link)
                if method_str in code or (self_str in code and class_[0] == c[0]):
                    if method_str not in methods_linked:
                        includes.append(f'- {link}')
                        methods_linked.append(method_str)
        includes = '\n'.join(includes) if includes else 'None available'
        return includes

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
                includes = self.create_links(source_code, classname, name)

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

    def write(self, path):
        with open(path, 'w', encoding='UTF-8') as result_file:
            result_file.write(self.text)

    def save(self, split_by='class'):
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

        if split_by == 'class':
            # print(self.root.children[0].__dir__())
            for part in self.root.children:
                Path('./docs/classes').mkdir(parents=True, exist_ok=True)
                self.text = part.generate()
                class_name = part.kwargs['class_name'].lower()
                self.write(self.output_dir+'/classes/'+class_name+'.md')
        else:
            self.write(self.output_path)


```
</details>

</details>
