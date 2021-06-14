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


for l in []:
    t = self.indent_width(l)
    print(t, l)
    if t == 0:
        # Detect section tag
        if l and l[0] == '@':
            section = l[1:]
        # New tag format (e.g., 'Params: ...')
        elif l[:-1] in self.headers:
            section = l[:-1]

        if section not in info:
            info[section] = {}
        if section == 'text':
            if 'val' not in info['text']:
                info['text']['val'] = []
            info[section]['val'].append(l)
    elif t in [1, 4]:
        subsection = self.clean_tabs(l)
        if subsection not in info[section]:
            info[section][subsection] = []
    elif t in [2, 8]:
        parts = self.clean_tabs(l).split(': ')
        print(parts)
        if len(parts) >= 2:
            label = parts[1]
            type_info = parts[0][1:-1].replace(' ','').split(',')
            arg_info = {
                'type': type_info,
                'label': label
            }
            info[section][subsection].append(arg_info)
