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

class ArgRange:
    """ArgRange"""

    def __init__(self, *args):
        # super(ArgRange, self).__init__()
        self.range = range(*args)
        self.info = 'between {} and {}'
        self.args = args

    def text(self):
        return self.info.format(*self.args)

test = ArgType(int, ArgRange(1, 10))
print(test.text())
