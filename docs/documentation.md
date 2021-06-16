Docs version 0

# Main

Module not yet documented

<!-- ## ArgRange -->

<details>
<summary>
ArgRange
</summary>

Class

*module `argtype`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __init__(self, *args):
        # super(ArgRange, self).__init__()
        self.range = range(*args)
        self.info = 'between {} and {}'
        self.args = args



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>example</code></h2></summary> -->
<summary>
example
</summary>
<!-- ### `example` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def example(self, n=1):
        values = list(self.range)
        return random.choices(values, k=n)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>text</code></h2></summary> -->
<summary>
text
</summary>
<!-- ### `text` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def text(self):
        return self.info.format(*self.args)



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.099609

<details>
<summary>View source</summary>

```python

class ArgRange:
    """ArgRange"""

    def __init__(self, *args):
        # super(ArgRange, self).__init__()
        self.range = range(*args)
        self.info = 'between {} and {}'
        self.args = args

    def text(self):
        return self.info.format(*self.args)

    def example(self, n=1):
        values = list(self.range)
        return random.choices(values, k=n)


```
</details>

</details>

<!-- ## ArgType -->

<details>
<summary>
ArgType
</summary>

Class

*module `argtype`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __init__(self, primitive, *conditions):
        self.primitive = primitive
        self.conditions = conditions
        self.info = '{} {} {}'



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>an</code></h2></summary> -->
<summary>
an
</summary>
<!-- ### `an` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def an(self, a):
        return 'an' if a[0] in 'aeiou' else 'a'



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>example</code></h2></summary> -->
<summary>
example
</summary>
<!-- ### `example` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def example(self, *args, **kwargs):
        return self.conditions[0].example(*args, **kwargs)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>text</code></h2></summary> -->
<summary>
text
</summary>
<!-- ### `text` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def text(self):
        condition_string = ', '.join(c.text() for c in self.conditions)
        p = self.primitive.__name__
        return self.info.format(self.an(p), p, condition_string)



```

</details>

#### References

- [ArgType.an](#an)

</details>


Docs built at 2021-06-16 05:12:41.102601

<details>
<summary>View source</summary>

```python

class ArgType:
    """
    Defines a 'type' that can be used for validating and/or converting function arguments, generating examples, type hinting, etc. It is intended to emulate some of the features of Python's `typing` module, albeit with a more general scope.
    """

    def __init__(self, primitive, *conditions):
        self.primitive = primitive
        self.conditions = conditions
        self.info = '{} {} {}'

    def an(self, a):
        return 'an' if a[0] in 'aeiou' else 'a'

    def text(self):
        condition_string = ', '.join(c.text() for c in self.conditions)
        p = self.primitive.__name__
        return self.info.format(self.an(p), p, condition_string)

    def example(self, *args, **kwargs):
        return self.conditions[0].example(*args, **kwargs)


```
</details>

</details>

<!-- ## ArgType -->

<details>
<summary>
ArgType
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

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __init__(self, primitive, *conditions):
        self.primitive = primitive
        self.conditions = conditions
        self.info = '{} {} {}'



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>an</code></h2></summary> -->
<summary>
an
</summary>
<!-- ### `an` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def an(self, a):
        return 'an' if a[0] in 'aeiou' else 'a'



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>example</code></h2></summary> -->
<summary>
example
</summary>
<!-- ### `example` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def example(self, *args, **kwargs):
        return self.conditions[0].example(*args, **kwargs)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>text</code></h2></summary> -->
<summary>
text
</summary>
<!-- ### `text` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def text(self):
        condition_string = ', '.join(c.text() for c in self.conditions)
        p = self.primitive.__name__
        return self.info.format(self.an(p), p, condition_string)



```

</details>

#### References

