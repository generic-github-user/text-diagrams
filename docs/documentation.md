Docs version 12

# Main

Module not yet documented

## Documentation

Class

*module `build-docs`*

Class not yet documented

### Methods

### `__init__`

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


```
</details>

### `clean_tabs`

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

### `extract_info`

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

### `generate`

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
                    source_code = '\n'+getsource(method)+'\n'
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
                            new_section = Section(
                                content=l.split(':'),
                                type_=section_type,
                                # parent=self.current[section_type],
                                templates=self.template_content,
                                params='children',
                                parameter=l.split(':')[0],
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

### `import_modules`

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

### `indent_width`

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

### `isnum`

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

### `parent`

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

### `split_numeric`

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

### `write`

Method

Not yet documented

#### Parameters



#### Source

<details>
<summary>View source</summary>

```python

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


```
</details>


Docs built at 2021-06-14 20:09:41.371427

<details>
<summary>View source</summary>

```python

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
                    source_code = '\n'+getsource(method)+'\n'
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
                            new_section = Section(
                                content=l.split(':'),
                                type_=section_type,
                                # parent=self.current[section_type],
                                templates=self.template_content,
                                params='children',
                                parameter=l.split(':')[0],
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


```
</details>

## Section

Class

*module `build-docs`*

Class not yet documented

### Methods

### `__init__`

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

### `add`

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

### `generate`

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

### `names`

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

### `set`

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


Docs built at 2021-06-14 20:09:41.386388

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

## Diagram

Class

*module `diagrams`*

Class not yet documented

### Methods

### `__init__`

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

### `add`

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

### `render`

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

### `write`

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


Docs built at 2021-06-14 20:09:41.396383

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

## Element

Class

*module `diagrams`*

Class not yet documented

### Methods

### `__init__`

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

 #



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
			pos: #
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


Docs built at 2021-06-14 20:09:41.425285

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
			pos: #
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

## Point

Class

*module `diagrams`*

Class not yet documented

### Methods

### `__call__`

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

### `__init__`

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

### `__str__`

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

### `move`

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

### `print`

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

### `rotate`

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


Docs built at 2021-06-14 20:09:41.456201

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

## Text

Class

*module `diagrams`*

Class not yet documented

### Methods

### `__init__`

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

### `render`

Method

Create a 2D array representing the bounding box of this element

#### Parameters

##### `Params`

{parameter_info}

##### `rich_output`

 #



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
			rich_output: #
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


Docs built at 2021-06-14 20:09:41.468169

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
			rich_output: #
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

## Section

Class

*module `section`*

Class not yet documented

### Methods

### `__init__`

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

### `add`

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

### `generate`

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

### `names`

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

### `set`

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


Docs built at 2021-06-14 20:09:41.483130

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


Docs built at 2021-06-14 20:09:41.361454
