import string
import re 

useless = string.printable + "，。；’：‘’“”！？《》￥…（）—·【】、"


def has_chinese(str0):
    """判断是否存在汉字
    """
    return bool(re.search(u'[\u4e00-\u9fa5]', str0))
def has_english(str0):
    return bool(re.search('[a-z]', str0.lower()))

def has_number(str0):
    return bool(re.search('[0-9]', str0))

def replace_bracket(a):
    l0 = a.find('（')
    l1 = a.find('）')
    a=a.replace(a[l0:l1+1],'')
    return a

def sub2empty(useless, str0):
    return re.sub(f"[{useless}]+", "", str0)

def fstring(string, N=20, align='>', symbol=None, space=" "):
    """Chinese and English mixed string alignment
     chr(12288): Chinese space"""
    #def lenStr(string, zh=1, en=0.58):if space is chr(12288)
    def lenStr(string, zh=1.80, en=1):
        count = 0
        for i in string:
            if has_chinese(i):
                count += zh
            else:
                count += en
        return count
    n = int(lenStr(string))
    if symbol == None:
        symbol = space
    if align == '>':
        out = (N-n)*symbol+string
    elif align == "<":
        out = string + symbol*(N-n)
    elif align == "^":
        left = (N-n)//2
        right = N-n-left
        out = left* symbol + string + right* symbol
    else:
        "align options: > < ^"
    return out


if __name__ == "__main__":
    print(useless)