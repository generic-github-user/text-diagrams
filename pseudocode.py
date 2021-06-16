import ast

# class node_strings:
#     For:

op_strings = {
    'Add': 'Increment',
    'Sub': 'Decrement',
    'In': 'contains',
    'NotIn': 'does not contain',
    'Eq': 'is equal',
    'NotEq': 'is equal',
    'Lt': 'is less than',
    'LtE': 'is less than or equal to',
    'Gt': 'is greater than',
    'GtE': 'is greater than or equal to',
}
reversed = ['In', 'NotIn']

symbols = {
    'Add': '+',
    'Mult': '*',
    'FloorDiv': '//',
    'Div': '/',
    'Pow': '^',
    'Sub': '-',
    'Mod': '%',
    'Eq': '=',
    'NotEq': '!=',
    'Lt': '<',
    'LtE': '<=',
    'Gt': '>',
    'GtE': '>=',
    'LShift': '<<',
    'RShift': '>>',
}

functions = {
    'range': ('the range {} to {}', (0, None)),
    'print': ('Print {}', (''))
}

node_strings = {
    'For': ('For {} in {}:', 'target', 'iter'),
    'Name': ('{}', 'id'),
    'Assign': ('Set {} to {}', 'targets', 'value'),
    'Constant': ('{}', 'value'),
    'Expr': ('({})', 'value'),
    'Call': ('{}({})', 'func', 'args'),
    'AugAssign': ('{} {} by {}', 'op', 'target', 'value'),
    'BinOp': ('({} {} {})', 'left', 'op', 'right'),
}
sample = """
a = 5
for i in range(8):
    for j in range(6):
        a += (i * j) // 2
    a -= a % 4
    print(a)
"""

print(ast.parse(sample).body)
print(Pseudocode(sample))
