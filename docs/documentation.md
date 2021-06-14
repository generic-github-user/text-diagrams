Docs version 254

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





### `clean_tabs`

Method

Remove leading tabs from a string

#### Parameters

##### `Params`

{parameter_info}

##### `text`

 The input string





### `extract_info`

Method

Parse a docstring and return a dictionary of its structured data

#### Parameters



### `generate`

Method

Not yet documented

#### Parameters



### `import_modules`

Method

Import each of the modules to be documented

#### Parameters



### `indent_width`

Method

Count the number of leading tabs in a string (e.g., a line of code)

#### Parameters

##### `Params`

{parameter_info}

##### `string`

 The input string





### `isnum`

Method

Check if a given character is numeric

#### Parameters



### `parent`

Method

Not yet documented

#### Parameters



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






### `write`

Method

Not yet documented

#### Parameters




Docs built at 2021-06-14 19:21:53.848431

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





### `add`

Method

Not yet documented

#### Parameters



### `generate`

Method

Not yet documented

#### Parameters



### `names`

Method

Not yet documented

#### Parameters



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






Docs built at 2021-06-14 19:21:53.852420

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







### `add`

Method

Add an element to this diagram

#### Parameters



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








### `write`

Method

Create a new file and insert UTF-8-encoded text data or update an existing file

#### Parameters




Docs built at 2021-06-14 19:21:53.856409

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







Docs built at 2021-06-14 19:21:53.872367

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





### `__str__`

Method

Generate a string representation of this point

#### Parameters



### `move`

Method

Translate the point

#### Parameters

##### `Params`

{parameter_info}

##### `delta`

 A list of offsets to move the point along each axis in space by





### `print`

Method

Not yet documented

#### Parameters



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






Docs built at 2021-06-14 19:21:53.876356

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






Docs built at 2021-06-14 19:21:53.885333


Docs built at 2021-06-14 19:21:53.848431
