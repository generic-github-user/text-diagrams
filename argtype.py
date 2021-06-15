class ArgType:
    """
    Defines a 'type' that can be used for validating and/or converting function arguments, generating examples, type hinting, etc. It is intended to emulate some of the features of Python's `typing` module, albeit with a more general scope.
    """

    def __init__(self, primitive, **conditions):
        self.primitive = primitive
        self.conditions = conditions
