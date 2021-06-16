import uuid
import math
import unicodedata
import random
import colorsys
import numpy as np
import typing

from geometry.point import Point
from element import Element

shading = '░█'


def get_char(name):
	try:
		return unicodedata.lookup(name)
	except:
		return None

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

print(typing.get_type_hints(Text))
print(typing.get_type_hints(Text.__init__))
print(typing.get_type_hints(Text.render))
print(typing.get_type_hints(Diagram.render))
# print(Text([5, 5], 't').__annotations__['rx'])


TestDiagram = Diagram(background='X', origin='center', direction=(lambda x, y: [x**2, y**2]), hue=(lambda x, y: x*y))
TestDiagram.render(rich_output=True, path='./generated', extensions=['md', 'html'])
# TestDiagram.add(Text([10, 10], 'Hello World', style='math-bold-script')).render(rich_output=True, path='./generated', extensions=['md', 'html'], hue=(lambda x, y: x/y*360))
