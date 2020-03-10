class BitSet:
    '''
    >用于维护一个定长的二进制串<
    创建BitSet对象:
        a = BitSet(8)               # 8位二进制串
        b = BitSet('00101101')      # 8位二进制串 初值为45
        c = BitSet(b'\xff')         # 8位二进制串 初值为255
        d = BitSet(['a', 'b', 'c']) # 3位二进制串 初值为0   三位名字分别为abc
        e = BitSet(('a', 'b', 'c')) # 3位二进制串 初值为0   三位名字分别为abc
        f = BitSet(b)               # 8位二进制串 初值为45(来自b)
        g = BitSet({'a':1, 'b':0})  # 2位二进制串 初值为2   两位名字分别是ab
    使用BitSet对象:
        赋值操作:
            a(123)                  # 向a赋值123, 会返回a本身
            a[3] = 0                # 将a从左向右第4位设置成0
            a[1:4] = 5              # 将a从第2位开始3位的切片设置成5
            d['a'] = 1              # 将d的a位设置成1
            d.b = 1                 # 将d的b位设置成1
        可以转换成int,bytes,list,tuple,bool,str
        format支持的格式:
            <w>                     # BitSet的位宽
            <b>                     # BitSet的二进制形式(高位不补0)
            <0b>                    # BitSet的二进制形式(高位补满位宽)
            <o>                     # BitSet的八进制形式(高位不补0)
            <0o>                    # BitSet的八进制形式(高位补满位宽)
            <u>                     # BitSet的十进制形式(无符号)
            <d>                     # BitSet的十进制形式(有符号位)
            <x>                     # BitSet的十六进制形式(高位不补0,小写)
            <0x>                    # BitSet的十六进制形式(高位补满位宽)
            <X>                     # BitSet的十六进制形式(高位不补0,大写)
            <0X>                    # BitSet的十六进制形式(高位补满位宽)
            <m>                     # BitSet按位表示形式
    更多信息请查看源代码
    '''
    def __init__(self, bit_mask, *, gen_strmask=False):
        if isinstance(bit_mask, int) : 
            self.width = bit_mask
            if gen_strmask :
                self.strmask = ["bit"+str(i) for i in range(bit_mask)]
            else : self.strmask = []
            self.data = 0
        if isinstance(bit_mask, bytes) : 
            bit_width = len(bit_mask) * 8
            bit_mask = self.__trans__(bit_mask)
            bit_mask.width = bit_width
        if isinstance(bit_mask, str) : 
            bit_mask = self.__trans__(bit_mask)
        if isinstance(bit_mask, (tuple, list)) : 
            self.width = len(bit_mask)
            self.strmask = [str(i) for i in bit_mask]
            self.data = 0
        if isinstance(bit_mask, BitSet) : 
            self.width = bit_mask.width
            self.strmask = list(bit_mask.strmask)
            self.data = bit_mask.data
        if isinstance(bit_mask, dict) : 
            self.width = len(bit_mask)
            self.strmask = [str(i) for i in bit_mask.keys()]
            self.data = self.__trans__(list(bit_mask.values())).data
        if self.width <= 0 : raise ValueError("位宽必须大于0")
        self.tranb = "{:0>%db}"%self.width      # 字符串转换格式Bin
        owidth = self.width // 3 + (self.width % 3 != 0)
        self.trano = "{:0>%ds}"%owidth          # 字符串转换格式Oct
        xwidth = self.width // 4 + (self.width % 4 != 0)
        self.tranx = "{:0>%ds}"%xwidth          # 字符串转换格式Hex
        self.mask = pow(2, self.width) - 1      # 2进制掩码
        self.mods = {}
    # 在直接输入这个名字的时候会返回指定位宽的二进制数
    def __repr__(self):
        return self.tranb.format(self.data)
    # 返回二进制数指定的位宽
    def __len__(self):
        return self.width
    # 返回二进制的数值(无符号)
    def __int__(self):
        return self.data
    # 返回bytes序列(右对齐)
    def __bytes__(self):
        if self.width % 8 : lenth = (self.width // 8) + 1
        else : lenth = self.width // 8
        return self.data.to_bytes(lenth, "big")
    # 返回list列表
    def __list__(self):
        return [i for i in self]
    # 返回tuple列表
    def __tuple__(self):
        return tuple(i for i in self)
    # 返回真假(全为0时为假)
    def __bool__(self):
        return bool(self.data)
    # 返回二进制数的字符串形式
    def __str__(self):
        return self.tranb.format(self.data)
    # 返回指定格式的字符串
    def __format__(self, tips):
        if tips == "" : 
            return str(self)
        if "<w>" in tips : 
            tips = tips.replace("<w>", str(self.width))
        if "<b>" in tips : 
            tips = tips.replace("<b>", bin(self.data)[2:])
        if "<0b>" in tips : 
            tips = tips.replace("<0b>", str(self))
        if "<o>" in tips : 
            tips = tips.replace("<o>", oct(self.data)[2:])
        if "<0o>" in tips : 
            tips = tips.replace("<0o>", self.trano.format(oct(self.data)[2:]))
        if "<u>" in tips : 
            tips = tips.replace("<u>", str(self.data))
        if "<d>" in tips : 
            if self.data >= pow(2, self.width-1) : 
                tips = tips.replace("<d>", "-"+str(abs(self).data))
            else : tips = tips.replace("<d>", str(self.data))
        if "<x>" in tips :
            tips = tips.replace("<x>", hex(self.data)[2:])
        if "<0x>" in tips :
            tips = tips.replace("<0x>", self.tranx.format(hex(self.data)[2:]))
        if "<X>" in tips :
            tips = tips.replace("<X>", hex(self.data)[2:].upper())
        if "<0X>" in tips :
            tips = tips.replace("<0X>", self.tranx.format(hex(self.data)[2:].upper()))
        if "<m>" in tips :
            if bool(self.strmask) : 
                tips = "".join(["<%s>:[%d] "%(s, self[s]) for s in self.strmask])[:-1]
            else : tips = "<NO DATAMASK>"
        return tips
    # 赋值、取值方法(链式赋值)
    def __call__(self, value=None):
        '''
        使用Call方法来设置BitSet的值
        无参数的时候会返回自己
        '''
        if isinstance(value, type(None)) : return self
        if isinstance(value, int) : 
            self.data = value & self.mask
        elif isinstance(value, (bool, bytes, list, tuple, list, BitSet)) :
            value = self.__trans__(value)
            self.data = value.data & self.mask
        else : raise TypeError("请传入类型为int,bool,bytes,list,tuple,BitSet的值")
        return self
    def __dir__(self):
        WID = "<位宽>:[{:<w>}]".format(self)
        BIT = "<数据:bit>:[{:<B>}]".format(self)
        INT = "<数据:int>:[{:<d>}]".format(self)
        UINT = "<数据:uint>:[{:<u>}]".format(self)
        MASK = "<详细>:{{ {:<m>} }}".format(self)
        return [WID, BIT, UINT, INT, MASK]
    # 返回迭代器来完成迭代, 避免出现迭代未完成的情况
    class _iterator:
        '''BitSet专用迭代器'''
        def __init__(self, wrapped):
            '''传入一个BitSet'''
            self.wrap = wrapped
            self.offset = 0
        def __iter__(self):
            return self
        def __length_hint__(self):
            if self.wrap.width - self.offset > 0 :
                return self.wrap.width - self.offset
            else : return 0
        def __next__(self):
            if self.offset == self.wrap.width : 
                raise StopIteration("迭代器结束")
            self.offset = self.offset + 1
            return (self.wrap.data >> self.wrap.width - self.offset) & 1
        def __setstate__(self, state:int):
            self.offset = state
    # 迭代器函数, 返回可迭代对象
    def __iter__(self):
        return BitSet._iterator(self)
    def __reversed__(self):
        return BitSet(self.width)(int(self.tranb.format(self.data)[::-1], 2))
    # 获取指定项/切片
    def __getitem__(self, key):
        key = self.__mask__(key)
        item = str(self)[key]
        return BitSet(len(item))(int(item, 2))
    def __setitem__(self, key, value) : 
        key = self.__mask__(key)
        item = list(self)
        value = BitSet(self.__masklen__(key))(value)
        if len(str(self)[key]) >= len(value) : 
            item[key] = list(str(value))
            item = [str(i) for i in item]
            self.data = int("0"+"".join(item), 2)
        else : raise ValueError("设定的长度不匹配")
    def __getattr__(self, key:str):
        if key in self.strmask : 
            return self[key]
        else : raise AttributeError("没有名为'%s'的位存在"%key)
    def __setattr__(self, key:str, value):
        if key in ["width", "strmask", "data", "tranb", "trano", "tranx", "mask", "mods"] : 
            self.__dict__[key] = value
        elif key in self.strmask : 
            self[key] = value
        else : raise AttributeError("没有名为'%s'的位存在"%key)
    # 计算类魔术方法
    # 求绝对值,对于首位为1的二进制数被认为是负数
    def __abs__(self):
        if self.data >= pow(2, self.width-1) : 
            return BitSet(self.width)(pow(2, self.width) - self.data)
        else : return BitSet(self.width)(self.data)
    # 求负数，和求反有点不一样
    def __neg__(self):
        return BitSet(self.width)(-self.data & self.mask)
    # 求正
    def __pos__(self):
        return BitSet(self.width)(self.data)
    # 求反
    def __invert__(self):
        return BitSet(self.width)(pow(2, self.width)-self.data-1)
    # 比较函数
    def __lt__(self, other):
        other = self.__trans__(other)
        return self.data < other.data
    def __le__(self, other):
        other = self.__trans__(other)
        return self.data <= other.data
    def __eq__(self, other):
        other = self.__trans__(other)
        return self.data == other.data
    def __ne__(self, other):
        other = self.__trans__(other)
        return self.data != other.data
    def __gt__(self, other):
        other = self.__trans__(other)
        return self.data > other.data
    def __ge__(self, other):
        other = self.__trans__(other)
        return self.data >= other.data
    # 运算函数
    def __add__(self, other):
        other = self.__trans__(other)
        return self.__trans__(self.data + other.data)
    def __sub__(self, other):
        other = self.__trans__(other)
        return self.__trans__(self.data - other.data)
    def __lshift__(self, other):
        other = self.__trans__(other)
        return self.__trans__(self.data << other.data)
    def __rshift__(self, other):
        other = self.__trans__(other)
        return self.__trans__(self.data >> other.data)
    def __and__(self, other):
        other = self.__trans__(other)
        return self.__trans__(self.data & other.data)
    def __xor__(self, other):
        other = self.__trans__(other)
        return self.__trans__(self.data ^ other.data)
    def __or__(self, other):
        other = self.__trans__(other)
        return self.__trans__(self.data | other.data)
    class _masked:
        '''BitSet的切片引用类，去掉了计算功能，用call可以返回一个BitSet对象参与运算'''
        def __init__(self, data, mask):
            self.mask = data.__mask__(mask)
            self.wrap = data
            self.width = data[self.mask].width
            self.bitmask = data[self.mask].mask
            self.bind = []
        def __repr__(self):
            return self.wrap[self.mask].__repr__()
        def __call__(self, value=None):
            if isinstance(value, type(None)) : return self.wrap[self.mask]
            if isinstance(value, int) : self.wrap[self.mask] = value & self.bitmask
            elif isinstance(value, (bool, bytes, list, tuple, list, BitSet, type(self))) :
                value = self.wrap.__trans__(value)
                self.wrap[self.mask] = value.data & self.bitmask
            else : raise TypeError("请传入类型为int,bool,bytes,list,tuple,BitSet的值")
            return self
        def __bind__(self, pin):
            self.bind.append(pin)
        def __update__(self):
            for conn in self.bind : conn(self())
    def __matmul__(self, mask):
        return BitSet._masked(self, mask)
    # 自运算函数(位数不够会切断)
    def __iadd__(self, other):
        other = self.__trans__(other)
        return self.__call__(self.data + other.data)
    def __isub__(self, other):
        other = self.__trans__(other)
        return self.__call__(self.data - other.data)
    def __ilshift__(self, other):
        other = self.__trans__(other)
        return self.__call__(self.data << other.data)
    def __irshift__(self, other):
        other = self.__trans__(other)
        return self.__call__(self.data >> other.data)
    def __iand__(self, other):
        other = self.__trans__(other)
        return self.__call__(self.data & other.data)
    def __ixor__(self, other):
        other = self.__trans__(other)
        return self.__call__(self.data ^ other.data)
    def __ior__(self, other):
        other = self.__trans__(other)
        return self.__call__(self.data | other.data)
    # 右运算符
    def __radd__(self, other):
        res = self.__trans__(other) + self
        return type(other)(res)
    def __rsub__(self, other):
        res = self.__trans__(other) - self
        return type(other)(res)
    def __rlshift__(self, other):
        res = self.__trans__(other) << self
        return type(other)(res)
    def __rrshift__(self, other):
        res = self.__trans__(other) >> self
        return type(other)(res)
    def __rand__(self, other):
        res = self.__trans__(other) & self
        return type(other)(res)
    def __rxor__(self, other):
        res = self.__trans__(other) ^ self
        return type(other)(res)
    def __ror__(self, other):
        res = self.__trans__(other) | self
        return type(other)(res)
    # 工具方法
    def __trans__(self, data):
        if isinstance(data, BitSet) :           # 传入是BitSet
            return data
        elif isinstance(data, BitSet._masked) : # 传入是BitSet的切片引用
            return data()
        elif isinstance(data, bytes) :          # 传入是Bytes
            data = int.from_bytes(data, "big")
            return BitSet(len(bin(data))-2)(data)
        elif isinstance(data, int) :            # 传入是Int
            return BitSet(len(bin(data))-2)(data)
        elif isinstance(data, (list, tuple)) :  # 传入是List,Tuple
            if set(data).issubset({0, 1, "0", "1"}) : 
                data = [str(i) for i in data]
                data = int("0"+"".join(data), 2)
                return BitSet(len(bin(data))-2)(data)
            else : raise ValueError("List/Tuple中只能包含0, 1, '0', '1'")
        elif isinstance(data, bool) :           # 传入是Bool
            return BitSet(1)(int(data))
        elif isinstance(data, str) :            # 传入是Str
            try : data = int(data, 2)
            except : raise ValueError("Str中出现了二进制以外的字符")
            else : return BitSet(len(bin(data))-2)(data)
        else : raise TypeError("无法将传入的数据转换为BitSet")
    def __mask__(self, key):
        if isinstance(key, slice) : 
            return key
        elif isinstance(key, int) : 
            return slice(key, key+1)
        elif isinstance(key, str) : 
            if key in self.strmask : key = self.strmask.index(key)
            else : raise KeyError(key)
            return slice(key, key+1)
        elif isinstance(key, list):
            if   len(key) == 1 : return slice(key[0], key[0]+1)
            elif len(key) == 2 : return slice(key[0], key[1])
            elif len(key) == 3 : return slice(key[0], key[1], key[2])
            else : raise ValueError("传入的List无法转化成slice,参数过多")
        else : 
            try : key = int(key)
            except : raise TypeError("传入的类型无法转换成索引%s"%key.__class__.__name__)
            else : return slice(key, key+1)
    def __masklen__(self, key):
        key = self.__mask__(key)
        return len(("0"*128)[key])

