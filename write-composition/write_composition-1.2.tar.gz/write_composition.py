import random
import json
import os


path = "\\"   
                      
dirs = eval(repr(os.path.split(os.path.realpath(__file__))[0]).replace('\\', '/'))

try:
    data = json.load(open('data.json', encoding='ansi'))
except:
    data = json.load(open(dirs + '//wc_data//data.json', encoding='ansi'))


def generator(title, length=800):
    body = ""
    while len(body) < length:
        num = random.randint(0, 100)
        if num < 10:
            body += "\r\n"
        elif num < 40:
            body += random.choice(data['famous']) \
                .replace('a', random.choice(data['before'])) \
                .replace('b', random.choice(data['after'])) \
                + random.choice(data['web_sen']) \
                + random.choice(data['web_sen'])           
        else:
            body += random.choice(data['bosh'])
        body = body.replace('x', title)

    return body

def make_and_write(title, length = 800):
    composition = generator(title = title, length = length)
    with open(title + '.txt', 'w+') as f:
        f.write(composition)
        f.close()
