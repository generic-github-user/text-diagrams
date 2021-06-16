import ast
import unicodedata

from python_ops import op_strings, symbols

# class node_strings:
#     For:

reversed = ['In', 'NotIn']

def lookup(name):
    try:
        return unicodedata.lookup(name)
    except:
        return None

unicode_chars = ['sum', 'lambda']

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

def stringify_node(node):
    node_data = []

    node_type = type(node).__name__
    if node_type in node_strings:
        template = node_strings[node_type]
    else:
        template = [node_type]

    if node_type in op_strings:
        return op_strings[node_type]
    elif node_type in symbols:
        return symbols[node_type]
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
