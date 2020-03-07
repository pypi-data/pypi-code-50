import os
import re

class Block:
    def __init__(self, name, type_, occurs, codes):
        self.name = name
        self.type = type_
        self.occurs = occurs
        self.codes = codes

    def __repr__(self):
        display = f'''
        {self.name}.name: {self.name}
        {self.name}.type: {self.type}
        {self.name}.occurs: {self.occurs}
        {self.name}.codes: {self.codes}
        '''
        return display

class Res:
    def __init__(self, filepath):
        self.filepath = filepath
        self._parse()

    def _parse(self):
        with open(self.filepath, 'r') as f:
            read = f.read()
        DATA_MAP = re.search(r"BEGIN_DATA_MAP([\S\s]*)END_DATA_MAP", read)
        BLOCKS = re.findall(r"([\S\s]*?)\sbegin\s([\S\s]*?)\send\s", DATA_MAP.group(1))
        self.blocks = {}
        for BLOCK in BLOCKS:
            TITLE = re.search(r"\s([\S\s]*)\s", BLOCK[0]).group(1).replace(';','').strip().split(',')
            BLOCK_NAME = TITLE[0]
            BLOCK_TYPE = TITLE[2]
            BLOCK_OCCURS = True if 'occurs' in TITLE else False
            BLOCK_CODES = {} # empty dict for final return
            CODES = re.sub(r'\n\s*\n','\n', re.search(r"\s([\S\s]*)\s", BLOCK[1]).group(1)).replace(' ','').replace(';','').replace('\t','').strip().split('\n')
            for CODE in CODES:
                if CODE.split(',') != ['']:
                    name, code, _, _, _ = CODE.split(',')
                    BLOCK_CODES[name] = code
            self.blocks[BLOCK_NAME] = Block(BLOCK_NAME, BLOCK_TYPE, BLOCK_OCCURS, BLOCK_CODES)
            self.__setattr__(BLOCK_NAME, self.blocks[BLOCK_NAME])

    def __repr__(self):
        return self.filepath

path = r"C:\eBEST\xingAPI\Res"
files = os.listdir(path)
for file in files:
    name = os.path.splitext(file)[0]
    filepath = os.path.join(path, file)
    globals()[name] = Res(filepath)

del file, name, filepath, Res, Block