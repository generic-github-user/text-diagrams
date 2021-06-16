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

unicode_chars = {
    'sum': 'greek capital letter sigma',
    'Lambda': 'greek small letter lamda',
    'Lt': '<',
    'LtE': '≤',
    'Gt': '>',
    'GtE': '≥',
}

functions = {
    'range': ('the range {} to {}', (0, None)),
    'print': ('Print {}', ('',)),
    'sum': ('Sum ({})', ('',)),
    'Lambda': ('Lambda ({}) → {}', ('args', 'body')),
    'abs': ('|{}|', ('',)),
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
    '#e5e7e9': ['Gt', 'GtE'],
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
    'Constant': ('**.*{}*.**', 'value'),
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
    'Lambda': ('Lambda ({}) → {}', 'args', 'body'),
    'UnaryOp': ('{} {}', 'op', 'operand'),
}

def convert_markup(d):
    for k, v in d.items():
        if v in [tuple]:
            v = list(v)
        opening = True
        tags = [('**', 'b'), ('*', 'i'), ('_', 'u'), ('$', 'span')]
        f = type(v) in [list, tuple]
        if f:
            v = v[0]
        for c, t in tags:
            while c in v:
                s = '' if opening else '/'
                col = {a: b for a, b in colors.items() if k in b}
                col = ' color: {}'.format(list(col)[0]) if col else ''
                # style = f' style="font-style: italic;{col}"' if opening else ''
                style = f' style="{col}"' if opening else ''
                # v[0] = v[0].replace(c, f'<{s}span{style}>', 1)
                if type(v) in [list]:
                    v = v.replace(c, f'<{s}{t}{style}>', 1)
                else:
                    v = v.replace(c, f'<{s}{t}{style}>', 1)
                opening = not opening
            v = v.replace('.', '')
        if f:
            v_ = list(d[k])
            v_[0] = v
            d[k] = v_
        else:
            d[k] = v

convert_markup(node_strings)
convert_markup(op_strings)
# convert_markup(symbols)
print(node_strings)
print(op_strings)

def stringify_node(node, formatting='markdown'):
    """
    Convert an abstract syntax tree node to a string

    Params:
        node: The node to convert
        formatting: The markup style to use when generating the result
            'markdown': Markdown
    """
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

    try:
        print(node, node_type, node.args, stringify_node(node.args))
    except:
        pass

    # nd = node_data[0]
    nd = node
    if node_type in ['Call', 'Lambda']:
        # func_name = stringify_node(nd.func)
        func_name = nd.func.id if node_type == 'Call' else 'Lambda'
        # node_args = nd.args if node_type == 'Call' else [a for a in nd.args.args]
        node_args = nd.args if node_type == 'Call' else nd.args.args
        if func_name in functions:
            func_info = list(functions[func_name])
            # p = [value.args[i] for i in range(len(func_info)) if ]
            # node_args = nd.args

            if func_name in unicode_chars:
                char_name = unicode_chars[func_name]
                if not char_name:
                    char_name = func_name
                char = lookup(char_name) if len(char_name) > 1 else char_name
                func_info[0] = func_info[0].lower().replace(func_name.lower(), char)
                # print(len(node_args))
                # print(char)
                # print(func_name, char, func_info)

            clone = [a for a in func_info[1]]
            clone[-len(node_args):] = [stringify_node(v) for v in node_args]

            result = func_info[0].format(*clone)
            return result

    elif node_type == 'arguments':
        # return ', '.join(stringify_node(a) for a in node.args)
        return stringify_node(node.args)

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
            if value_type == 'Callable':
                value = stringify_node(value)

            node_data.append(value)

        # try:
        #     print(node_data)
        # except:
        #     pass

        # print(node_data)
    return template[0].format(*node_data)



def parse_node(node, level=0, indent='    ', formatting='markdown'):
    result = []

    # node_data = [parse_node(getattr(node, attr)) for attr in template[1:]]

    result.append((indent * level) + stringify_node(node))

    if hasattr(node, 'body'):
        for x in node.body:
            result.append(parse_node(x, level=level+1, formatting=formatting))

    # result.append('End')
    if type(result) is list:
        h = '>' if level == 0 else ''
        result = '  \\\n'.join([h+r for r in result])

    return result.replace('    ', '&nbsp;'*4)
    return result

def Pseudocode(source, output_path='./generated-pseudocode.md', formatting='markdown', **kwargs):
    code = parse_node(ast.parse(source), formatting=formatting, **kwargs) + '\n End'
    # if formatting == 'markdown':
        # code = '>>>' + code
        # code = '```\n{}\n```'.format(code)
        # .replace('<', '&lt;').replace('>', '&rt;')
        # code = '<pre><code>{}</code></pre>'.format(code)
        # code = '~~~\n{}\n~~~'.format(code)

    # return '\n'.join(code)
    with open(output_path, 'w', encoding='UTF-8') as output_file:
        output_file.write(code)
    return code

sample = """
a = 5
def z(n, m):
    return n ** m / 4

for i in range(8):
    for j in range(6):
        a += (i * j) // 2
        a += z(i, j)
        if a >= 10000:
            break
    if a % 567 == 0:
        print(a + '!')
    a -= a % 4
    print(a)

if 5 in a:
    print(a*99)

q = sum(range(20))
w = lambda u, t: u ** 9
print(abs(-50))
# print(floor())
# print(abs())
print(q)
"""

print(ast.parse(sample).body)
print(Pseudocode(sample))
