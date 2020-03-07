import os

def get_resfile(code):
    return os.path.join(os.path.dirname(__file__), 'res', code+'.res')  

def parse_resfile(resfile):
    with open(resfile) as f:
        return [[word.strip() for word in line.replace(";","").split(",")] for line in f.readlines()]

def get_trname(code):
    resfile = get_resfile(code)
    r = parse_resfile(resfile)
    return r[1][1]

def get_resblocks(resfile):
    r = parse_resfile(resfile)

    idx_head, idx_begin, idx_end = [], [], []
    for i, x in enumerate(r):
        if x == ['begin']:
            idx_head.append(i-1)
            idx_begin.append(i+1)
        if x == ['end']:
            idx_end.append(i)

    blocks = []
    for h, b, e in zip(idx_head,idx_begin,idx_end):
        blocks.append(dict(
            type  = r[h][2], # input/output
            name  = r[h][0], # InBlock/Outblock name
            occurs= True if "occurs" in r[h] else False, # occurs boolean
            args  = [x[1] for x in r[b:e]]))
    return blocks

def query_blocks(code,key,value):
    resfile = get_resfile(code)
    blocks  = get_resblocks(resfile)
    return [block for block in blocks if block[key] == value]

def get_input(code):
    return query_blocks(code=code, key="type", value="input")

def get_output(code):
    return query_blocks(code=code ,key="type", value="output")

def get_output_frame(code):
    frame = dict()
    out_blocks = get_output(code)
    for out_block in out_blocks:
        frame[out_block["name"]] = dict()
        for arg in out_block["args"]:
            frame[out_block["name"]][arg] = list()
    return frame

def get_cts_fields(code):
    cts_fields = list()
    out_blocks = get_output(code)
    for out_block in out_blocks:
        for arg in out_block["args"]:
            if 'cts_' in arg:
                cts_fields.append(arg)
    return cts_fields

def get_is_cts(code):
    out_blocks = get_output(code)
    for out_block in out_blocks:
        for arg in out_block["args"]:
            if 'cts_' in arg:
                return True
    return False

if __name__ == "__main__":
    print(get_trname(get_resfile("t1101")))