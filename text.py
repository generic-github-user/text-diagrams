from element import Element

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
