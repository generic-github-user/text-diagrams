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
    # 'Dict': ('Dictionary with {{{}, {}}}',),
    'Dict': ('Dictionary with values:',),
    'Call': ('_{}({})_', 'func', 'args'),
    'AugAssign': ('{} {} by {}', 'op', 'target', 'value'),
    'BinOp': ('({} {} {})', 'left', 'op', 'right'),
    'Lambda': ('Lambda ({}) → {}', 'args', 'body'),
    'UnaryOp': ('{} {}', 'op', 'operand'),
}

def func_factory(F, *args, **kwargs):
    def generated_func(*args, **kwargs):
        # print(args, kwargs)
        return F(*args, **kwargs)
    return generated_func

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

def stringify_node(
    node,
    formatting='markdown',
    identifiers='symbols',
    short_mul=True,
    level=0,
    indent='    ',
    *args,
    **kwargs
):
    """
    Convert an abstract syntax tree node to a string

    Params:
        node: The node to convert
        formatting: The markup style to use when generating the result
            'markdown': Markdown
        identifiers: The default encoding style for function and operator identifiers such as `sum`, `product`, and `abs`
            'symbols': Use a Unicode symbol in place of the full name if available
            'strings': Use the default name strings
    """

    nested_stringify = func_factory(stringify_node, level=level, indent=indent, *args, **kwargs)

    node_data = []
    if short_mul:
        symbols['Mult'] = ''

    # Determine the type of node (excluding the `ast.` prefix)
    node_type = type(node).__name__

    # This is just for logging/debugging
    # try:
    #     pass
        # print(node, node_type)
        # print(node, node_type, node.args, stringify_node(node.args))
    # except:
    #     pass

    # Find the template string if one is available
    if node_type in node_strings:
        template = node_strings[node_type]
    # If not available, use the plain type name
    else:
        template = [node_type]

    # Handle the conversion of specific function names to corresponding symbols
    if node_type in ['Call', 'Lambda']:
        # func_name = stringify_node(nd.func)
        func_name = node.func.id if node_type == 'Call' else 'Lambda'
        # node_args = nd.args if node_type == 'Call' else [a for a in nd.args.args]
        node_args = node.args if node_type == 'Call' else node.args.args
        if func_name in functions:
            func_info = list(functions[func_name])
            # p = [value.args[i] for i in range(len(func_info)) if ]
            # node_args = nd.args

            if func_name in unicode_chars and identifiers == 'symbols':
                char_name = unicode_chars[func_name]
                if not char_name:
                    char_name = func_name
                char = lookup(char_name) if len(char_name) > 1 else char_name
                func_info[0] = func_info[0].lower().replace(func_name.lower(), char)
                # print(len(node_args))
                # print(char)
                # print(func_name, char, func_info)

            clone = [a for a in func_info[1]]
            clone[-len(node_args):] = [nested_stringify(v) for v in node_args]

            result = func_info[0].format(*clone)
            return result

    elif node_type == 'arguments':
        # return ', '.join(stringify_node(a) for a in node.args)
        return nested_stringify(node.args)

    # If the template has any attributes to be filled in, generate the strings for these first
    # e.g., a `for` loop's `target` and `iter` properties
    # Note that this does not handle iterable properties such as function argument objects
    if len(template) > 1:
        temp = template[1:]
        # if node_type in reversed:
        if node_type == 'Compare':
            # print(type(node.ops)[0].__name__)
            if type(node.ops[0]).__name__ in reversed:
                temp = temp[::-1]

        # Loop through the attributes in the template and get the corresponding strings
        for attr in temp:
            # Get the node's attribute
            value = getattr(node, attr)
            value_type = type(value).__name__



            value_type = type(value).__name__
            if value_type in node_strings:
                value = nested_stringify(value)
                # print(value_type, value)
            else:
                value = nested_stringify(value)

            # print(super(type(value)))
            # if super(type(value)) is ast.BinOp:
            # if isinstance(value, ast.BinOp):

                # node_data.extend(value)
                # value = ' '.join(map(str, value))
                # value = value[0]
            # else:
            if value_type == 'Callable':
                value = nested_stringify(value)

            node_data.append(value)

        # Load the data into the template string
        node_string = template[0].format(*node_data)

    else:
        if type(node) in [list, tuple]:
            # value = parse_node(value)
            node_string = [nested_stringify(v) for v in node]
            node_string = ', '.join(node_string)
        # if node_type in []
        elif not isinstance(node, ast.AST):
            node_string = node
        elif type(node) is ast.Dict:
            node_string = node_strings['Dict'][0] + '  \\\n'
            # print(node_string, level, list(map(stringify_node, list(zip(node.keys, node.values))[0])))
            # breakpoint()
            dict_vals = zip(node.keys, node.values)
            ind = indent * (level+2)
            print(len(ind))
            node_string += ('  \\\n').join(
                ['' + ind + ': '.join(map(nested_stringify, x)) for x in dict_vals]
            )
        elif node_type in op_strings:
            node_string = op_strings[node_type]
        elif node_type in symbols:
            node_string = symbols[node_type]
        else:
            node_string = node_type

    node_string = str(node_string)
    # node_string = node_string.replace('    ', '&nbsp;'*4)
    return node_string


def parse_node(
    node,
    level=0,
    indent='    ',
    formatting='markdown'
):
    result = []

    # node_data = [parse_node(getattr(node, attr)) for attr in template[1:]]

    next_node = stringify_node(node, level=level+1, indent=indent, formatting=formatting)
    result.append((indent * level) + next_node)
    # print(True, level, next_node)

    if hasattr(node, 'body'):
        for x in node.body:
            result.append(parse_node(x, level=level+1, formatting=formatting))

    # result.append('End')
    if type(result) is list:
        # h = '>' if level == 0 else ''
        h = ''
        result = '  \\\n'.join([h+r for r in result])

    # Fix spacing so that the leading whitespace/indentation is not removed by the browser
    return result.replace('    ', '&nbsp;'*4)
    return result

def Pseudocode(source,
    output_path='./generated-pseudocode.md',
    formatting='markdown',
    **kwargs
):
    # TODO: Add a class

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
g = {
    'x': 36,
    'y': 49
}

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
