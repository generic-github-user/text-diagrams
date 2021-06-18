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