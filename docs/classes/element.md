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


Docs built at 2021-06-16 05:07:07.752458

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
