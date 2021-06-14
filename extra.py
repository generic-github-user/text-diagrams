def parse_tags(tag_list):
    result = '**'
    for i, t in enumerate(tag_list):
        if i < len(tag_list) - 1:
            next = tag_list[i+1]
        else:
            next = None

        if t in data_types:
            result += '`{}`'.format(t)
            if type(next) is list:
                if t in ['str']:
                    result += ' in `{}`'.format(', '.join(next))
                    tag_list.remove(next)
                elif t in ['func']:
                    result += ' (`{}` -> `{}`)'.format(*next)
                    tag_list.remove(next)
        elif '-' in str(t):
            limits = t.split('-')
            result += ' between `{}` and `{}`'.format(*limits)
        elif type(t) is not list and t in symbols:
            # elif any(s in t for s in symbols):
            result += ' {} {}'.format(symbols[t], next)
        elif type(t) is list and t[0] in data_types:
            if type(t[1]) in [int, float, str]:
                t[1] = [t[1]]
            result += '`{}` array of shape `{}`'.format(*t)
    result += '**'
    return result
