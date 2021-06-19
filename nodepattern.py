class NodePattern:
    def __init__(self, replacement=None, info=None, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.args = args
        self.kwargs = kwargs

        self.replacement = replacement
        self.info = info

    def tostring(self, node):
        return self.replacement.format(*self.info(node))

    def get(self, q, w):
        if hasattr(q, w):
            return getattr(q, w)
        else:
            return None

    def match(self, node):
        print(self.get(node, 'ops'))
        return all((v(self.get(node, k)) if callable(v) else self.get(node, k) == v) for k, v in self.kwargs.items())
