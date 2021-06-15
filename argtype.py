class ArgType:
    """
    Defines a 'type' that can be used for validating and/or converting function arguments, generating examples, type hinting, etc. It is intended to emulate some of the features of Python's `typing` module, albeit with a more general scope.
    """

    def __init__(self, primitive, *conditions):
        self.primitive = primitive
        self.conditions = conditions

class ArgRange:
    """ArgRange"""

    def __init__(self, *args):
        # super(ArgRange, self).__init__()
        self.range = range(*args)


test = ArgType(int, ArgRange(1, 10, 2))
