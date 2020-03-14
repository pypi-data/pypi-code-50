import random
import json
import os


path = "\\"   
                      
dirs = eval(repr(os.path.split(os.path.realpath(__file__))[0]).replace('\\', '/'))

def generator(title, lenth=800):
    data = json.load(open(dirs + '//wc_data//data.json', encoding='ansi'))
    body = ""
    while len(body) < lenth:
        num = random.randint(0, 100)
        if num < 10:
            body += "\r\n"
        elif num < 30:
            body += random.choice(data['famous']) \
                .replace('a', random.choice(data['before'])) \
                .replace('b', random.choice(data['after'])) \
                + random.choice(data['web_sen']) \
                + random.choice(data['web_sen'])
        elif num < 60:
            body += random.choice(data['lz_sen'])        
        else:
            body += random.choice(data['bosh'])
        body = body.replace('x', title)
    return body

def make_and_write(title, lenth = 800):
    composition = generator(title = title, lenth = length)
    with open(title + '.txt', 'w+') as f:
        f.write(composition)
        f.close()

def only(type_, lenth = 800, name = '小明'):
    body = ''
    if type_ == 'famous_quotes':
        data_mingyan = json.load(open(dirs + '//wc_data//data_mingyan.json', 'r', encoding='utf8'))
        while len(body) < lenth:
            num = random.randint(0, 100)
            if num < 10:
                body += "\r\n"
            else:
                body += random.choice(data_mingyan)
        return body
    elif type_ == 'bullshit':
        bs_pasj = json.load(open(dirs + '//wc_data//bullshit_pasj.json', 'r', encoding = 'gb2312'))
        body += name + ',' + random.choice(bs_pasj['place']) + \
                '省' + random.choice(bs_pasj['place']) + '市人。\n' \
                + str(random.randint(9, 12)) + '岁以' + \
                random.choice(bs_pasj['achievement']) + '的好成绩' + \
                '顺利考入' + random.choice(bs_pasj['school']) + \
                random.choice(bs_pasj['job']) + '学院。\n' + \
                '一生有' + str(random.randint(1, 5)) + '000' + \
                '多项发明。'
        return body
    else:
        pass

