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


Docs built at 2021-06-16 05:07:07.692445

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
