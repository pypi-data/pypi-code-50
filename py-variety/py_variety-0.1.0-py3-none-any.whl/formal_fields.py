# -*- coding: utf-8 -*-
import re
import ast
import pymongo
import subprocess


def formal_fields(host='127.0.0.1', port='27017', verify=None, db_name='', coll_name='', new_name=''):
    """
    MongoDB列出所有字段并规整
    :param host:str,MongoDB地址
    :param port:str,MongoDB端口
    :param verify:dict,MongoDB验证所需参数
                    user:用户名
                    passwd:密码
                    authdb:验证数据库
    :param db_name:目标数据库名
    :param coll_name:目标集合名
    :param new_name:规整完字段后的集合名,默认为在原集合名后加上 '__formal'
    :return:正确执行返回None
            错误执行返回错误信息
    """
    print('正在查找所有字段......')
    if verify:
        popenargs = ['mongo', '--host', host, '--port', port, '-u', verify.get('user'), '-p', verify.get('passwd'),
                     db_name, '--eval', "var collection = '%s'" % coll_name, 'variety/variety.js',
                     '--authenticationDatabase=%s' % verify.get('authdb')]
        mongo_uri = 'mongodb://%s:%s@%s:%s/?authSource=%s' % (
            verify.get('user'), verify.get('passwd'), host, port, verify.get('authdb'))
    else:
        popenargs = ['mongo', '--host', host, '--port', port, db_name, '--eval', "var collection = '%s'" % coll_name,
                     'variety/variety.js']
        mongo_uri = 'mongodb://%s:%s' % (host, port)
    # 执行 js
    subp = subprocess.run(popenargs, capture_output=True)
    err = subp.stderr.decode('utf-8')
    if err:
        print(err)
        return err
    output = subp.stdout.decode('utf-8')
    # 取出第一级的所有字段名
    li_1 = re.findall('\| (.*?)\|.*\|', output)
    li_2 = [i.strip() for i in li_1 if '.' not in i]

    cli = pymongo.MongoClient(mongo_uri)
    coll = cli[db_name][coll_name]

    # 构造聚合 js
    s = ''
    for i in li_2[2:]:
        s += "'%s':{'$ifNull':['$%s','']}," % (i, i)
    # 处理之后的集合名
    if new_name:
        coll_name_pro = new_name
    else:
        coll_name_pro = coll_name + '__formal'
    aggregate_js = "[{'$project':{%s}},{'$out':'%s'}]" % (s, coll_name_pro)
    aggregate_js = ast.literal_eval(aggregate_js)
    print('正在聚合，请等待.....')
    coll.aggregate(aggregate_js)
    print('聚合结束，处理后的集合名为：\t[ %s ]' % coll_name_pro)


if __name__ == '__main__':
    print('*' * 25 + '\t' + 'MongoDB 列出所有字段并规整' + '\t' + '*' * 25 + '\n')
    db_name = input('请输入数据库名：')
    coll_name = input('请输入集合名：')
    formal_fields(host='x.x.x.x', verify={'user': 'xxx', 'passwd': 'xxxxxx', 'authdb': 'xxxx'},
                  db_name=db_name, coll_name=coll_name)
