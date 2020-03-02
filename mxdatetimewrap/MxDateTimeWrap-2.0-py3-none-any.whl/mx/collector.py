import os
import sys
import glob
import fileinput
import re
# from StringIO import StringIO

reg = re.compile(r'([A-Za-z]*DateTime[A-Za-z]*\([^\)]*\))')
search = reg.search


def main(*paths):
    if not paths:
        return exit('No paths defined...')
    for path in paths:
        if not os.path.isdir(path):
            return exit('"%s" is not a directory')
    rulenames = []
    for path in paths:
        rulenames += glob.glob(
            os.path.join(path, '*.timon.is', 'reglur_*', 'regla_*.py')
        )
    if not rulenames:
        return exit('No rules found under the defined paths')
    lines = set()
    for line in fileinput.input(rulenames):
        if 'DateTime' in line:
            line = line.lstrip()
            if not line.startswith('#') and not 'import' in line:
                # buf = ''
                # depth = 0
                # for let in line:
                #     buf += let
                #     if let == '(':
                #         depth += 1
                #     elif let in ',+= ':
                #         if not 'DateTime' in buf:
                #             buf = ''
                #     elif let == ')':
                #         depth = max((depth - 1, 0))
                #         if not depth and 'DateTime' in buf:
                #             lines.add(buf)
                # if 'DateTimeDeltaFrom' in line:
                #     import pdb; pdb.set_trace()
                res = search(line)
                res = res and res.groups() or []
                for o in res:
                    if 'DateTimeDeltaFrom(int(4.00*60*60)' in o:
                        import pdb; pdb.set_trace()
                    lines.add(o)
    with open('rulelines.out', 'w') as f:
        for line in sorted(lines):
            f.write(line)
            f.write('\n')


def exit(s):
    print(s)
    return 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
