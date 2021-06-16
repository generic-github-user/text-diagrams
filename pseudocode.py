import ast

from python_ops import op_strings, symbols

# class node_strings:
#     For:

reversed = ['In', 'NotIn']

functions = {
    'range': ('the range {} to {}', (0, None)),
    'print': ('Print {}', (''))
}

node_strings = {
    'Compare': ('({} {} {})', 'left', 'ops', 'comparators'),
    'For': ('For {} in {}:', 'target', 'iter'),
    'Name': ('{}', 'id'),
    'Assign': ('Set {} to {}', 'targets', 'value'),
    'Constant': ('{}', 'value'),
    'FunctionDef': ('Initialize function {}({})', 'name', 'args'),
    'arguments': ('{}', 'args'),
    'arg': ('{}', 'arg'),
    'Return': ('Return {}', 'value'),
    'If': ('If {} then:', 'test'),
    'Expr': ('{}', 'value'),
    'Break': ('End loop',),
    'Dict': ('{{{}, {}}}', 'keys', 'values'),
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
