import uuid

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
