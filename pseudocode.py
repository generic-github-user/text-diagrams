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

# Syntax colors via https://htmlcolorcodes.com/color-names/
colors = {
    '#800000': [],
    '#191970': [],
    '#1E90FF': [],
    '#6495ED': [],
    '#556B2F': [],
    '#32CD32': [],
}

colors = {
    '#e5e7e9': [],
    '#abebc6': ['Name', 'Call'],
    '#fadbd8': ['If', 'Break', 'For'],
    '#d2b4de': ['Add', 'Sub', 'Div'],
    '#f9e79f': ['Assign'],
    '#eafaf1': ['Constant'],
}

node_strings = {
    'Compare': ('({} {} {})', 'left', 'ops', 'comparators'),
    'For': ('**For** {} in {}:', 'target', 'iter'),
    'Name': ('*{}*', 'id'),
    'Assign': ('**Set** {} **to** {}', 'targets', 'value'),
    'Constant': ('*{}*', 'value'),
    'FunctionDef': ('**Initialize** function _{}({})_', 'name', 'args'),
    'arguments': ('{}', 'args'),
    'arg': ('{}', 'arg'),
    'Return': ('**Return** {}', 'value'),
    'If': ('**If** {} then:', 'test'),
    'Expr': ('{}', 'value'),
    'Break': ('**End loop**',),
    'Dict': ('{{{}, {}}}', 'keys', 'values'),
    'Call': ('_{}({})_', 'func', 'args'),
    'AugAssign': ('{} {} by {}', 'op', 'target', 'value'),
    'BinOp': ('({} {} {})', 'left', 'op', 'right'),
}

def convert_markup(d):
    for k, v in d.items():
        if v in [tuple]:
            v = list(v)
        opening = True
        tags = [('**', 'b'), ('*', 'i'), ('_', 'u')]
        f = type(v) in [list, tuple]
        if f:
            v = v[0]
        for c, t in tags:
            while c in v:
                s = '' if opening else '/'
                style = ' style="font-style: italic;"' if opening else ''
                # v[0] = v[0].replace(c, f'<{s}span{style}>', 1)
                if type(v) in [list]:
                    v = v.replace(c, f'<{s}{t}>', 1)
                else:
                    v = v.replace(c, f'<{s}{t}>', 1)
                opening = not opening
        if f:
            v_ = list(d[k])
            v_[0] = v
            d[k] = v_
        else:
            d[k] = v

convert_markup(node_strings)
convert_markup(op_strings)
print(node_strings)
print(op_strings)

def stringify_node(node, formatting='markdown'):
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

    if len(template) > 1:
        temp = template[1:]
        # if node_type in reversed:
        if node_type == 'Compare':
            # print(type(node.ops)[0].__name__)
            if type(node.ops[0]).__name__ in reversed:
                temp = temp[::-1]

        for attr in temp:
            value = getattr(node, attr)
            value_type = type(value).__name__

            if value_type == 'Call':
                func_name = stringify_node(value.func)
                if func_name in functions:
                    func_info = functions[func_name]
                    clone = [a for a in func_info[1]]
                    clone[-len(value.args):] = [stringify_node(v) for v in value.args]
                    # p = [value.args[i] for i in range(len(func_info)) if ]
                    value = func_info[0].format(*clone)

            if type(value) in [list, tuple]:
                # value = parse_node(value)
                value = [stringify_node(v) for v in value]
                value = ', '.join(value)

            value_type = type(value).__name__
            if value_type in node_strings:
                value = stringify_node(value)
                # print(value_type, value)
            elif value_type in op_strings:
                value = op_strings[value_type]
            elif value_type in symbols:
                # value = ast.unparse(value)
                value = symbols[value_type]


            # print(super(type(value)))
            # if super(type(value)) is ast.BinOp:
            # if isinstance(value, ast.BinOp):

                # node_data.extend(value)
                # value = ' '.join(map(str, value))
                # value = value[0]
            # else:
            node_data.append(value)

        # try:
        #     print(node_data)
        # except:
        #     pass

        # print(node_data)
    return template[0].format(*node_data)



def parse_node(node, level=0, indent='  '):
    result = []

    # node_data = [parse_node(getattr(node, attr)) for attr in template[1:]]

    result.append((indent * level) + stringify_node(node))

    if hasattr(node, 'body'):
        for x in node.body:
            result.append(parse_node(x, level=level+1))

    # result.append('End')
    if type(result) is list:
        result = '\n'.join(result)
    return result

def Pseudocode(source, output_path='./generated-pseudocode.md'):
    code = parse_node(ast.parse(source)) + '\n End'
    # return '\n'.join(code)
    with open(output_path, 'w', encoding='UTF-8') as output_file:
        output_file.write(code)
    return code

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
