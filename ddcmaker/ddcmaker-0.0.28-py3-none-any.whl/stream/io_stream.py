# 实现一个IO流
# readable():是否可读
# write():
# read():
# readline()
import time


class IOStream(object):
    def __init__(self):
        self.stream = []  # 存储完整的行
        self._cache = []  # 用于存储没有\n部分
        self._size = 0

    def readable(self):
        if len(self.stream) == 0 and len(self._cache) == 0:
            return False
        return True

    def write(self, msg: str):
        infos = msg.split('\n')
        if len(infos) == 0:
            return

        # 先处理cache
        if len(self._cache) != 0:
            if len(infos) == 1:
                self._cache.append(infos.pop(0))
            else:
                cache = f"{''.join(self._cache) + infos.pop(0)}"
                self.stream.append(cache)
                self._cache = []
                self._size = self._size + len(cache)
        if len(infos) != 0:
            for info in infos[:-1]:
                self.stream.append(f"{info}")
                self._size = self._size + len(info)

            # 如果最后一部分元素没有\n，则放入cache
            if not msg.endswith('\n'):
                self._cache.append(infos[-1])
                self._size = self._size + len(infos[-1])

    def read(self, size=None):
        """
        读取size个字符
        :param size:
        :return:
        """
        if not self.readable():
            raise Exception
        if size is None:
            size = self._size
        if size >= self._size:
            self.stream.append(''.join(self._cache))
            result = '\n'.join(self.stream)
            self._size = 0
            self.stream = []
            self._cache = []
            return result
        result = []
        for index in range(len(self.stream)):
            length = len(self.stream[index])
            if length <= size:
                result.append(self.stream.pop(index))
                self._size -= length
                size -= length
            else:
                result.append(self.stream[index][:size])
                self.stream[index] = self.stream[index][size:]
                self._size -= size
                size -= size
            if size == 0:
                break
        if size != 0:
            info = self._cache[:size]
            result.append(info)
            self._cache = self._cache[size:]
            self._size -= size
        return '\n'.join(result)

    def readline(self):
        """读一行"""
        if not self.readable():
            raise Exception
        if len(self.stream) != 0:
            info = [self.stream.pop(0), '']
        else:
            info = ["".join(self._cache), '']
            self._cache = []
        return '\n'.join(info)


def test():
    io_stream = IOStream()
    strs = 'asdasd\n'
    io_stream.write(strs)
    assert io_stream._cache == []
    assert io_stream.readline() == strs

    io_stream.write('asdad')
    assert io_stream._cache == ['asdad']
    assert io_stream.stream == []

    io_stream.write('1234')
    assert io_stream._cache == ['asdad', '1234']
    assert io_stream.stream == []

    io_stream.write('\n')
    assert io_stream._cache == []
    assert io_stream.stream == ['asdad1234']

    assert io_stream.read(3) == 'asd'
    assert io_stream.read() == 'ad1234\n'

    io_stream.write('abcd\n1234\nlmn')
    assert io_stream._cache == ['lmn']
    assert io_stream.stream == ['abcd', '1234']
    assert io_stream.readline() == 'abcd\n'
    assert io_stream._cache == ['lmn']
    assert io_stream.stream == ['1234']


def test_thread():
    import threading
    io_stream = IOStream()

    def write(io_stream: IOStream):
        for i in range(20):
            df = str(i)+"打死你个嘚嘚儿！"
            io_stream.write(f'{df}\n')
            time.sleep(1)

    def read(io_stream: IOStream):
        i = 0
        while True:
            if io_stream.readable():
                info = io_stream.readline()
                print(info)
                i += 1
            time.sleep(1)
            if i == 20:
                break

    write_thread = threading.Thread(target=write, args=(io_stream,))
    read_thread = threading.Thread(target=read, args=(io_stream,))
    write_thread.start()
    read_thread.start()
    write_thread. join()
    read_thread.join()


if __name__ == '__main__':
    test()
    test_thread()
