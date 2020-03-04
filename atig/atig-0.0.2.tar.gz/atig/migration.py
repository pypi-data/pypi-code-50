import os


class Migration():
    def __init__(self, path):
        self.path = path
        self.name = path.split('/')[-1]
        self.hash = self.name.split('_')[0]
        self.desc = ' '.join(self.name.split('_')[1:]).replace('.py', '')
        self.is_head = False
        self.prev = None
        self.date = None
        fle = open(path, 'r+')
        self.contents = fle.read()
        for curr in self.contents.split('\n'):
            if 'down_revision' in curr[:15]:
                self.prev = curr.split('revision = ')[-1].replace('\'', '')
            if 'Create Date' in curr:
                self.date = curr.split(': ')[-1].split('.')[0]

    def stringify(self):
        return f'{self.hash} - {self.desc}'


class MigrationCollection():
    def __init__(self, migrations):
        # take in a list of migrations, build a hashmap
        self.migrations = {m.hash: m for m in migrations}
        self.history = {m.prev: m.hash for m in migrations}
        self.initial = list(filter(lambda x: 'None' in x.prev, migrations))[0]
        self.current = os.popen('alembic current').read().split(
            '\n')[-2].split(' ')[0]
        self.heads = [
            head.split(' ')[0]
            for head in os.popen('alembic heads').read().split('\n')
            if head != ''
        ]
        for head in self.heads:
            curr = self.migrations[head]
            curr.is_head = True
        # make list of migrations

    def list_migrations(self):
        # start with initial, loop over others
        curr = self.initial
        stack = []
        while curr is not None:
            stack.append(curr)
            next_hash = self.history.get(curr.hash)
            curr = self.migrations.get(next_hash)
        while len(stack) > 0:
            yield stack.pop()
