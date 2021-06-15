class ArgType:
    """
    Defines a 'type' that can be used for validating and/or converting function arguments, generating examples, etc. It is intended to emulate some of the features of Python's `typing` module, albeit with a more general scope.
    """

    def __init__(self, arg):
        self.arg = arg
