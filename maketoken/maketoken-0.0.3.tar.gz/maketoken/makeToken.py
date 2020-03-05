import jieba
import chardet
import sys


def parse_args():
    print(sys.argv)
    return sys.argv[1], sys.argv[2]


def run():
    file, target = parse_args()
    charType = chardet.detect(open(file, 'rb').read())
    print(charType)
    with open(file,'r',errors='ignore', encoding=charType.get('encoding', 'utf-8')) as fp:
        lines = fp.readlines()
        for line in lines:
            seg_list = jieba.cut(line)
            with open(target, 'a+', encoding='utf-8') as ff:
               	ff.write(' '.join(seg_list))

if __name__ == '__main__':
    run()
