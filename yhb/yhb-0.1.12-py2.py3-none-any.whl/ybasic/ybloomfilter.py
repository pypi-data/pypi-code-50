import redis
from hashlib import md5


class SimpleHash:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed

    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])

        return (self.cap - 1) & ret


class BloomFilter:
    def __init__(self, host='localhost', port=6379, db=0, password="123456", block_num=2, key="bloomfilter"):
        self.server = redis.Redis(host=host, port=port, db=db, password=password)
        self.bit_size = 1 << 31
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.key = key
        self.block_num = block_num
        self.hash_func = []
        for seed in self.seeds:
            self.hash_func.append(SimpleHash(self.bit_size, seed))

    def get_md5(self, str_input):
        m5 = md5()
        str_input = str_input.encode("utf-8")
        m5.update(str_input)
        return m5.hexdigest()

    def is_contain(self, str_input):
        if not str_input:
            return False
        str_input = self.get_md5(str_input)
        ret = True
        name = self.key + str(int(str_input[0:2], 16) % self.block_num)
        for f in self.hash_func:
            loc = f.hash(str_input)
            ret = ret & self.server.getbit(name, loc)
        return ret

    def insert(self, str_input):
        str_input = self.get_md5(str_input)
        name = self.key + str(int(str_input[0:2], 16) % self.block_num)
        for f in self.hash_func:
            loc = f.hash(str_input)
            self.server.setbit(name, loc, 1)


if __name__ == '__main__':
    bf = BloomFilter()
    if bf.is_contain('http://www.66.com'):
        print('exists!')
    else:
        print('not exists!')
        bf.insert('http://www.66.com')
