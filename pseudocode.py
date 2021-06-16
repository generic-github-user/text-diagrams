import ast

# class node_strings:
#     For:

node_strings = {
    'For': ('For {} in {}:', 'target', 'iter'),
    'Name': ('{}', 'id'),
    'Assign': ('Set {} to {}', 'targets', 'value'),
    'Constant': ('{}', 'value')
}
