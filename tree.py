import os
import sys


def tree(top='.'):
    components = os.listdir(top)
    components_num = len(components)
    for i, component in enumerate(components, start=1):
        component_path = os.path.join(top, component)

        if i == components_num:
            prefix = ('└─', '   ')
        else:
            prefix = ('├─', '│  ')

        yield f'{prefix[0]}{component}'
        if os.path.isdir(component_path):
            for line in tree(component_path):
                yield f'{prefix[1]}{line}'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '.'

    for line in tree(path):
        print(line)