- [ArgType.an](#an)

</details>


Docs built at 2021-06-16 05:12:41.105586

<details>
<summary>View source</summary>

```python

class ArgType:
    """
    Defines a 'type' that can be used for validating and/or converting function arguments, generating examples, type hinting, etc. It is intended to emulate some of the features of Python's `typing` module, albeit with a more general scope.
    """

    def __init__(self, primitive, *conditions):
        self.primitive = primitive
        self.conditions = conditions
        self.info = '{} {} {}'

    def an(self, a):
        return 'an' if a[0] in 'aeiou' else 'a'

    def text(self):
        condition_string = ', '.join(c.text() for c in self.conditions)
        p = self.primitive.__name__
        return self.info.format(self.an(p), p, condition_string)

    def example(self, *args, **kwargs):
        return self.conditions[0].example(*args, **kwargs)


```
</details>

</details>

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


Docs built at 2021-06-16 05:12:41.117561

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

<!-- ## Path -->

<details>
<summary>
Path
</summary>

Class

*module `build-docs`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__bytes__</code></h2></summary> -->
<summary>
__bytes__
</summary>
<!-- ### `__bytes__` -->
Method

Return the bytes representation of the path.  This is only


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __bytes__(self):
        """Return the bytes representation of the path.  This is only
        recommended to use under Unix."""
        return os.fsencode(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__enter__</code></h2></summary> -->
<summary>
__enter__
</summary>
<!-- ### `__enter__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __enter__(self):
        return self



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__eq__</code></h2></summary> -->
<summary>
__eq__
</summary>
<!-- ### `__eq__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __eq__(self, other):
        if not isinstance(other, PurePath):
            return NotImplemented
        return self._cparts == other._cparts and self._flavour is other._flavour



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__exit__</code></h2></summary> -->
<summary>
__exit__
</summary>
<!-- ### `__exit__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __exit__(self, t, v, tb):
        # https://bugs.python.org/issue39682
        # In previous versions of pathlib, this method marked this path as
        # closed; subsequent attempts to perform I/O would raise an IOError.
        # This functionality was never documented, and had the effect of
        # making Path objects mutable, contrary to PEP 428. In Python 3.9 the
        # _closed attribute was removed, and this method made a no-op.
        # This method and __enter__()/__exit__() should be deprecated and
        # removed in the future.
        pass



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__fspath__</code></h2></summary> -->
<summary>
__fspath__
</summary>
<!-- ### `__fspath__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __fspath__(self):
        return str(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__ge__</code></h2></summary> -->
<summary>
__ge__
</summary>
<!-- ### `__ge__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __ge__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts >= other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__gt__</code></h2></summary> -->
<summary>
__gt__
</summary>
<!-- ### `__gt__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __gt__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts > other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__hash__</code></h2></summary> -->
<summary>
__hash__
</summary>
<!-- ### `__hash__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __hash__(self):
        try:
            return self._hash
        except AttributeError:
            self._hash = hash(tuple(self._cparts))
            return self._hash



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__le__</code></h2></summary> -->
<summary>
__le__
</summary>
<!-- ### `__le__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __le__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts <= other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__lt__</code></h2></summary> -->
<summary>
__lt__
</summary>
<!-- ### `__lt__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __lt__(self, other):
        if not isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return self._cparts < other._cparts



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__new__</code></h2></summary> -->
<summary>
__new__
</summary>
<!-- ### `__new__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == 'nt' else PosixPath
        self = cls._from_parts(args, init=False)
        if not self._flavour.is_supported:
            raise NotImplementedError("cannot instantiate %r on your system"
                                      % (cls.__name__,))
        self._init()
        return self



```

</details>

#### References

- [Path._init](#_init)

</details>


<details>
<!-- <summary><h2><code>__reduce__</code></h2></summary> -->
<summary>
__reduce__
</summary>
<!-- ### `__reduce__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __reduce__(self):
        # Using the parts tuple helps share interned path parts
        # when pickling related paths.
        return (self.__class__, tuple(self._parts))



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__repr__</code></h2></summary> -->
<summary>
__repr__
</summary>
<!-- ### `__repr__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.as_posix())



```

</details>

#### References

- [Path.as_posix](#as_posix)

</details>


<details>
<!-- <summary><h2><code>__rtruediv__</code></h2></summary> -->
<summary>
__rtruediv__
</summary>
<!-- ### `__rtruediv__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __rtruediv__(self, key):
        try:
            return self._from_parts([key] + self._parts)
        except TypeError:
            return NotImplemented



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__str__</code></h2></summary> -->
<summary>
__str__
</summary>
<!-- ### `__str__` -->
Method

Return the string representation of the path, suitable for


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __str__(self):
        """Return the string representation of the path, suitable for
        passing to system calls."""
        try:
            return self._str
        except AttributeError:
            self._str = self._format_parsed_parts(self._drv, self._root,
                                                  self._parts) or '.'
            return self._str



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__truediv__</code></h2></summary> -->
<summary>
__truediv__
</summary>
<!-- ### `__truediv__` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __truediv__(self, key):
        try:
            return self._make_child((key,))
        except TypeError:
            return NotImplemented



```

</details>

#### References

- [Path._make_child](#_make_child)

</details>


<details>
<!-- <summary><h2><code>_init</code></h2></summary> -->
<summary>
_init
</summary>
<!-- ### `_init` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _init(self,
              # Private non-constructor arguments
              template=None,
              ):
        if template is not None:
            self._accessor = template._accessor
        else:
            self._accessor = _normal_accessor



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_make_child</code></h2></summary> -->
<summary>
_make_child
</summary>
<!-- ### `_make_child` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _make_child(self, args):
        drv, root, parts = self._parse_args(args)
        drv, root, parts = self._flavour.join_parsed_parts(
            self._drv, self._root, self._parts, drv, root, parts)
        return self._from_parsed_parts(drv, root, parts)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_make_child_relpath</code></h2></summary> -->
<summary>
_make_child_relpath
</summary>
<!-- ### `_make_child_relpath` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _make_child_relpath(self, part):
        # This is an optimization used for dir walking.  `part` must be
        # a single part relative to this path.
        parts = self._parts + [part]
        return self._from_parsed_parts(self._drv, self._root, parts)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_opener</code></h2></summary> -->
<summary>
_opener
</summary>
<!-- ### `_opener` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _opener(self, name, flags, mode=0o666):
        # A stub for the opener argument to built-in open()
        return self._accessor.open(self, flags, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>_raw_open</code></h2></summary> -->
<summary>
_raw_open
</summary>
<!-- ### `_raw_open` -->
Method

as os.open() does.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def _raw_open(self, flags, mode=0o777):
        """
        Open the file pointed by this path and return a file descriptor,
        as os.open() does.
        """
        return self._accessor.open(self, flags, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>absolute</code></h2></summary> -->
<summary>
absolute
</summary>
<!-- ### `absolute` -->
Method

Return an absolute version of this path.  This function works


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def absolute(self):
        """Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        """
        # XXX untested yet!
        if self.is_absolute():
            return self
        # FIXME this must defer to the specific flavour (and, under Windows,
        # use nt._getfullpathname())
        obj = self._from_parts([os.getcwd()] + self._parts, init=False)
        obj._init(template=self)
        return obj



```

</details>

#### References

- [Path.is_absolute](#is_absolute)

</details>


<details>
<!-- <summary><h2><code>as_posix</code></h2></summary> -->
<summary>
as_posix
</summary>
<!-- ### `as_posix` -->
Method

Return the string representation of the path with forward (/)


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def as_posix(self):
        """Return the string representation of the path with forward (/)
        slashes."""
        f = self._flavour
        return str(self).replace(f.sep, '/')



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>as_uri</code></h2></summary> -->
<summary>
as_uri
</summary>
<!-- ### `as_uri` -->
Method

Return the path as a 'file' URI.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def as_uri(self):
        """Return the path as a 'file' URI."""
        if not self.is_absolute():
            raise ValueError("relative path can't be expressed as a file URI")
        return self._flavour.make_uri(self)



```

</details>

#### References

- [Path.is_absolute](#is_absolute)

</details>


<details>
<!-- <summary><h2><code>chmod</code></h2></summary> -->
<summary>
chmod
</summary>
<!-- ### `chmod` -->
Method

Change the permissions of the path, like os.chmod().


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def chmod(self, mode):
        """
        Change the permissions of the path, like os.chmod().
        """
        self._accessor.chmod(self, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>exists</code></h2></summary> -->
<summary>
exists
</summary>
<!-- ### `exists` -->
Method

Whether this path exists.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def exists(self):
        """
        Whether this path exists.
        """
        try:
            self.stat()
        except OSError as e:
            if not _ignore_error(e):
                raise
            return False
        except ValueError:
            # Non-encodable path
            return False
        return True



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>expanduser</code></h2></summary> -->
<summary>
expanduser
</summary>
<!-- ### `expanduser` -->
Method

Return a new path with expanded ~ and ~user constructs


#### Parameters

##### `(as returned by os.path.expanduser)`





##### ``



- kind, including directories) matching the given relative pattern.

- 

- a drive).

- 

- by the system, if any.

- result for the special paths '.' and '..'.

- 

- new path representing either a subpath (if all arguments are relative

- paths) or a totally different path (if one of the arguments is

- anchored).

- 

- arguments.  If the operation is not possible (because this is not

- a subpath of the other path), raise ValueError.

- 

- directories) matching the given relative pattern, anywhere in

- this subtree.

- 

- (as returned by os.path.samefile()).

- 

- has no suffix, add given suffix.  If the given suffix is an empty

- string, remove the suffix from the path.

- 



#### Source

<details>
<summary>View source</summary>

```python


    def expanduser(self):
        """ Return a new path with expanded ~ and ~user constructs
        (as returned by os.path.expanduser)
        """
        if (not (self._drv or self._root) and
            self._parts and self._parts[0][:1] == '~'):
            homedir = self._flavour.gethomedir(self._parts[0][1:])
            return self._from_parts([homedir] + self._parts[1:])

        return self



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>glob</code></h2></summary> -->
<summary>
glob
</summary>
<!-- ### `glob` -->
Method

Iterate over this subtree and yield all existing files (of any


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def glob(self, pattern):
        """Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        """
        sys.audit("pathlib.Path.glob", self, pattern)
        if not pattern:
            raise ValueError("Unacceptable pattern: {!r}".format(pattern))
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p



```

</details>

#### References

- [Path.glob](#glob)

</details>


<details>
<!-- <summary><h2><code>group</code></h2></summary> -->
<summary>
group
</summary>
<!-- ### `group` -->
Method

Return the group name of the file gid.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def group(self):
        """
        Return the group name of the file gid.
        """
        return self._accessor.group(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>is_absolute</code></h2></summary> -->
<summary>
is_absolute
</summary>
<!-- ### `is_absolute` -->
Method

True if the path is absolute (has both a root and, if applicable,


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_absolute(self):
        """True if the path is absolute (has both a root and, if applicable,
        a drive)."""
        if not self._root:
            return False
        return not self._flavour.has_drv or bool(self._drv)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>is_block_device</code></h2></summary> -->
<summary>
is_block_device
</summary>
<!-- ### `is_block_device` -->
Method

Whether this path is a block device.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_block_device(self):
        """
        Whether this path is a block device.
        """
        try:
            return S_ISBLK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_char_device</code></h2></summary> -->
<summary>
is_char_device
</summary>
<!-- ### `is_char_device` -->
Method

Whether this path is a character device.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_char_device(self):
        """
        Whether this path is a character device.
        """
        try:
            return S_ISCHR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_dir</code></h2></summary> -->
<summary>
is_dir
</summary>
<!-- ### `is_dir` -->
Method

Whether this path is a directory.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_dir(self):
        """
        Whether this path is a directory.
        """
        try:
            return S_ISDIR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_fifo</code></h2></summary> -->
<summary>
is_fifo
</summary>
<!-- ### `is_fifo` -->
Method

Whether this path is a FIFO.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_fifo(self):
        """
        Whether this path is a FIFO.
        """
        try:
            return S_ISFIFO(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_file</code></h2></summary> -->
<summary>
is_file
</summary>
<!-- ### `is_file` -->
Method

to regular files).


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_file(self):
        """
        Whether this path is a regular file (also True for symlinks pointing
        to regular files).
        """
        try:
            return S_ISREG(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_mount</code></h2></summary> -->
<summary>
is_mount
</summary>
<!-- ### `is_mount` -->
Method

Check if this path is a POSIX mount point


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_mount(self):
        """
        Check if this path is a POSIX mount point
        """
        # Need to exist and be a dir
        if not self.exists() or not self.is_dir():
            return False

        try:
            parent_dev = self.parent.stat().st_dev
        except OSError:
            return False

        dev = self.stat().st_dev
        if dev != parent_dev:
            return True
        ino = self.stat().st_ino
        parent_ino = self.parent.stat().st_ino
        return ino == parent_ino



```

</details>

#### References

- [Path.exists](#exists)
- [Path.is_dir](#is_dir)
- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_relative_to</code></h2></summary> -->
<summary>
is_relative_to
</summary>
<!-- ### `is_relative_to` -->
Method

Return True if the path is relative to another path or False.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_relative_to(self, *other):
        """Return True if the path is relative to another path or False.
        """
        try:
            self.relative_to(*other)
            return True
        except ValueError:
            return False



```

</details>

#### References

- [Path.relative_to](#relative_to)

</details>


<details>
<!-- <summary><h2><code>is_reserved</code></h2></summary> -->
<summary>
is_reserved
</summary>
<!-- ### `is_reserved` -->
Method

Return True if the path contains one of the special names reserved


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_reserved(self):
        """Return True if the path contains one of the special names reserved
        by the system, if any."""
        return self._flavour.is_reserved(self._parts)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>is_socket</code></h2></summary> -->
<summary>
is_socket
</summary>
<!-- ### `is_socket` -->
Method

Whether this path is a socket.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_socket(self):
        """
        Whether this path is a socket.
        """
        try:
            return S_ISSOCK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>is_symlink</code></h2></summary> -->
<summary>
is_symlink
</summary>
<!-- ### `is_symlink` -->
Method

Whether this path is a symbolic link.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def is_symlink(self):
        """
        Whether this path is a symbolic link.
        """
        try:
            return S_ISLNK(self.lstat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist
            return False
        except ValueError:
            # Non-encodable path
            return False



```

</details>

#### References

- [Path.lstat](#lstat)

</details>


<details>
<!-- <summary><h2><code>iterdir</code></h2></summary> -->
<summary>
iterdir
</summary>
<!-- ### `iterdir` -->
Method

Iterate over the files in this directory.  Does not yield any


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def iterdir(self):
        """Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        """
        for name in self._accessor.listdir(self):
            if name in {'.', '..'}:
                # Yielding a path object for these makes little sense
                continue
            yield self._make_child_relpath(name)



```

</details>

#### References

- [Path._make_child](#_make_child)
- [Path._make_child_relpath](#_make_child_relpath)

</details>


<details>
<!-- <summary><h2><code>joinpath</code></h2></summary> -->
<summary>
joinpath
</summary>
<!-- ### `joinpath` -->
Method

Combine this path with one or several arguments, and return a


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def joinpath(self, *args):
        """Combine this path with one or several arguments, and return a
        new path representing either a subpath (if all arguments are relative
        paths) or a totally different path (if one of the arguments is
        anchored).
        """
        return self._make_child(args)



```

</details>

#### References

- [Path._make_child](#_make_child)

</details>


<details>
<!-- <summary><h2><code>lchmod</code></h2></summary> -->
<summary>
lchmod
</summary>
<!-- ### `lchmod` -->
Method

permissions are changed, rather than its target's.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def lchmod(self, mode):
        """
        Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
        """
        self._accessor.lchmod(self, mode)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>link_to</code></h2></summary> -->
<summary>
link_to
</summary>
<!-- ### `link_to` -->
Method

Create a hard link pointing to a path named target.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def link_to(self, target):
        """
        Create a hard link pointing to a path named target.
        """
        self._accessor.link_to(self, target)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>lstat</code></h2></summary> -->
<summary>
lstat
</summary>
<!-- ### `lstat` -->
Method

status information is returned, rather than its target's.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def lstat(self):
        """
        Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
        """
        return self._accessor.lstat(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>match</code></h2></summary> -->
<summary>
match
</summary>
<!-- ### `match` -->
Method

Return True if this path matches the given pattern.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def match(self, path_pattern):
        """
        Return True if this path matches the given pattern.
        """
        cf = self._flavour.casefold
        path_pattern = cf(path_pattern)
        drv, root, pat_parts = self._flavour.parse_parts((path_pattern,))
        if not pat_parts:
            raise ValueError("empty pattern")
        if drv and drv != cf(self._drv):
            return False
        if root and root != cf(self._root):
            return False
        parts = self._cparts
        if drv or root:
            if len(pat_parts) != len(parts):
                return False
            pat_parts = pat_parts[1:]
        elif len(pat_parts) > len(parts):
            return False
        for part, pat in zip(reversed(parts), reversed(pat_parts)):
            if not fnmatch.fnmatchcase(part, pat):
                return False
        return True



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>mkdir</code></h2></summary> -->
<summary>
mkdir
</summary>
<!-- ### `mkdir` -->
Method

Create a new directory at this given path.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
            self._accessor.mkdir(self, mode)
        except FileNotFoundError:
            if not parents or self.parent == self:
                raise
            self.parent.mkdir(parents=True, exist_ok=True)
            self.mkdir(mode, parents=False, exist_ok=exist_ok)
        except OSError:
            # Cannot rely on checking for EEXIST, since the operating system
            # could give priority to other errors like EACCES or EROFS
            if not exist_ok or not self.is_dir():
                raise



```

</details>

#### References

- [Path.is_dir](#is_dir)
- [Path.mkdir](#mkdir)

</details>


<details>
<!-- <summary><h2><code>open</code></h2></summary> -->
<summary>
open
</summary>
<!-- ### `open` -->
Method

the built-in open() function does.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def open(self, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None):
        """
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.
        """
        return io.open(self, mode, buffering, encoding, errors, newline,
                       opener=self._opener)



```

</details>

#### References

- [Path._opener](#_opener)

</details>


<details>
<!-- <summary><h2><code>owner</code></h2></summary> -->
<summary>
owner
</summary>
<!-- ### `owner` -->
Method

Return the login name of the file owner.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def owner(self):
        """
        Return the login name of the file owner.
        """
        return self._accessor.owner(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>read_bytes</code></h2></summary> -->
<summary>
read_bytes
</summary>
<!-- ### `read_bytes` -->
Method

Open the file in bytes mode, read it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def read_bytes(self):
        """
        Open the file in bytes mode, read it, and close the file.
        """
        with self.open(mode='rb') as f:
            return f.read()



```

</details>

#### References

- [Path.open](#open)

</details>


<details>
<!-- <summary><h2><code>read_text</code></h2></summary> -->
<summary>
read_text
</summary>
<!-- ### `read_text` -->
Method

Open the file in text mode, read it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def read_text(self, encoding=None, errors=None):
        """
        Open the file in text mode, read it, and close the file.
        """
        with self.open(mode='r', encoding=encoding, errors=errors) as f:
            return f.read()



```

</details>

#### References

- [Path.open](#open)

</details>


<details>
<!-- <summary><h2><code>readlink</code></h2></summary> -->
<summary>
readlink
</summary>
<!-- ### `readlink` -->
Method

Return the path to which the symbolic link points.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def readlink(self):
        """
        Return the path to which the symbolic link points.
        """
        path = self._accessor.readlink(self)
        obj = self._from_parts((path,), init=False)
        obj._init(template=self)
        return obj



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>relative_to</code></h2></summary> -->
<summary>
relative_to
</summary>
<!-- ### `relative_to` -->
Method

Return the relative path to another path identified by the passed


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def relative_to(self, *other):
        """Return the relative path to another path identified by the passed
        arguments.  If the operation is not possible (because this is not
        a subpath of the other path), raise ValueError.
        """
        # For the purpose of this method, drive and root are considered
        # separate parts, i.e.:
        #   Path('c:/').relative_to('c:')  gives Path('/')
        #   Path('c:/').relative_to('/')   raise ValueError
        if not other:
            raise TypeError("need at least one argument")
        parts = self._parts
        drv = self._drv
        root = self._root
        if root:
            abs_parts = [drv, root] + parts[1:]
        else:
            abs_parts = parts
        to_drv, to_root, to_parts = self._parse_args(other)
        if to_root:
            to_abs_parts = [to_drv, to_root] + to_parts[1:]
        else:
            to_abs_parts = to_parts
        n = len(to_abs_parts)
        cf = self._flavour.casefold_parts
        if (root or drv) if n == 0 else cf(abs_parts[:n]) != cf(to_abs_parts):
            formatted = self._format_parsed_parts(to_drv, to_root, to_parts)
            raise ValueError("{!r} is not in the subpath of {!r}"
                    " OR one path is relative and the other is absolute."
                             .format(str(self), str(formatted)))
        return self._from_parsed_parts('', root if n == 1 else '',
                                       abs_parts[n:])



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>rename</code></h2></summary> -->
<summary>
rename
</summary>
<!-- ### `rename` -->
Method

directory of the Path object.


#### Parameters

##### `Returns the new Path instance pointing to the target path.`

{parameter_info}




#### Source

<details>
<summary>View source</summary>

```python


    def rename(self, target):
        """
        Rename this path to the target path.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.rename(self, target)
        return self.__class__(target)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>replace</code></h2></summary> -->
<summary>
replace
</summary>
<!-- ### `replace` -->
Method

directory of the Path object.


#### Parameters

##### `Returns the new Path instance pointing to the target path.`

{parameter_info}




#### Source

<details>
<summary>View source</summary>

```python


    def replace(self, target):
        """
        Rename this path to the target path, overwriting if that path exists.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.replace(self, target)
        return self.__class__(target)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>resolve</code></h2></summary> -->
<summary>
resolve
</summary>
<!-- ### `resolve` -->
Method

Windows).


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def resolve(self, strict=False):
        """
        Make the path absolute, resolving all symlinks on the way and also
        normalizing it (for example turning slashes into backslashes under
        Windows).
        """
        s = self._flavour.resolve(self, strict=strict)
        if s is None:
            # No symlink resolution => for consistency, raise an error if
            # the path doesn't exist or is forbidden
            self.stat()
            s = str(self.absolute())
        # Now we have no symlinks in the path, it's safe to normalize it.
        normed = self._flavour.pathmod.normpath(s)
        obj = self._from_parts((normed,), init=False)
        obj._init(template=self)
        return obj



```

</details>

#### References

- [Path.absolute](#absolute)
- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>rglob</code></h2></summary> -->
<summary>
rglob
</summary>
<!-- ### `rglob` -->
Method

Recursively yield all existing files (of any kind, including


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def rglob(self, pattern):
        """Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        """
        sys.audit("pathlib.Path.rglob", self, pattern)
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(("**",) + tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p



```

</details>

#### References

- [Path.rglob](#rglob)

</details>


<details>
<!-- <summary><h2><code>rmdir</code></h2></summary> -->
<summary>
rmdir
</summary>
<!-- ### `rmdir` -->
Method

Remove this directory.  The directory must be empty.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def rmdir(self):
        """
        Remove this directory.  The directory must be empty.
        """
        self._accessor.rmdir(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>samefile</code></h2></summary> -->
<summary>
samefile
</summary>
<!-- ### `samefile` -->
Method

Return whether other_path is the same or not as this file


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def samefile(self, other_path):
        """Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        """
        st = self.stat()
        try:
            other_st = other_path.stat()
        except AttributeError:
            other_st = self._accessor.stat(other_path)
        return os.path.samestat(st, other_st)



```

</details>

#### References

- [Path.stat](#stat)

</details>


<details>
<!-- <summary><h2><code>stat</code></h2></summary> -->
<summary>
stat
</summary>
<!-- ### `stat` -->
Method

os.stat() does.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def stat(self):
        """
        Return the result of the stat() system call on this path, like
        os.stat() does.
        """
        return self._accessor.stat(self)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>symlink_to</code></h2></summary> -->
<summary>
symlink_to
</summary>
<!-- ### `symlink_to` -->
Method

Note the order of arguments (self, target) is the reverse of os.symlink's.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def symlink_to(self, target, target_is_directory=False):
        """
        Make this path a symlink pointing to the given path.
        Note the order of arguments (self, target) is the reverse of os.symlink's.
        """
        self._accessor.symlink(target, self, target_is_directory)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>touch</code></h2></summary> -->
<summary>
touch
</summary>
<!-- ### `touch` -->
Method

Create this file with the given access mode, if it doesn't exist.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def touch(self, mode=0o666, exist_ok=True):
        """
        Create this file with the given access mode, if it doesn't exist.
        """
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                self._accessor.utime(self, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
        fd = self._raw_open(flags, mode)
        os.close(fd)



```

</details>

#### References

- [Path._raw_open](#_raw_open)

</details>


<details>
<!-- <summary><h2><code>unlink</code></h2></summary> -->
<summary>
unlink
</summary>
<!-- ### `unlink` -->
Method

If the path is a directory, use rmdir() instead.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def unlink(self, missing_ok=False):
        """
        Remove this file or link.
        If the path is a directory, use rmdir() instead.
        """
        try:
            self._accessor.unlink(self)
        except FileNotFoundError:
            if not missing_ok:
                raise



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>with_name</code></h2></summary> -->
<summary>
with_name
</summary>
<!-- ### `with_name` -->
Method

Return a new path with the file name changed.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def with_name(self, name):
        """Return a new path with the file name changed."""
        if not self.name:
            raise ValueError("%r has an empty name" % (self,))
        drv, root, parts = self._flavour.parse_parts((name,))
        if (not name or name[-1] in [self._flavour.sep, self._flavour.altsep]
            or drv or root or len(parts) != 1):
            raise ValueError("Invalid name %r" % (name))
        return self._from_parsed_parts(self._drv, self._root,
                                       self._parts[:-1] + [name])



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>with_stem</code></h2></summary> -->
<summary>
with_stem
</summary>
<!-- ### `with_stem` -->
Method

Return a new path with the stem changed.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def with_stem(self, stem):
        """Return a new path with the stem changed."""
        return self.with_name(stem + self.suffix)



```

</details>

#### References

- [Path.with_name](#with_name)

</details>


<details>
<!-- <summary><h2><code>with_suffix</code></h2></summary> -->
<summary>
with_suffix
</summary>
<!-- ### `with_suffix` -->
Method

Return a new path with the file suffix changed.  If the path


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def with_suffix(self, suffix):
        """Return a new path with the file suffix changed.  If the path
        has no suffix, add given suffix.  If the given suffix is an empty
        string, remove the suffix from the path.
        """
        f = self._flavour
        if f.sep in suffix or f.altsep and f.altsep in suffix:
            raise ValueError("Invalid suffix %r" % (suffix,))
        if suffix and not suffix.startswith('.') or suffix == '.':
            raise ValueError("Invalid suffix %r" % (suffix))
        name = self.name
        if not name:
            raise ValueError("%r has an empty name" % (self,))
        old_suffix = self.suffix
        if not old_suffix:
            name = name + suffix
        else:
            name = name[:-len(old_suffix)] + suffix
        return self._from_parsed_parts(self._drv, self._root,
                                       self._parts[:-1] + [name])



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>write_bytes</code></h2></summary> -->
<summary>
write_bytes
</summary>
<!-- ### `write_bytes` -->
Method

Open the file in bytes mode, write to it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def write_bytes(self, data):
        """
        Open the file in bytes mode, write to it, and close the file.
        """
        # type-check for the buffer interface before truncating the file
        view = memoryview(data)
        with self.open(mode='wb') as f:
            return f.write(view)



```

</details>

#### References

- [Path.open](#open)

</details>


<details>
<!-- <summary><h2><code>write_text</code></h2></summary> -->
<summary>
write_text
</summary>
<!-- ### `write_text` -->
Method

Open the file in text mode, write to it, and close the file.


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def write_text(self, data, encoding=None, errors=None):
        """
        Open the file in text mode, write to it, and close the file.
        """
        if not isinstance(data, str):
            raise TypeError('data must be str, not %s' %
                            data.__class__.__name__)
        with self.open(mode='w', encoding=encoding, errors=errors) as f:
            return f.write(data)



```

</details>

#### References

- [Path.open](#open)

</details>


Docs built at 2021-06-16 05:12:41.161415

<details>
<summary>View source</summary>

```python

class Path(PurePath):
    """PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiate a PosixPath or WindowsPath directly,
    but cannot instantiate a WindowsPath on a POSIX system or vice versa.
    """
    __slots__ = (
        '_accessor',
    )

    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == 'nt' else PosixPath
        self = cls._from_parts(args, init=False)
        if not self._flavour.is_supported:
            raise NotImplementedError("cannot instantiate %r on your system"
                                      % (cls.__name__,))
        self._init()
        return self

    def _init(self,
              # Private non-constructor arguments
              template=None,
              ):
        if template is not None:
            self._accessor = template._accessor
        else:
            self._accessor = _normal_accessor

    def _make_child_relpath(self, part):
        # This is an optimization used for dir walking.  `part` must be
        # a single part relative to this path.
        parts = self._parts + [part]
        return self._from_parsed_parts(self._drv, self._root, parts)

    def __enter__(self):
        return self

    def __exit__(self, t, v, tb):
        # https://bugs.python.org/issue39682
        # In previous versions of pathlib, this method marked this path as
        # closed; subsequent attempts to perform I/O would raise an IOError.
        # This functionality was never documented, and had the effect of
        # making Path objects mutable, contrary to PEP 428. In Python 3.9 the
        # _closed attribute was removed, and this method made a no-op.
        # This method and __enter__()/__exit__() should be deprecated and
        # removed in the future.
        pass

    def _opener(self, name, flags, mode=0o666):
        # A stub for the opener argument to built-in open()
        return self._accessor.open(self, flags, mode)

    def _raw_open(self, flags, mode=0o777):
        """
        Open the file pointed by this path and return a file descriptor,
        as os.open() does.
        """
        return self._accessor.open(self, flags, mode)

    # Public API

    @classmethod
    def cwd(cls):
        """Return a new path pointing to the current working directory
        (as returned by os.getcwd()).
        """
        return cls(os.getcwd())

    @classmethod
    def home(cls):
        """Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
        """
        return cls(cls()._flavour.gethomedir(None))

    def samefile(self, other_path):
        """Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        """
        st = self.stat()
        try:
            other_st = other_path.stat()
        except AttributeError:
            other_st = self._accessor.stat(other_path)
        return os.path.samestat(st, other_st)

    def iterdir(self):
        """Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        """
        for name in self._accessor.listdir(self):
            if name in {'.', '..'}:
                # Yielding a path object for these makes little sense
                continue
            yield self._make_child_relpath(name)

    def glob(self, pattern):
        """Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        """
        sys.audit("pathlib.Path.glob", self, pattern)
        if not pattern:
            raise ValueError("Unacceptable pattern: {!r}".format(pattern))
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p

    def rglob(self, pattern):
        """Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        """
        sys.audit("pathlib.Path.rglob", self, pattern)
        drv, root, pattern_parts = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError("Non-relative patterns are unsupported")
        selector = _make_selector(("**",) + tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p

    def absolute(self):
        """Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        """
        # XXX untested yet!
        if self.is_absolute():
            return self
        # FIXME this must defer to the specific flavour (and, under Windows,
        # use nt._getfullpathname())
        obj = self._from_parts([os.getcwd()] + self._parts, init=False)
        obj._init(template=self)
        return obj

    def resolve(self, strict=False):
        """
        Make the path absolute, resolving all symlinks on the way and also
        normalizing it (for example turning slashes into backslashes under
        Windows).
        """
        s = self._flavour.resolve(self, strict=strict)
        if s is None:
            # No symlink resolution => for consistency, raise an error if
            # the path doesn't exist or is forbidden
            self.stat()
            s = str(self.absolute())
        # Now we have no symlinks in the path, it's safe to normalize it.
        normed = self._flavour.pathmod.normpath(s)
        obj = self._from_parts((normed,), init=False)
        obj._init(template=self)
        return obj

    def stat(self):
        """
        Return the result of the stat() system call on this path, like
        os.stat() does.
        """
        return self._accessor.stat(self)

    def owner(self):
        """
        Return the login name of the file owner.
        """
        return self._accessor.owner(self)

    def group(self):
        """
        Return the group name of the file gid.
        """
        return self._accessor.group(self)

    def open(self, mode='r', buffering=-1, encoding=None,
             errors=None, newline=None):
        """
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.
        """
        return io.open(self, mode, buffering, encoding, errors, newline,
                       opener=self._opener)

    def read_bytes(self):
        """
        Open the file in bytes mode, read it, and close the file.
        """
        with self.open(mode='rb') as f:
            return f.read()

    def read_text(self, encoding=None, errors=None):
        """
        Open the file in text mode, read it, and close the file.
        """
        with self.open(mode='r', encoding=encoding, errors=errors) as f:
            return f.read()

    def write_bytes(self, data):
        """
        Open the file in bytes mode, write to it, and close the file.
        """
        # type-check for the buffer interface before truncating the file
        view = memoryview(data)
        with self.open(mode='wb') as f:
            return f.write(view)

    def write_text(self, data, encoding=None, errors=None):
        """
        Open the file in text mode, write to it, and close the file.
        """
        if not isinstance(data, str):
            raise TypeError('data must be str, not %s' %
                            data.__class__.__name__)
        with self.open(mode='w', encoding=encoding, errors=errors) as f:
            return f.write(data)

    def readlink(self):
        """
        Return the path to which the symbolic link points.
        """
        path = self._accessor.readlink(self)
        obj = self._from_parts((path,), init=False)
        obj._init(template=self)
        return obj

    def touch(self, mode=0o666, exist_ok=True):
        """
        Create this file with the given access mode, if it doesn't exist.
        """
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                self._accessor.utime(self, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
        fd = self._raw_open(flags, mode)
        os.close(fd)

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
            self._accessor.mkdir(self, mode)
        except FileNotFoundError:
            if not parents or self.parent == self:
                raise
            self.parent.mkdir(parents=True, exist_ok=True)
            self.mkdir(mode, parents=False, exist_ok=exist_ok)
        except OSError:
            # Cannot rely on checking for EEXIST, since the operating system
            # could give priority to other errors like EACCES or EROFS
            if not exist_ok or not self.is_dir():
                raise

    def chmod(self, mode):
        """
        Change the permissions of the path, like os.chmod().
        """
        self._accessor.chmod(self, mode)

    def lchmod(self, mode):
        """
        Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
        """
        self._accessor.lchmod(self, mode)

    def unlink(self, missing_ok=False):
        """
        Remove this file or link.
        If the path is a directory, use rmdir() instead.
        """
        try:
            self._accessor.unlink(self)
        except FileNotFoundError:
            if not missing_ok:
                raise

    def rmdir(self):
        """
        Remove this directory.  The directory must be empty.
        """
        self._accessor.rmdir(self)

    def lstat(self):
        """
        Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
        """
        return self._accessor.lstat(self)

    def link_to(self, target):
        """
        Create a hard link pointing to a path named target.
        """
        self._accessor.link_to(self, target)

    def rename(self, target):
        """
        Rename this path to the target path.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.rename(self, target)
        return self.__class__(target)

    def replace(self, target):
        """
        Rename this path to the target path, overwriting if that path exists.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        """
        self._accessor.replace(self, target)
        return self.__class__(target)

    def symlink_to(self, target, target_is_directory=False):
        """
        Make this path a symlink pointing to the given path.
        Note the order of arguments (self, target) is the reverse of os.symlink's.
        """
        self._accessor.symlink(target, self, target_is_directory)

    # Convenience functions for querying the stat results

    def exists(self):
        """
        Whether this path exists.
        """
        try:
            self.stat()
        except OSError as e:
            if not _ignore_error(e):
                raise
            return False
        except ValueError:
            # Non-encodable path
            return False
        return True

    def is_dir(self):
        """
        Whether this path is a directory.
        """
        try:
            return S_ISDIR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_file(self):
        """
        Whether this path is a regular file (also True for symlinks pointing
        to regular files).
        """
        try:
            return S_ISREG(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_mount(self):
        """
        Check if this path is a POSIX mount point
        """
        # Need to exist and be a dir
        if not self.exists() or not self.is_dir():
            return False

        try:
            parent_dev = self.parent.stat().st_dev
        except OSError:
            return False

        dev = self.stat().st_dev
        if dev != parent_dev:
            return True
        ino = self.stat().st_ino
        parent_ino = self.parent.stat().st_ino
        return ino == parent_ino

    def is_symlink(self):
        """
        Whether this path is a symbolic link.
        """
        try:
            return S_ISLNK(self.lstat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_block_device(self):
        """
        Whether this path is a block device.
        """
        try:
            return S_ISBLK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_char_device(self):
        """
        Whether this path is a character device.
        """
        try:
            return S_ISCHR(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_fifo(self):
        """
        Whether this path is a FIFO.
        """
        try:
            return S_ISFIFO(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def is_socket(self):
        """
        Whether this path is a socket.
        """
        try:
            return S_ISSOCK(self.stat().st_mode)
        except OSError as e:
            if not _ignore_error(e):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False
        except ValueError:
            # Non-encodable path
            return False

    def expanduser(self):
        """ Return a new path with expanded ~ and ~user constructs
        (as returned by os.path.expanduser)
        """
        if (not (self._drv or self._root) and
            self._parts and self._parts[0][:1] == '~'):
            homedir = self._flavour.gethomedir(self._parts[0][1:])
            return self._from_parts([homedir] + self._parts[1:])

        return self


```
</details>

</details>

<!-- ## Section -->

<details>
<summary>
Section
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

Create a new section


#### Parameters

##### `Params`

{parameter_info}

##### `type_`

 The type of section



##### `templates`

 A dictionary pairing template names to their contents



##### `parent`

 The parent section



##### `**kwargs`

 Additional arguments and/or data for the section





#### Source

<details>
<summary>View source</summary>

```python


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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>add</code></h2></summary> -->
<summary>
add
</summary>
<!-- ### `add` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def add(self, x):
        self.children.append(x)
        return x



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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>names</code></h2></summary> -->
<summary>
names
</summary>
<!-- ### `names` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def names(self):
        return [c.type for c in self.children]



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>set</code></h2></summary> -->
<summary>
set
</summary>
<!-- ### `set` -->
Method

Set a property of the section


#### Parameters

##### `Params`

{parameter_info}

##### `a`

 The name of the property



##### `b`

 The value to set the property to





#### Source

<details>
<summary>View source</summary>

```python


    def set(self, a, b):
        """
        Set a property of the section

        Params:
            a: The name of the property
            b: The value to set the property to
        """
        self.kwargs[a] = b



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.299048

<details>
<summary>View source</summary>

```python

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


```
</details>

</details>

<!-- ## Diagram -->

<details>
<summary>
Diagram
</summary>

Class

*module `diagrams`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new diagram object


#### Parameters

##### `Params`

{parameter_info}

##### `objects`

 The elements to initialize the Diagram with



##### `dims`

 The size of the diagram; `[width, height]`



##### `background`

 The Diagram's background

- A character to use for each cell of the background

- `'random'`: a value will be automatically selected


##### `origin`

 The position that should be used for the center of the coordinate system (i.e., `(0, 0)`)



##### `hue`

 The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value



##### `saturation`

 The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)



##### `value`

 Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)



##### `direction`







#### Source

<details>
<summary>View source</summary>

```python


	def __init__(self,
		objects=None,
		dims=[30, 30],
		background='&nbsp;',
		origin='center',
		hue=0,
		saturation=50,
		value=50,
		direction=None,
		**kwargs
	):
		"""
		Create a new diagram object

		Params:
			objects: The elements to initialize the Diagram with
			dims: The size of the diagram; `[width, height]`
			background: The Diagram's background
				A character to use for each cell of the background
				`'random'`: a value will be automatically selected
			origin: The position that should be used for the center of the coordinate system (i.e., `(0, 0)`)
			hue: The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value
			saturation: The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)
			value: Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)
			direction
		"""

		self.objects = objects if objects else []
		self.id = uuid.uuid4()
		self.canvas = []
		self.dims = dims
		self.x, self.y = self.dims
		self.background = background
		self.offset = [0, 0]

		self.hue = hue
		self.saturation = saturation
		self.value = value

		self.shades = ['light {}', 'medium {}', 'dark {}', 'full block']
		for i, s in enumerate(self.shades):
			num_fields = s.count('{}')
			if num_fields == 1:
				self.shades[i] = s.format('shade')
			self.shades[i] = get_char(self.shades[i])

		self.directions = ['right', 'down', 'left', 'up']
		self.cardinal = ['east', 'south', 'west', 'north']
		# self.arrows = [
		#	 '{}wards arrow',
		#	 '{} {} sans-serif arrow'
		# ]
		# for i, d in enumerate(self.directions):
		self.arrows = '🡢🡦🡣🡧🡠🡤🡡🡥'
		self.direction = direction

		self.origin = origin
		if self.origin == 'center':
			self.offset = [self.x//2, self.y//2]



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>add</code></h2></summary> -->
<summary>
add
</summary>
<!-- ### `add` -->
Method

Add an element to this diagram


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


	def add(self, element):
		"""
		Add an element to this diagram
		"""
		self.objects.append(element)
		return self



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>render</code></h2></summary> -->
<summary>
render
</summary>
<!-- ### `render` -->
Method

Convert the diagram's elements to a portable string and optionally save the generated document


#### Parameters

##### `Params`

{parameter_info}

##### `path`

 The base path to save the result to



##### `extensions`

 Versions of the output to generate and save

- md

- html

- txt


##### `rich_output`

 Whether to use HTML tags and CSS attributes to style Markdown content



##### `Returns`

{parameter_info}

##### `self`








#### Source

<details>
<summary>View source</summary>

```python


	def render(self,
		path:str='./generated-diagram.txt',
		extensions:list[str]=None,
		rich_output:bool=False,
		**kwargs
	) -> 'Diagram':
		"""
		Convert the diagram's elements to a portable string and optionally save the generated document

		Params:
			path: The base path to save the result to
			extensions: Versions of the output to generate and save
				md
				html
				txt
			rich_output: Whether to use HTML tags and CSS attributes to style Markdown content

		Returns:
			self
		"""

		# Generate the "canvas"; a two-dimensional list storing the character at each position
		bg = self.background
		self.canvas = []
		for i in range(self.y):
			row = []
			for j in range(self.x):
				if bg == 'random':
					cell = self.shades[random.randint(0, 3)]
				else:
					cell = bg

				if callable(self.direction):
					a = np.array([j, i]) - np.array(self.offset)
					z = self.direction(*a)
					theta = math.degrees(math.atan2(*z[::-1]))
					cell = self.arrows[round(theta / 360 * 8)]

				if rich_output:
					if callable(self.hue):
						a = np.array([j, i]) - np.array(self.offset)
						h = self.hue(*a)
					else:
						h = self.hue

					tag = 'span'
					colors = map(round, [h, self.saturation, self.value])
					cell = '<{} style="color: hsl({},{}%,{}%);">{}</ {} >'.format(tag, *colors, cell, tag)

				row.append(cell)
			self.canvas.append(row)

		# Render each object and add it to the canvas
		for o in self.objects:
			t = o.render(rich_output=rich_output, **kwargs)
			# If a 1D list is provided, add a wrapper list around it
			if t and type(t[0]) not in [list, tuple]:
				t = [t]
			# Add each character from the rendered element
			for i, row in enumerate(t):
				for j, c in enumerate(row):
					xc, yc = o.x+j, o.y+i
					if c and yc < self.y and xc < self.x:
						self.canvas[yc][xc] = c

		joiner = '<br>' if rich_output else '\n'
		# Combine canvas characters into an exportable string
		self.text = joiner.join(''.join(map(str, row)) for row in self.canvas)


		if rich_output:
			self.text = '<div><p>{}</p></div>'.format(self.text)

		if extensions:
			for e in extensions:
				self.write(path+'.'+e, self.text)
		else:
			self.write(path, self.text)

		return self



```

</details>

#### References

- [Diagram.write](#write)

</details>


<details>
<!-- <summary><h2><code>write</code></h2></summary> -->
<summary>
write
</summary>
<!-- ### `write` -->
Method

Create a new file and insert UTF-8-encoded text data or update an existing file


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


	def write(self, path, data) -> 'Diagram':
		"""
		Create a new file and insert UTF-8-encoded text data or update an existing file
		"""
		# Write the string to a file
		with open(path, 'w', encoding='utf-8') as file:
			file.write(data)
		return self



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.313010

<details>
<summary>View source</summary>

```python

class Diagram:
	"""
	A diagram containing some graphical elements and their relationships.
	"""

	objects: list[Element]
	dims: list[int]
	x: int
	y: int
	offset: list[int]
	hue: int
	saturation: int
	value: int

	def __init__(self,
		objects=None,
		dims=[30, 30],
		background='&nbsp;',
		origin='center',
		hue=0,
		saturation=50,
		value=50,
		direction=None,
		**kwargs
	):
		"""
		Create a new diagram object

		Params:
			objects: The elements to initialize the Diagram with
			dims: The size of the diagram; `[width, height]`
			background: The Diagram's background
				A character to use for each cell of the background
				`'random'`: a value will be automatically selected
			origin: The position that should be used for the center of the coordinate system (i.e., `(0, 0)`)
			hue: The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value
			saturation: The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)
			value: Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)
			direction
		"""

		self.objects = objects if objects else []
		self.id = uuid.uuid4()
		self.canvas = []
		self.dims = dims
		self.x, self.y = self.dims
		self.background = background
		self.offset = [0, 0]

		self.hue = hue
		self.saturation = saturation
		self.value = value

		self.shades = ['light {}', 'medium {}', 'dark {}', 'full block']
		for i, s in enumerate(self.shades):
			num_fields = s.count('{}')
			if num_fields == 1:
				self.shades[i] = s.format('shade')
			self.shades[i] = get_char(self.shades[i])

		self.directions = ['right', 'down', 'left', 'up']
		self.cardinal = ['east', 'south', 'west', 'north']
		# self.arrows = [
		#	 '{}wards arrow',
		#	 '{} {} sans-serif arrow'
		# ]
		# for i, d in enumerate(self.directions):
		self.arrows = '🡢🡦🡣🡧🡠🡤🡡🡥'
		self.direction = direction

		self.origin = origin
		if self.origin == 'center':
			self.offset = [self.x//2, self.y//2]

	def write(self, path, data) -> 'Diagram':
		"""
		Create a new file and insert UTF-8-encoded text data or update an existing file
		"""
		# Write the string to a file
		with open(path, 'w', encoding='utf-8') as file:
			file.write(data)
		return self

	def render(self,
		path:str='./generated-diagram.txt',
		extensions:list[str]=None,
		rich_output:bool=False,
		**kwargs
	) -> 'Diagram':
		"""
		Convert the diagram's elements to a portable string and optionally save the generated document

		Params:
			path: The base path to save the result to
			extensions: Versions of the output to generate and save
				md
				html
				txt
			rich_output: Whether to use HTML tags and CSS attributes to style Markdown content

		Returns:
			self
		"""

		# Generate the "canvas"; a two-dimensional list storing the character at each position
		bg = self.background
		self.canvas = []
		for i in range(self.y):
			row = []
			for j in range(self.x):
				if bg == 'random':
					cell = self.shades[random.randint(0, 3)]
				else:
					cell = bg

				if callable(self.direction):
					a = np.array([j, i]) - np.array(self.offset)
					z = self.direction(*a)
					theta = math.degrees(math.atan2(*z[::-1]))
					cell = self.arrows[round(theta / 360 * 8)]

				if rich_output:
					if callable(self.hue):
						a = np.array([j, i]) - np.array(self.offset)
						h = self.hue(*a)
					else:
						h = self.hue

					tag = 'span'
					colors = map(round, [h, self.saturation, self.value])
					cell = '<{} style="color: hsl({},{}%,{}%);">{}</ {} >'.format(tag, *colors, cell, tag)

				row.append(cell)
			self.canvas.append(row)

		# Render each object and add it to the canvas
		for o in self.objects:
			t = o.render(rich_output=rich_output, **kwargs)
			# If a 1D list is provided, add a wrapper list around it
			if t and type(t[0]) not in [list, tuple]:
				t = [t]
			# Add each character from the rendered element
			for i, row in enumerate(t):
				for j, c in enumerate(row):
					xc, yc = o.x+j, o.y+i
					if c and yc < self.y and xc < self.x:
						self.canvas[yc][xc] = c

		joiner = '<br>' if rich_output else '\n'
		# Combine canvas characters into an exportable string
		self.text = joiner.join(''.join(map(str, row)) for row in self.canvas)


		if rich_output:
			self.text = '<div><p>{}</p></div>'.format(self.text)

		if extensions:
			for e in extensions:
				self.write(path+'.'+e, self.text)
		else:
			self.write(path, self.text)

		return self

	def add(self, element):
		"""
		Add an element to this diagram
		"""
		self.objects.append(element)
		return self


```
</details>

</details>

<!-- ## Element -->

<details>
<summary>
Element
</summary>

Class

*module `diagrams`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)


#### Parameters

##### `Params`

{parameter_info}

##### `pos`

 Coordinates of the element in the scene



##### `Attributes`

{parameter_info}

##### `pos`

  Coordinates of the element in the scene (inserted from docs for `Element.__init__#pos`)



##### `x`

 The x coordinate



##### `y`

 The y coordinate



##### `id`

 The UUID of this element






#### Source

<details>
<summary>View source</summary>

```python


	def __init__(self, pos):
		"""
		Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)

		Params:
			pos: Coordinates of the element in the scene

		Attributes:
			pos: $$
			x: The x coordinate
			y: The y coordinate
			id: The UUID of this element
		"""

		# Upper left-hand corner of bounding box (inclusive)
		self.pos = pos if pos else [0, 0]
		self.x, self.y = self.pos
		self.id = uuid.uuid4()



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.327969

<details>
<summary>View source</summary>

```python

class Element:
	"""A generic element to be added to a diagram"""

	def __init__(self, pos):
		"""
		Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)

		Params:
			pos: Coordinates of the element in the scene

		Attributes:
			pos: $$
			x: The x coordinate
			y: The y coordinate
			id: The UUID of this element
		"""

		# Upper left-hand corner of bounding box (inclusive)
		self.pos = pos if pos else [0, 0]
		self.x, self.y = self.pos
		self.id = uuid.uuid4()


```
</details>

</details>

<!-- ## Point -->

<details>
<summary>
Point
</summary>

Class

*module `diagrams`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__call__</code></h2></summary> -->
<summary>
__call__
</summary>
<!-- ### `__call__` -->
Method

{method_info}


#### Parameters

##### `Returns this point's position`

{parameter_info}




#### Source

<details>
<summary>View source</summary>

```python


    def __call__(self):
        """
        Returns this point's position
        """
        return self.pos



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new Point instance


#### Parameters

##### `Params`

{parameter_info}

##### `pos`

 The new point's position in the coordinate system



##### `p`

 The level of precision to store the point's position with





#### Source

<details>
<summary>View source</summary>

```python


    def __init__(self, pos:list, p:int=8):
        """
        Create a new Point instance

        Params:
            pos: The new point's position in the coordinate system
            p: The level of precision to store the point's position with
        """
        self.pos = np.array(pos, dtype=float)
        self.precision = p



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>__str__</code></h2></summary> -->
<summary>
__str__
</summary>
<!-- ### `__str__` -->
Method

Generate a string representation of this point


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def __str__(self):
        """
        Generate a string representation of this point
        """
        return 'Point ' + str(self.pos)



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>move</code></h2></summary> -->
<summary>
move
</summary>
<!-- ### `move` -->
Method

Translate the point


#### Parameters

##### `Params`

{parameter_info}

##### `delta`

 A list of offsets to move the point along each axis in space by





#### Source

<details>
<summary>View source</summary>

```python


    def move(self, delta:list):
        """
        Translate the point

        Params:
            delta: A list of offsets to move the point along each axis in space by
        """
        self.pos += np.array(delta)
        return self



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>print</code></h2></summary> -->
<summary>
print
</summary>
<!-- ### `print` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def print(self):
        print(self)
        return self



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>rotate</code></h2></summary> -->
<summary>
rotate
</summary>
<!-- ### `rotate` -->
Method

Rotate the point about another


#### Parameters

##### `Params`

{parameter_info}

##### `a`

 The point to rotate about



##### `theta`

 The rotation to apply to the point, in degrees



##### `rad`

 The rotation in radians (supersedes `theta`)





#### Source

<details>
<summary>View source</summary>

```python


    def rotate(self, a:list, theta:int, rad:float=None):
        """
        Rotate the point about another

        Params:
            a: The point to rotate about
            theta: The rotation to apply to the point, in degrees
            rad: The rotation in radians (supersedes `theta`)
        """
        theta = float(theta)
        # Convert to radians
        if not rad:
            theta = theta * math.pi / 180
        # Create a rotation matrix to apply a rotation to the point
        rotation_matrix = [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ]
#         print(rotation_matrix)
#         self.pos *= rotation_matrix

        # Move the point so its coordinate is relative to the origin
        self.move(-a.pos)
        # Apply the rotation matrix
        self.pos = np.dot(self.pos, rotation_matrix)
        # Move point back
        self.move(a.pos)
        # Round to specified precision
        self.pos = self.pos.round(self.precision)
        return self



```

</details>

#### References

- [Point.move](#move)

</details>


Docs built at 2021-06-16 05:12:41.332957

<details>
<summary>View source</summary>

```python

class Point:
    pos: np.ndarray
    precision: int

    def __init__(self, pos:list, p:int=8):
        """
        Create a new Point instance

        Params:
            pos: The new point's position in the coordinate system
            p: The level of precision to store the point's position with
        """
        self.pos = np.array(pos, dtype=float)
        self.precision = p

    def move(self, delta:list):
        """
        Translate the point

        Params:
            delta: A list of offsets to move the point along each axis in space by
        """
        self.pos += np.array(delta)
        return self

    def rotate(self, a:list, theta:int, rad:float=None):
        """
        Rotate the point about another

        Params:
            a: The point to rotate about
            theta: The rotation to apply to the point, in degrees
            rad: The rotation in radians (supersedes `theta`)
        """
        theta = float(theta)
        # Convert to radians
        if not rad:
            theta = theta * math.pi / 180
        # Create a rotation matrix to apply a rotation to the point
        rotation_matrix = [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ]
#         print(rotation_matrix)
#         self.pos *= rotation_matrix

        # Move the point so its coordinate is relative to the origin
        self.move(-a.pos)
        # Apply the rotation matrix
        self.pos = np.dot(self.pos, rotation_matrix)
        # Move point back
        self.move(a.pos)
        # Round to specified precision
        self.pos = self.pos.round(self.precision)
        return self

    def __call__(self):
        """
        Returns this point's position
        """
        return self.pos

    def print(self):
        print(self)
        return self

    def __str__(self):
        """
        Generate a string representation of this point
        """
        return 'Point ' + str(self.pos)


```
</details>

</details>

<!-- ## Text -->

<details>
<summary>
Text
</summary>

Class

*module `diagrams`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new text element


#### Parameters

##### `Params`

{parameter_info}

##### `pos`

 Coordinates of the text element



##### `text`

 The text to display



##### `angle`

 The angle in degrees (clockwise from the positive x-axis)



##### `style`

 Which character set to render the text in

- circled: Circled Latin letters

- squared: Squared Latin letters

- math-bold-script: Boldface math font

- random: Randomly choose for each character between the available fonts




#### Source

<details>
<summary>View source</summary>

```python


	def __init__(self, pos:list, text:str, angle:int=45, style:str=None):
		"""
		Create a new text element

		Params:
			pos: Coordinates of the text element
			text: The text to display
			angle: The angle in degrees (clockwise from the positive x-axis)
			style: Which character set to render the text in
				circled: Circled Latin letters
				squared: Squared Latin letters
				math-bold-script: Boldface math font
				random: Randomly choose for each character between the available fonts
		"""
		super(Text, self).__init__(pos)
		self.text = text
		self.l = len(self.text)
		self.angle = angle
		# self.ratio = math.sin(math.radians(self.angle))
		r = math.radians(self.angle)
		self.rx: float = math.cos(r)
		self.ry: float = math.sin(r)
		m = max(self.rx, self.ry)
		f = 1 / m if m else 1
		self.rx *= f
		self.ry *= f

		# The bounding box of the rendered text
		self.box = [round(self.l*abs(self.rx)+1), round(self.l*abs(self.ry)+1)]
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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>render</code></h2></summary> -->
<summary>
render
</summary>
<!-- ### `render` -->
Method

Create a 2D array representing the bounding box of this element


#### Parameters

##### `Params`

{parameter_info}

##### `rich_output`

  Whether to use HTML tags and CSS attributes to style Markdown content (inserted from docs for `Text.render#rich_output`)



##### `capitalization`

 What case the output should appear in

- small: lowercase

- capital: uppercase

- inherit: use the input text's capitalization

- random: randomly decide whether to capitalize each letter


##### `hue`

 The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value



##### `saturation`

 The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)



##### `value`

 Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)





#### Source

<details>
<summary>View source</summary>

```python


	def render(self,
		rich_output:bool=False,
		capitalization:str='inherit',
		hue:int=0,
		saturation:int=50,
		value:int=50,
		**kwargs
	):
		"""
		Create a 2D array representing the bounding box of this element

		Params:
			rich_output: $$
			capitalization: What case the output should appear in
				small: lowercase
				capital: uppercase
				inherit: use the input text's capitalization
				random: randomly decide whether to capitalize each letter
			hue: The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value
			saturation: The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)
			value: Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)
		"""
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


			if rich_output and c:
				if callable(hue):
					h = hue(i, self.l)
				else:
					h = hue

				# hex_color = colorsys.hsv_to_rgb
				tag = 'span'
				colors = map(round, [h, saturation, value])
				c = '<{} style="color: hsl({},{}%,{}%);">{}</ {} >'.format(tag, *colors, c, tag)
			# Set the character in the canvas
			# print(self.rx)
			if xc < self.w and yc < self.h:
				self.canvas[yc][xc] = c
		return self.canvas



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.346919

<details>
<summary>View source</summary>

```python

class Text(Element):
	"""
	Simple text element to add to a diagram
	"""

	text: str
	l: int
	box: list[int]
	w: int
	h: int
	rx: float
	ry: float

	def __init__(self, pos:list, text:str, angle:int=45, style:str=None):
		"""
		Create a new text element

		Params:
			pos: Coordinates of the text element
			text: The text to display
			angle: The angle in degrees (clockwise from the positive x-axis)
			style: Which character set to render the text in
				circled: Circled Latin letters
				squared: Squared Latin letters
				math-bold-script: Boldface math font
				random: Randomly choose for each character between the available fonts
		"""
		super(Text, self).__init__(pos)
		self.text = text
		self.l = len(self.text)
		self.angle = angle
		# self.ratio = math.sin(math.radians(self.angle))
		r = math.radians(self.angle)
		self.rx: float = math.cos(r)
		self.ry: float = math.sin(r)
		m = max(self.rx, self.ry)
		f = 1 / m if m else 1
		self.rx *= f
		self.ry *= f

		# The bounding box of the rendered text
		self.box = [round(self.l*abs(self.rx)+1), round(self.l*abs(self.ry)+1)]
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

	def render(self,
		rich_output:bool=False,
		capitalization:str='inherit',
		hue:int=0,
		saturation:int=50,
		value:int=50,
		**kwargs
	):
		"""
		Create a 2D array representing the bounding box of this element

		Params:
			rich_output: $$
			capitalization: What case the output should appear in
				small: lowercase
				capital: uppercase
				inherit: use the input text's capitalization
				random: randomly decide whether to capitalize each letter
			hue: The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value
			saturation: The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)
			value: Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)
		"""
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


			if rich_output and c:
				if callable(hue):
					h = hue(i, self.l)
				else:
					h = hue

				# hex_color = colorsys.hsv_to_rgb
				tag = 'span'
				colors = map(round, [h, saturation, value])
				c = '<{} style="color: hsl({},{}%,{}%);">{}</ {} >'.format(tag, *colors, c, tag)
			# Set the character in the canvas
			# print(self.rx)
			if xc < self.w and yc < self.h:
				self.canvas[yc][xc] = c
		return self.canvas


```
</details>

</details>

<!-- ## Element -->

<details>
<summary>
Element
</summary>

Class

*module `element`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)


#### Parameters

##### `Params`

{parameter_info}

##### `pos`

 Coordinates of the element in the scene



##### `Attributes`

{parameter_info}

##### `pos`

  Coordinates of the element in the scene (inserted from docs for `Element.__init__#pos`)



##### `x`

 The x coordinate



##### `y`

 The y coordinate



##### `id`

 The UUID of this element






#### Source

<details>
<summary>View source</summary>

```python


	def __init__(self, pos):
		"""
		Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)

		Params:
			pos: Coordinates of the element in the scene

		Attributes:
			pos: $$
			x: The x coordinate
			y: The y coordinate
			id: The UUID of this element
		"""

		# Upper left-hand corner of bounding box (inclusive)
		self.pos = pos if pos else [0, 0]
		self.x, self.y = self.pos
		self.id = uuid.uuid4()



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.358888

<details>
<summary>View source</summary>

```python

class Element:
	"""A generic element to be added to a diagram"""

	def __init__(self, pos):
		"""
		Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)

		Params:
			pos: Coordinates of the element in the scene

		Attributes:
			pos: $$
			x: The x coordinate
			y: The y coordinate
			id: The UUID of this element
		"""

		# Upper left-hand corner of bounding box (inclusive)
		self.pos = pos if pos else [0, 0]
		self.x, self.y = self.pos
		self.id = uuid.uuid4()


```
</details>

</details>

<!-- ## Section -->

<details>
<summary>
Section
</summary>

Class

*module `section`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new section


#### Parameters

##### `Params`

{parameter_info}

##### `type_`

 The type of section



##### `templates`

 A dictionary pairing template names to their contents



##### `parent`

 The parent section



##### `**kwargs`

 Additional arguments and/or data for the section





#### Source

<details>
<summary>View source</summary>

```python


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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>add</code></h2></summary> -->
<summary>
add
</summary>
<!-- ### `add` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def add(self, x):
        self.children.append(x)
        return x



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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>names</code></h2></summary> -->
<summary>
names
</summary>
<!-- ### `names` -->
Method

Not yet documented


#### Parameters



#### Source

<details>
<summary>View source</summary>

```python


    def names(self):
        return [c.type for c in self.children]



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>set</code></h2></summary> -->
<summary>
set
</summary>
<!-- ### `set` -->
Method

Set a property of the section


#### Parameters

##### `Params`

{parameter_info}

##### `a`

 The name of the property



##### `b`

 The value to set the property to





#### Source

<details>
<summary>View source</summary>

```python


    def set(self, a, b):
        """
        Set a property of the section

        Params:
            a: The name of the property
            b: The value to set the property to
        """
        self.kwargs[a] = b



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.363873

<details>
<summary>View source</summary>

```python

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


```
</details>

</details>

<!-- ## Element -->

<details>
<summary>
Element
</summary>

Class

*module `text`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)


#### Parameters

##### `Params`

{parameter_info}

##### `pos`

 Coordinates of the element in the scene



##### `Attributes`

{parameter_info}

##### `pos`

  Coordinates of the element in the scene (inserted from docs for `Element.__init__#pos`)



##### `x`

 The x coordinate



##### `y`

 The y coordinate



##### `id`

 The UUID of this element






#### Source

<details>
<summary>View source</summary>

```python


	def __init__(self, pos):
		"""
		Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)

		Params:
			pos: Coordinates of the element in the scene

		Attributes:
			pos: $$
			x: The x coordinate
			y: The y coordinate
			id: The UUID of this element
		"""

		# Upper left-hand corner of bounding box (inclusive)
		self.pos = pos if pos else [0, 0]
		self.x, self.y = self.pos
		self.id = uuid.uuid4()



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.371852

<details>
<summary>View source</summary>

```python

class Element:
	"""A generic element to be added to a diagram"""

	def __init__(self, pos):
		"""
		Create a new element (note that this is an internal method used to create instances of element subclasses like the Text class)

		Params:
			pos: Coordinates of the element in the scene

		Attributes:
			pos: $$
			x: The x coordinate
			y: The y coordinate
			id: The UUID of this element
		"""

		# Upper left-hand corner of bounding box (inclusive)
		self.pos = pos if pos else [0, 0]
		self.x, self.y = self.pos
		self.id = uuid.uuid4()


```
</details>

</details>

<!-- ## Text -->

<details>
<summary>
Text
</summary>

Class

*module `text`*

Class not yet documented

### Methods


<details>
<!-- <summary><h2><code>__init__</code></h2></summary> -->
<summary>
__init__
</summary>
<!-- ### `__init__` -->
Method

Create a new text element


#### Parameters

##### `Params`

{parameter_info}

##### `pos`

 Coordinates of the text element



##### `text`

 The text to display



##### `angle`

 The angle in degrees (clockwise from the positive x-axis)



##### `style`

 Which character set to render the text in

- circled: Circled Latin letters

- squared: Squared Latin letters

- math-bold-script: Boldface math font

- random: Randomly choose for each character between the available fonts




#### Source

<details>
<summary>View source</summary>

```python


	def __init__(self, pos:list, text:str, angle:int=45, style:str=None):
		"""
		Create a new text element

		Params:
			pos: Coordinates of the text element
			text: The text to display
			angle: The angle in degrees (clockwise from the positive x-axis)
			style: Which character set to render the text in
				circled: Circled Latin letters
				squared: Squared Latin letters
				math-bold-script: Boldface math font
				random: Randomly choose for each character between the available fonts
		"""
		super(Text, self).__init__(pos)
		self.text = text
		self.l = len(self.text)
		self.angle = angle
		# self.ratio = math.sin(math.radians(self.angle))
		r = math.radians(self.angle)
		self.rx: float = math.cos(r)
		self.ry: float = math.sin(r)
		m = max(self.rx, self.ry)
		f = 1 / m if m else 1
		self.rx *= f
		self.ry *= f

		# The bounding box of the rendered text
		self.box = [round(self.l*abs(self.rx)+1), round(self.l*abs(self.ry)+1)]
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



```

</details>

#### References

None available

</details>


<details>
<!-- <summary><h2><code>render</code></h2></summary> -->
<summary>
render
</summary>
<!-- ### `render` -->
Method

Create a 2D array representing the bounding box of this element


#### Parameters

##### `Params`

{parameter_info}

##### `rich_output`

  Whether to use HTML tags and CSS attributes to style Markdown content (inserted from docs for `Text.render#rich_output`)



##### `capitalization`

 What case the output should appear in

- small: lowercase

- capital: uppercase

- inherit: use the input text's capitalization

- random: randomly decide whether to capitalize each letter


##### `hue`

 The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value



##### `saturation`

 The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)



##### `value`

 Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)





#### Source

<details>
<summary>View source</summary>

```python


	def render(self,
		rich_output:bool=False,
		capitalization:str='inherit',
		hue:int=0,
		saturation:int=50,
		value:int=50,
		**kwargs
	):
		"""
		Create a 2D array representing the bounding box of this element

		Params:
			rich_output: $$
			capitalization: What case the output should appear in
				small: lowercase
				capital: uppercase
				inherit: use the input text's capitalization
				random: randomly decide whether to capitalize each letter
			hue: The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value
			saturation: The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)
			value: Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)
		"""
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


			if rich_output and c:
				if callable(hue):
					h = hue(i, self.l)
				else:
					h = hue

				# hex_color = colorsys.hsv_to_rgb
				tag = 'span'
				colors = map(round, [h, saturation, value])
				c = '<{} style="color: hsl({},{}%,{}%);">{}</ {} >'.format(tag, *colors, c, tag)
			# Set the character in the canvas
			# print(self.rx)
			if xc < self.w and yc < self.h:
				self.canvas[yc][xc] = c
		return self.canvas



```

</details>

#### References

None available

</details>


Docs built at 2021-06-16 05:12:41.377836

<details>
<summary>View source</summary>

```python

class Text(Element):
	"""
	Simple text element to add to a diagram
	"""

	text: str
	l: int
	box: list[int]
	w: int
	h: int
	rx: float
	ry: float

	def __init__(self, pos:list, text:str, angle:int=45, style:str=None):
		"""
		Create a new text element

		Params:
			pos: Coordinates of the text element
			text: The text to display
			angle: The angle in degrees (clockwise from the positive x-axis)
			style: Which character set to render the text in
				circled: Circled Latin letters
				squared: Squared Latin letters
				math-bold-script: Boldface math font
				random: Randomly choose for each character between the available fonts
		"""
		super(Text, self).__init__(pos)
		self.text = text
		self.l = len(self.text)
		self.angle = angle
		# self.ratio = math.sin(math.radians(self.angle))
		r = math.radians(self.angle)
		self.rx: float = math.cos(r)
		self.ry: float = math.sin(r)
		m = max(self.rx, self.ry)
		f = 1 / m if m else 1
		self.rx *= f
		self.ry *= f

		# The bounding box of the rendered text
		self.box = [round(self.l*abs(self.rx)+1), round(self.l*abs(self.ry)+1)]
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

	def render(self,
		rich_output:bool=False,
		capitalization:str='inherit',
		hue:int=0,
		saturation:int=50,
		value:int=50,
		**kwargs
	):
		"""
		Create a 2D array representing the bounding box of this element

		Params:
			rich_output: $$
			capitalization: What case the output should appear in
				small: lowercase
				capital: uppercase
				inherit: use the input text's capitalization
				random: randomly decide whether to capitalize each letter
			hue: The hue component of the color; either an integer in the range `[0, 360]` or a function that takes the current character index and total length of the text and returns an appropriate value
			saturation: The same as the hue, but representing the saturation of the font color - a value from 0 to 100 (i.e., a percentage)
			value: Essentially identical to saturation except controlling brightness instead (0 will give black and 100 will give white)
		"""
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


			if rich_output and c:
				if callable(hue):
					h = hue(i, self.l)
				else:
					h = hue

				# hex_color = colorsys.hsv_to_rgb
				tag = 'span'
				colors = map(round, [h, saturation, value])
				c = '<{} style="color: hsl({},{}%,{}%);">{}</ {} >'.format(tag, *colors, c, tag)
			# Set the character in the canvas
			# print(self.rx)
			if xc < self.w and yc < self.h:
				self.canvas[yc][xc] = c
		return self.canvas


```
</details>

</details>


Docs built at 2021-06-16 05:12:41.095591
