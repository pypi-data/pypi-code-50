class Imports:

    def __init__(self):
        self._imports = {}

    def add(self, namespace, classname):
        if namespace not in self._imports:
            self._imports[namespace] = set()

        self._imports[namespace].add(classname)

    def to_code(self) -> str:
        lines = []
        namespaces = sorted(self._imports.keys())
        for namespace in namespaces:
            class_names = sorted(self._imports[namespace])
            lines.append('from {0} import {1}'.format(
                namespace,
                ', '.join([
                    classname for classname in class_names
                ])
            ))

        return '\n'.join(lines)+'\n\n'
