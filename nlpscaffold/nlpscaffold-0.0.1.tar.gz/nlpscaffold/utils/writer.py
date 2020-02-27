import json


class Writer:

    def __init__(self, fname):
        self.fname = fname
        self.file = None

    def write(self, content, newline=False, mode='w', close_on_finish=True, stdout=False):
        if newline:
            content += '\n'
        if self.file is None or self.file.closed:
            self.file = open(self.fname, mode=mode)
        self.file.write(content)
        if close_on_finish:
            self.file.close()
        if stdout:
            print(content[:-1])  # strip added newline

    def write_dict(self, data, newline=False, mode='w', close_on_finish=True, indent=2, stdout=False):
        content = json.dumps(data, indent=indent)
        if newline:
            content += '\n'
        self.write(content, mode=mode, close_on_finish=close_on_finish, stdout=stdout)

    def close(self):
        if self.file and not self.file.closed:
            self.file.close()
