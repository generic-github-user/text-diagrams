import ast

# class node_strings:
#     For:

op_strings = {
    'Add': 'Increment',
    'Sub': 'Decrement'
}
node_strings = {
    'For': ('For {} in {}:', 'target', 'iter'),
    'Name': ('{}', 'id'),
    'Assign': ('Set {} to {}', 'targets', 'value'),
    'Constant': ('{}', 'value')
}
