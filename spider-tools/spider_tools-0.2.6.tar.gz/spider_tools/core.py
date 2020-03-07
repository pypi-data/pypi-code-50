# _*_coding:utf-8_*_
# Author_name : by zcl
# Emial: zclmbf597854439@gmial.com
# Created at: 2020/3/7
import hashlib, json, re, os, random, xlrd
import time
import datetime
import redis, execjs
from os import listdir
import jieba.posseg as pseg
import arrow
import math, pymysql
import numpy as np
from scrapy import Selector
import pytesseract, requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from multiprocessing import Pool, Process, Queue
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chardet

# sudo pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple           linux
# pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple                             windows

# 红色输出

status_404 = 500


def red_print(str):
    print('\033[31m{}\033[0m'.format(str))


class Auto_indb():
    def __init__(self,host='rm-2zeo0ew8s18q793q32o.mysql.rds.aliyuncs.com', username='hd_woca', password='', db='hd_one', table_name='', comment='', create_tables=True):
        red_print("--------------------------------------------------------------------------------------------")
        print(
            '''auto_indb = t.Auto_indb(host='192.168.4.201',username='root',password='mysql',db="storm",table_name='',comment='表注释',create_tables=True)''')
        red_print("--------------------------------------------------------------------------------------------")
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.comment = comment  # 表注释
        self.table_name = table_name
        self.create_tables = create_tables  # 是否创建表
        try:
            self.conn = pymysql.connect(self.host, self.username, self.password, self.db, charset='utf8')
            self.cursor = self.conn.cursor()
            print("连接数据库成功")
        except:
            raise ('连接数据库失败')
        self.columns = self.get_columns()
        if create_tables:
            self.table_exists()

    def table_exists(self):
        hassql = ' show tables where Tables_in_%s ="%s"' % (self.db, self.table_name)
        has = self.cursor.execute(hassql)
        if has:
            print("该{}表已经存在".format(self.table_name))
            judge = input("是否需要删除表重新建表 y/n:")
            if judge == 'y':
                drop_table = "drop table if exists {}".format(self.table_name)
                self.cursor.execute(drop_table)
                self.conn.commit()
                self.create_table()
            else:
                print("未创建表")
        else:
            self.create_table()

    def create_table(self):
        newtab = '''
                   CREATE TABLE `%s` (
                   	`id` INT(11) NOT NULL AUTO_INCREMENT primary key ,
                   	`url` TEXT not NULL,
                   	`updated` DATATIME NULL DEFAULT CURRENT_TIMESTAMP
                   )
                   COMMENT='%s'
                   ENGINE=MyISAM;
                   ''' % (self.table_name, self.comment)
        self.cursor.execute(newtab)
        self.conn.commit()
        print("创建{}表成功".format(self.table_name))

    def get_columns(self):
        result = []
        sql = "select COLUMN_NAME from information_schema.columns where table_name='%s'" % self.table_name
        self.cursor.execute(sql)
        for res in self.cursor.fetchall():
            res = res[0]
            result.append(res)
        return result

    def insert_data(self, items):
        keys = ''
        vals = []
        s = ''
        for item in items.keys():
            if not item in self.get_columns():
                sql = 'alter table %s add %s text' % (self.table_name, item)
                self.cursor.execute(sql)
                self.conn.commit()
                self.columns.append(item)
            if item:
                keys += item + ','
                s += '%s,'
                vals.append(items.get(item))
        keys = keys[:-1]
        indbsrt = 'insert ignore into %s(%s) VALUES (%s)' % (
        self.table_name, keys, ','.join(pymysql.escape_string('%r') % str(i) for i in vals))
        print(indbsrt)
        self.cursor.execute(indbsrt)
        self.conn.commit()
        print("###################  insert data success ################")


# 使用说明:
# create_tables为是否自动建表,默认为True
# auto_indb = Auto_indb(host='192.168.4.201',username='root',password='mysql',db="storm",table_name='',comment='表注释',create_tables=True)
# item要插入的字典
# i.insert_data(item)
class Auto_sinsert():
    def __init__(self, host='rm-2zeo0ew8s18q793q32o.mysql.rds.aliyuncs.com', username='hd_woca', password='', db='hd_one',
                 drop_column=["id", "updated"]):
        red_print("--------------------------------------------------------------------------------------------")
        print(
            '''auto_sinsert = t.Auto_sinsert(host='192.168.4.201',username='root',password='mysql',db='zhijianju',drop_column=["id","jid","updated","entid"])''')
        red_print("--------------------------------------------------------------------------------------------")
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.drop_column = drop_column  # 表删除字段
        try:
            self.conn = pymysql.connect(self.host, self.username, self.password, self.db, charset='utf8')
            self.cursor = self.conn.cursor()
            print("连接数据库成功")
        except:
            raise ValueError('连接数据库失败')
        self.table_name_list = self.get_db_name()

    def get_db_name(self):
        sql = "select table_name from information_schema.tables where table_schema='{}'".format(self.db)
        self.cursor.execute(sql)
        db_list = self.cursor.fetchall()
        db_list = [i[0] for i in db_list]
        return db_list

    def get_columns(self):
        item = {}
        for table_name in self.table_name_list:
            sql = "select column_name from information_schema.columns where table_name=%r and table_schema=%r" % (
            table_name, self.db)
            self.cursor.execute(sql)
            column_list = self.cursor.fetchall()
            column_list = [i[0] for i in column_list]
            insert_columns = [i for i in column_list if i not in self.drop_column]
            item[table_name] = insert_columns
        return item

    def insert_data(self, item, table_name):
        if item:
            insert_tables_key = self.get_columns()
            item_key = insert_tables_key.get(table_name)
            if item_key:
                item_values = [item.get(i) for i in item_key]
                sql = 'insert ignore into {}('.format(table_name) + ','.join(item_key) + ')values(' + ','.join(
                    [pymysql.escape_string('%r') % str(i) for i in item_values]) + ')'
                self.cursor.execute(sql)
                self.conn.commit()
                print("###################  insert data success ################")
            else:
                raise ValueError("没有{}表".format(table_name))
        else:
            print("item is None")


# 使用说明:
# item = {'key':'none'}
# # drop_column 为所有表中不插入的字段
# auto_sinsert = Auto_sinsert(host='192.168.4.201',username='root',password='mysql',db='zhijianju',drop_column=["id","jid","update","entid"])
# a.insert_data(item,'aqsiq_biaozhun_basic')

# ID增量更新，查询最大ID
class query_db():
    table_name = 'dataplus_b2b_update'

    def __init__(self):
        self.conn = pymysql.connect(host='192.168.4.205', port=3306, user='root', passwd='mysql', db='storm',
                                    charset='utf8')
        self.cursor = self.conn.cursor()
        print("连接数据库成功")

    def query_max_id(self, b2b_name):
        sql = 'select url from {}'.format('max_url') + ' where b2b=%r' % b2b_name
        print("正在查询max_url表中{}url最大ID。。。".format(b2b_name))
        self.cursor.execute(sql)
        urls = self.cursor.fetchall()
        id_list = []
        for url in urls:
            id_l = re.findall('\d+', str(url), re.S)
            for i in id_l:
                id_list.append(int(i))
                id_list.append(1)
                id_list.append(1)

        if id_list:
            key = max(id_list, key=id_list.count)
            id_list = set(id_list)
            id_list.remove(key)
            max_id = max(id_list)
            print(max_id)
            return max_id

        else:
            print("没有查询到最大id")
            return 1000000

    def insert_max_data(self, item, b2b_name):
        url = item.get('url')
        if url:
            insert_into = '''insert into max_url(url,b2b) values ('%s','%s') ''' % (url, b2b_name)
            self.cursor.execute(insert_into)
            self.conn.commit()
            print("存入{}最大id成功".format(b2b_name))
        else:
            print("木有发现最大url,无法存入")


# 执行sql语句
class Execute_sql():
    def __init__(self, host='', username='', password='', db=''):
        red_print("--------------------------------------------------------------------------------------------")
        print('''execute_sql = t.Execute_sql(host='192.168.4.201',username='root',password='mysql',db='zhijianju')''')
        red_print("--------------------------------------------------------------------------------------------")
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        try:
            self.conn = pymysql.connect(self.host, self.username, self.password, self.db, charset='utf8')
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql,data)
            print("连接数据库成功")
        except:
            raise ValueError('连接数据库失败')

    def select_sql(self, cloumns='*', table_name='', limit='10'):
        sql = 'select {} from {} limit {}'.format(cloumns, table_name, limit)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def get_scrapy_filed(self, table_name):
        sql = '''
        select column_name,column_comment from information_schema.columns where table_name='{}' and table_schema='{}'
        '''.format(table_name, self.db)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            red_print('----------------------------------------------------------')
            for item in result:
                item = '{} = scrapy.Field() #{}'.format(item[0], item[1])
                print(item)
            red_print('----------------------------------------------------------')
            for item in result:
                item = "item['{}'] = t.get_column(response,'') #{}".format(item[0], item[1])
                print(item)
            red_print('----------------------------------------------------------')
            os._exit(0)

        else:
            red_print('no result')
            return None

    def custom(self, sql, state='commit'):
        self.cursor.execute(sql)
        if state == 'commit':
            self.conn.commit()
        elif state == 'fetchall':
            result = self.cursor.fetchall()
            if result:
                return result
            else:
                red_print('no result')
                return None
        else:
            red_print("no practice way,please appoint commit or fetchall")


# execute_sql = Execute_sql(host='192.168.4.201',username='root',password='mysql',db='zhijianju')

class Debug_code():
    def __init__(self, url):
        self.url = url

    def get(self, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
            xpath=''):
        res = requests.get(url=self.url, headers=headers, timeout=5)
        try:
            text = res.json()
            print(text)
            result = get_column(text, xpath)
            print(result)
        except:
            text = res.text
            print(text)
            result = get_column(text, xpath)
            print(result)

    def post(self, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'},
             data={}, xpath=''):
        res = requests.post(url=self.url, headers=headers, data=data, timeout=5)
        try:
            text = res.json()
            print(text)
            result = get_column(text, xpath)
            print(result)
        except:
            text = res.text
            print(text)
            result = get_column(text, xpath)
            print(result)


class Redis_handle():
    def __init__(self, host='127.0.0.1', password='', db='1', decode_responses=True):
        self.db = db
        self.r = redis.Redis(host=host, port=6379, password=password, db=db, decode_responses=decode_responses)
        red_print("链接redis成功")

    def push_queue(self, value):
        self.r.rpush(self.db, value)

    def get_out(self):
        if self.r.llen(self.db) == 0:
            red_print("redis队列值为空,程序退出")
            os._exit(0)
        get_value = self.r.lpop(self.db)
        return get_value

    def custom(self, operation):
        pass


# 自动解析  'title':  # 'description'# 'keyword'# 'content' 四个字段
class AutoHtmlParser(object):
    """智能网页文章解析类
    影响结果的参数：
        extract_title：标题仅由'_'分割，可以再添加
        extract_content：
            1. 抛弃置信度低于1000的行块（即使最大）
            2. 在上下搜索时，对于行块字符长度低于30的直接抛弃，不进行添加
        get_blocks：
            1. 当前行的正文长度不小于30才将改行设为行块起点
            2. 当前行的正文长度不小于30，且接下去两行行正文长度均小于30才将改行设为行块终点
    """

    def __init__(self):
        # re.I: 忽略大小写，re.S: '.'可以代表任意字符包括换行符
        self._title = re.compile(r'<title>(.*?)</title>', re.I | re.S)  # 匹配标题
        self._keyword = re.compile(r'<\s*meta\s*name="?Keywords"?\s+content="?(.*?)"?\s*[/]?>', re.I | re.S)  # 匹配关键词
        self._description = re.compile(r'<\s*meta\s*name="?Description"?\s+content="?(.*?)"?\s*[/]?>',
                                       re.I | re.S)  # 匹配描述
        self._link = re.compile(r'<a(.*?)>|</a>')  # 匹配<a>，</a>标签
        self._link_mark = '|ABC|'  # 标记<a>，</a>  【在extract_content中会删除改标记，所以这里修改，那也得改】
        self._space = re.compile(r'\s+')  # 匹配所有空白字符，包括\r, \n, \t, " "
        self._stopword = re.compile(
            r'备\d+号|Copyright\s*©|版权所有|all rights reserved|广告|推广|回复|评论|关于我们|链接|About|广告|下载|href=|本网|言论|内容合作|法律法规|原创|许可证|营业执照|合作伙伴|备案',
            re.I | re.S)
        self._punc = re.compile(r',|\?|!|:|;|。|，|？|！|：|；|《|》|%|、|“|”', re.I | re.S)
        self._special_list = [(re.compile(r'&quot;', re.I | re.S), '\"'),  # 还原特殊字符
                              (re.compile(r'&amp;', re.I | re.S), '&'),
                              (re.compile(r'&lt;', re.I | re.S), '<'),
                              (re.compile(r'&gt;', re.I | re.S), '>'),
                              (re.compile(r'&nbsp;', re.I | re.S), ' '),
                              (re.compile(r'&#34;', re.I | re.S), '\"'),
                              (re.compile(r'&#38;', re.I | re.S), '&'),
                              (re.compile(r'&#60;', re.I | re.S), '<'),
                              (re.compile(r'&#62;', re.I | re.S), '>'),
                              (re.compile(r'&#160;', re.I | re.S), ' '),
                              ]

    def extract_offline(self, html):
        """离线解析html页面"""
        title = self.extract_title(html)
        description = self.extract_description(html)
        keyword = self.extract_keywords(html)
        content = self.extract_content(html, title)
        return {
            'title': title,
            'description': description,
            'keyword': keyword,
            'content': content
        }

    def extract_online(self, url):
        """在线解析html页面"""
        r = requests.get(url)
        if r.status_code == 200:
            if r.encoding == 'ISO-8859-1':
                r.encoding = chardet.detect(r.content)['encoding']  # 确定网页编码
            html = r.text
            title = self.extract_title(html)
            description = self.extract_description(html)
            keyword = self.extract_keywords(html)
            content = self.extract_content(html, title)
            return {
                'title': title,
                'description': description,
                'keyword': keyword,
                'content': content
            }
        return {}

    def extract_title(self, html):
        """解析文章标题
        :param html: 未处理tag标记的html响应页面
        :return: 字符串，如果没有找到则返回空字符串
        """
        title = self._title.search(html)
        if title:
            title = title.groups()[0]
        else:
            return ''
        # 如果标题由'_'组合而成，如"习近平告诉主要负责人改革抓什么_新闻_腾讯网"，则取字数最长的字符串作为标题
        titleArr = re.split(r'_', title)
        newTitle = titleArr[0]
        for subTitle in titleArr:
            if len(subTitle) > len(newTitle):
                newTitle = subTitle
        return newTitle

    def extract_keywords(self, html):
        """解析文章关键词
        :param html: 未处理tag标记的html响应页面
        :return: 字符串，如果没有找到则返回空字符串
        """
        keyword = self._keyword.search(html)
        if keyword:
            keyword = keyword.groups()[0]
        else:
            return ''
        # 将\n, \t, \r都转为一个空白字符
        keyword = self._space.sub(' ', keyword)
        return keyword

    def extract_description(self, html):
        """解析文章描述
        :param html: 未处理tag标记的html响应页面
        :return: 字符串，如果没有找到则返回空字符串
        """
        description = self._description.search(html)
        if description:
            keyword = description.groups()[0]
        else:
            return ''
        # 将\n, \t, \r都转为一个空白字符
        keyword = self._space.sub(' ', keyword)
        return keyword

    def extract_content(self, html, title):
        """解析正文"""
        lines = self.remove_tag(html)
        blocks = self.get_blocks(lines)
        blockScores = self.block_scores(lines, blocks, title)
        res = ""
        if len(blockScores) != 0:
            maxScore = max(blockScores)
            if maxScore > 1000:  # 置信度低于1000的抛弃
                blockIndex = blockScores.index(maxScore)
                lineStart, lineEnd = blocks[blockIndex]

                # 搜索该行块的下一块，如果出现更大的置信度则加入，否则退出
                nextIndex = blockIndex + 1
                while nextIndex < len(blocks):
                    # 如果区块字符低于30个字符，直接抛弃【这个可以根据需要改变，如果希望尽可能的捕捉所有内容可以注释改行】
                    if self.detBlockLenght(lines, blocks, nextIndex) < 30: break
                    newBlock = (lineStart, blocks[nextIndex][1])
                    score = self.block_scores(lines, [newBlock], title)[0]
                    if score > maxScore:
                        lineEnd = blocks[nextIndex][1]
                        maxScore = score
                    else:
                        break

                # 搜索该行块的上一块，如果出现更大的置信度则加入，否则退出
                lastIndex = blockIndex - 1
                while lastIndex >= 0:
                    # 如果区块字符低于30个字符，直接抛弃【这个可以根据需要改变，如果希望尽可能的捕捉所有内容可以注释改行】
                    if self.detBlockLenght(lines, blocks, nextIndex) < 30: break
                    newBlock = (blocks[lastIndex][0], lineEnd)
                    score = self.block_scores(lines, [newBlock], title)[0]
                    if score > maxScore:
                        lineEnd = blocks[nextIndex][1]
                        maxScore = score
                    else:
                        break

                res += ''.join(lines[lineStart:lineEnd])
                res = re.sub('\|ABC\|(.*?)\|ABC\|', '', res, 0, re.I | re.S)  # 去除<a>内容
        return res

    def detBlockLenght(self, lines, blocks, index):
        """检测区块中字符长度"""
        if len(blocks) <= index: return 0  # 索引越界
        lineStart, lineEnd = blocks[index]
        block = ''.join(lines[lineStart:lineEnd])
        block = re.sub('\|ABC\|(.*?)\|ABC\|', '', block, 0, re.I | re.S)  # 去除<a>内容
        return len(block)

    def get_blocks(self, lines):
        """得到所有含有正文的区块
         - 区块起始点的确定：当前行的正文长度不小于30
         - 区块终点的缺点：当前行的正文长度不小于30，且接下去两行行正文长度均小于30
        :param lines: 输入一个列表，每一项为一行
        :return: 返回一个列表，每一项为一个区块
        """
        linesLen = [len(line) for line in lines]
        totalLen = len(lines)

        blocks = []
        indexStart = 0
        while indexStart < totalLen and linesLen[indexStart] < 30: indexStart += 1
        for indexEnd in range(totalLen):
            if indexEnd > indexStart and linesLen[indexEnd] == 0 and \
                    indexEnd + 1 < totalLen and linesLen[indexEnd + 1] <= 30 and \
                    indexEnd + 2 < totalLen and linesLen[indexEnd + 2] <= 30:
                blocks.append((indexStart, indexEnd))
                indexStart = indexEnd + 3
                while indexStart < totalLen and linesLen[indexStart] <= 30: indexStart += 1
        '''
        for s, e in blocks:
            print(''.join(lines[s:e]))
        '''
        return blocks

    def block_scores(self, lines, blocks, title):
        """计算区块的置信度
         - A： 当前区块<a> 标记占区块总行数比例  （标记越多，比例越高）【0.01 - 5】
         - B： 起始位置占总行数的比例 （起始位置越前面越有可能是正文）【0 - 1】
         - C： 诸如广告，版权所有，推广等词汇数占区块总行数比例 【比较大】
         - D： 当前区块中与标题重复的字占标题的比例 【0 - 1】
         - E： 当前区块标点符号占区块总行数比例 【比较大】
         - F:  当前区块去除<a>标签后的正文占区块总行数比例 【比较大】
         - G:  当前区块中文比例 【0 - 1】
         公式： scores = G * F * B * pow(E) * （1 + D） / A / pow(C)
        :param lines: 列表，每一项为一行
        :param blocks: 列表，每一项为一个区块
        :param title: 字符串
        :return: 列表，每一项为一个区块的置信度
        """
        blockScores = []
        for indexStart, indexEnd in blocks:
            blockLinesLen = indexEnd - indexStart + 1.0
            block = ''.join(lines[indexStart:indexEnd])
            cleanBlock = block.replace(self._link_mark, '')

            linkScale = (block.count(self._link_mark) + 1.0) / blockLinesLen
            lineScale = (len(lines) - indexStart + 1.0) / (len(lines) + 1.0)
            stopScale = (len(self._stopword.findall(block)) + 1.0) / blockLinesLen
            titleMatchScale = len(set(title) & set(cleanBlock)) / (len(title) + 1.0)
            puncScale = (len(self._punc.findall(block)) + 1.0) / blockLinesLen
            textScale = (len(cleanBlock) + 1.0) / blockLinesLen
            chineseScale = len(re.findall("[\u4e00-\u9fa5]", block)) / len(block)

            score = chineseScale * textScale * lineScale * puncScale * (1.0 + titleMatchScale) / linkScale / math.pow(
                stopScale, 0.5)
            blockScores.append(score)
        ''' 输出当前最大置信度的行块
        index = blockScores.index(max(blockScores))
        start, end = blocks[index]
        print(''.join(lines[start:end]))
        print(blockScores)
        '''
        return blockScores

    def remove_tag(self, html):
        """去除html的tag标签
        :param html: 未处理tag标记的html响应页面
        :return: 返回列表，每一项为一行
        """
        for r, c in self._special_list: text = r.sub(c, html)  # 还原特殊字符
        text = re.sub(r'<script(.*?)>(.*?)</script>', '', text, 0, re.I | re.S)  # 去除javascript
        text = re.sub(r'<!--(.*?)-->', '', text, 0, re.I | re.S)  # 去除注释
        text = re.sub(r'<style(.*?)>(.*?)</style>', '', text, 0, re.I | re.S)  # 去除css
        text = re.sub(r"&.{2,6};|&#.{2,5};", '', text)  # 去除如&nbsp等特殊字符
        # text = re.sub(r"<a(.*?)>(.*?)</a>", '', text, 0, re.S)  # 去除链接标记
        text = re.sub(r'<a(.*?)>|</a>', self._link_mark, text, 0, re.I | re.S)  # 将<a>, </a>标记换为|ATAG|
        text = re.sub(r'<[^>]*?>', '', text, 0, re.I | re.S)  # 去除tag标记
        lines = text.split('\n')
        for lineIndex in range(len(lines)):  # 去除所有空白字符，包括\r, \n, \t, " "
            lines[lineIndex] = re.sub(r'\s+', '', lines[lineIndex])
        return lines


def str2dict(headers_raw):
    if headers_raw is None:
        return None
    headers = headers_raw.splitlines()
    headers_tuples = [header.split(':', 1) for header in headers]
    result_dict = {}
    for header_item in headers_tuples:
        if not len(header_item) == 2:
            continue
        item_key = header_item[0].strip()
        item_value = header_item[1].strip()
        result_dict[item_key] = item_value
    return result_dict


# 列表分组
def list_of_groups(init_list, children_list_len):
    list_of_groups = zip(*(iter(init_list),) * children_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % children_list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list


def get_column(response, xpath, str_add_head='', str_add_tail='', Auto_wash=True):
    if xpath:
        if isinstance(response, dict):
            return response.get(xpath)
        if isinstance(response, str):
            response = Selector(text=response)
        if isinstance(xpath, list):
            value = ''.join(xpath).replace(' ', '').replace('\r', '').replace('\n', '').replace('\xa0', '').replace(
                '\t', '')
            return value
        value_list = response.xpath(xpath).getall()
        if Auto_wash:
            result = []
            for value in value_list:
                value = value.replace(' ', '').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('\t',
                                                                                                               '').replace(
                    '\u3000', '')
                result.append(value)
            return str_add_head + ''.join(set(result)) + str_add_tail
        else:
            return str_add_head + ''.join(set(value_list)) + str_add_tail
    else:
        return None


def get_column_div_list(response, xpath):
    if isinstance(response, str):
        response = Selector(text=response)
    value_list = response.xpath(xpath)
    return value_list


def get_column_list(response, xpath, str_add_head='', str_add_tail='', Auto_wash=True):
    if isinstance(response, str):
        response = Selector(text=response)
    value_list = response.xpath(xpath).getall()
    if Auto_wash:
        value_new_list = []
        for value in value_list:
            value = value.replace(' ', '').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('\t', '')
            value_new_list.append(str_add_head + value + str_add_tail)
        return list(set(value_new_list))
    else:
        return value_list


def get_column_re_list(rule, text, str_add_head='', str_add_tail='', Auto_wash=True):
    value_list = re.findall(rule, text, re.S)
    print(value_list)
    if Auto_wash:
        value_new_list = []
        for value in value_list:
            value = value.replace(' ', '').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('\t', '')
            value_new_list.append(str_add_head + value + str_add_tail)
        return list(set(value_new_list))
    else:
        value_new_list = []
        for value in value_list:
            value_new_list.append(str_add_head + value + str_add_tail)
        return list(set(value_new_list))


def get_column_re(rule, text, str_add_head='', str_add_tail='', Auto_wash=True):
    value_list = re.findall(rule, text, re.S)
    if Auto_wash:
        value_new_list = []
        for value in value_list:
            value = value.replace(' ', '').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('\t', '')
            value_new_list.append(str_add_head + value + str_add_tail)
        return ''.join(list(set(value_new_list)))
    else:
        value_new_list = []
        for value in value_list:
            value_new_list.append(str_add_head + value + str_add_tail)
        return ''.join(list(set(value_new_list)))


def getYesterday(day=0):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=day)
    yesterday = today + oneday
    return yesterday

def get_md5_sz(url):
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

# url去重MD5
def get_md5(url):
    if isinstance(url, list) or isinstance(url, tuple) or isinstance(url, str):
        url = str(url)
    m = hashlib.md5()
    if isinstance(url, str):
        url = url.encode('utf-8')
    m.update(url)
    return m.hexdigest()

def get_md5_by_sql(sql, cursor, key):
    # key 代表sql中 字段名。
    try:
        cursor.execute(sql)
        rst = cursor.fetchone()
        md55 = rst[key]
        return md55
    except Exception as ex:
        raise Exception(ex)

# 字符串转元组
def str2tuple(str):
    return tuple(eval(str.split('(')[-1].split(')')[0]))

def cn2en(url):
    md = get_md5(url)[8:24].replace('0', 'g').replace('1', 'h').replace('2', 'i').replace('3', 'j').replace('4',
                                                                                                            'k').replace(
        '5', 'l').replace('6', 'm').replace('7', 'n').replace('8', 'o').replace('9', 'p')
    return md

def get_dict_key(dict, value):
    for i, j in dict.items():
        if j == value:
            return i

def collect_filename(path):
    filenames = listdir(path)
    return filenames


def running_days(amount=10, unit=3):
    """
    此for循环表示：往前推amount个三天;
    :param amount:
    :param unit:
    :return:
    """
    unit = unit - 1
    temp = 0
    for i in range(1, amount + 1):
        h = temp
        q = h + unit
        temp = q + 1
        searchDate = datetime.datetime.now() - datetime.timedelta(days=q)
        startdate = searchDate.strftime("%Y-%m-%d")
        enddate = datetime.datetime.now() - datetime.timedelta(days=h)
        if searchDate > enddate:
            raise Exception('12333')
        enddate = enddate.strftime("%Y-%m-%d")
        yield [startdate, enddate]


def partition_days(TimeStart=None, TimeEnd=None, number=None):
    # TimeStart='2018-08-16'
    # TimeEnd='2018-08-16'
    # number=2
    """
      方法含义：在时间区间划分多少分;

      :param amount:
      :param unit:
      :return:
      """
    TimeStart = arrow.get(TimeStart).datetime
    TimeEnd = arrow.get(TimeEnd).datetime
    days = TimeEnd - TimeStart
    days = days.days
    unit = int(math.ceil(days / float(number)))
    temp = 0
    for i in range(number):
        q = temp
        w = (i + 1) * unit
        temp = w + 1
        searchDate = TimeEnd - datetime.timedelta(days=0 + w)
        startdate = searchDate.strftime("%Y-%m-%d")
        enddate_ = TimeEnd - datetime.timedelta(days=0 + q)
        if searchDate > enddate_:
            raise Exception('12333')
        enddate = enddate_.strftime("%Y-%m-%d")
        if searchDate < TimeStart:
            startdate = TimeStart.strftime("%Y-%m-%d")
        yield [startdate, enddate]

def getAllName(messageContent):
    words = pseg.cut(messageContent)
    names = []
    for word, flag in words:
        # print('%s,%s' % (word, flag))
        if flag == 'nr':  # 人名词性为nr
            print(word, '*' * 50)
            names.append(word)
    return names

# 识别验证码或者电话号码
def image_recognize_url(url, max_lenth=None, max_try=10, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'}):
    n = 0
    while n < max_try:
        res = requests.get(url, headers=headers, timeout=5)
        image = BytesIO(res.content)
        image = Image.open(image)
        im = image.convert('L')
        text = pytesseract.image_to_string(im)
        if max_lenth and len(text) == max_lenth:
            return text
        elif not max_lenth:
            if text:
                return text
            else:
                print("识别失败")
        else:
            print("识别失败")
            n += 1
    if n == max_try:
        print("无法识别该验证码")
        return None

def image_recognize_path(image_path):
    im = Image.open('{}'.format(image_path))
    auth = pytesseract.image_to_string(im)
    return auth

def get_photo(url, image_path,
              headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'}):
    path = '/'.join(image_path.split('\\')[:-1])
    if not os.path.exists(path):
        os.makedirs(path)
        red_print("创建{}文件夹".format(path))
    res = requests.get(url, headers=headers, timeout=5)
    with open(image_path, 'wb')as f:
        f.write(res.content)
    red_print("{}download_success".format(image_path))


def get_pdf(url, image_path,
            headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'}, data={},
            proxies={}, type_way="get"):
    path = '/'.join(image_path.split('\\')[:-1])
    if not os.path.exists(path):
        os.makedirs(path)
        red_print("创建{}文件夹".format(path))
    if type_way == "post":
        res = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=5)
    else:
        res = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    with open(image_path, 'wb')as f:
        red_print("{} downloading...".format(image_path))
        for i in res.iter_content():
            f.write(i)
    red_print("{}download_success".format(image_path))
    return True

def get_item_field(items):
    red_print("复制item字段列表值")
    red_print('----------------------------------------------------------')
    for item in items.keys():
        item = '{} = scrapy.Field()'.format(item)
        print(item)
    red_print('----------------------------------------------------------')
    os._exit(0)


from selenium.webdriver.chrome.options import Options


def save_csv(keyword_list, path, item):
    """
    保存csv方法
    :param keyword_list: 保存文件的字段或者说是表头
    :param path: 保存文件路径和名字
    :param item: 要保存的字典对象
    :return:
    """
    try:
        # 第一次打开文件时，第一行写入表头
        if not os.path.exists(path):
            with open(path, "w", newline='', encoding='utf-8') as csvfile:  # newline='' 去除空白行
                writer = csv.DictWriter(csvfile, fieldnames=keyword_list)  # 写字典的方法
                writer.writeheader()  # 写表头的方法

        # 接下来追加写入内容
        with open(path, "a", newline='', encoding='utf-8') as csvfile:  # newline='' 一定要写，否则写入数据有空白行
            writer = csv.DictWriter(csvfile, fieldnames=keyword_list)
            writer.writerow(item)  # 按行写入数据
            print("^_^ write success")
    except:
        pass


def get_cookies(url, executable_path="E:\chrome download\chromedriver.exe", type="str", Evasion_detection=True):
    desired_capabilities = DesiredCapabilities.CHROME  # 设置这个选项，加载更快。
    desired_capabilities["pageLoadStrategy"] = "none"
    chrome_options = webdriver.ChromeOptions()  # 无界面模式的选项设置
    if Evasion_detection:
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 实现了规避监测
    else:
        chrome_options.add_argument('--headless')  # 用规避检测无法使用无头模式
    chrome_options.add_argument(
        'User-Agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"')
    browser = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
    browser.get(url)
    if Evasion_detection:
        time.sleep(5)
    else:
        time.sleep(1)
    if type == "page":
        return browser.page_source
    result_list = browser.get_cookies()
    if type == "str":
        cookie = ""
        for i in result_list:
            cookie = cookie + i["name"] + "=" + i["value"] + ";"
        return cookie[:-1]
    elif type == "dict":
        cookie_dict = {}
        for i in result_list:
            cookie_dict[i["name"]] = i["value"]
        return cookie_dict
    else:
        raise ValueError("please choice a type 'str' or 'dict'")


def excute_js(js_code_path, func, args):
    with open(js_code_path, 'r')as f:
        js_code = f.read()
    js_code = execjs.compile(js_code)
    result = js_code.call(func, args)
    return result


def write_file(path, value):
    with open(path, 'a')as f:
        if isinstance(value, dict):
            result = json.dumps(value, ensure_ascii=False)
            f.write(result)
        f.write(value)


def convert_removing_interference(image_path, value_px=130, image_show=True, save_image=False):
    # np.set_printoptions(threshold=np.inf) #全显示图片数组
    img = Image.open(image_path)
    img = img.convert("L")
    array_list = np.array(img)
    shape = array_list.shape
    array_list = array_list.tolist()
    new_list = []
    for list in array_list:
        for i in list:
            new_list.append(i)
    for i, value in enumerate(new_list):
        if value < value_px:
            new_list[i] = 0
    # print(new_list)
    result = np.reshape(new_list, shape)
    new_im = Image.fromarray(result)
    if image_show:
        new_im.show()
    if save_image:
        new_im.save(image_path.split('.')[0] + "_new." + image_path.split('.')[-1])


def more_process(num, func):
    for i in range(num):
        p = Process(target=func)
        p.start()


ip_list = []
start = time.time()


def get_ip():
    global ip_list, start
    if time.time() - start > 180 or not ip_list:
        while True:
            url_daili = 'http://api2.uuhttp.com:39002/index/api/return_data?mode=http&count=199&b_time=300&return_type=1&line_break=1&secert=MTUwMTE0MTAzMjA6Mjk3NWFiM2Q4N2U0MmE1OTdjYmE5NWM3NDlkNDEzMDY='
            res = requests.get(url_daili)
            ip_list = res.text.split('\r\n')
            start = time.time()
            if ip_list:
                break
    while True:
        ip = random.choice(ip_list).strip(' ')
        if ip:
            red_print("正在使用的代理IP为: {}".format(ip))
            # request.meta['proxy'] = 'http://elements:Elements-123.@' + ip + '/'
            proxies = {'http': ip, 'https': ip}
            return proxies


def my_request(conn, url, proxy=None, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
               , allow_status=[200], timeout=(5, 8), method='get', data=None, retry=3,
               timesleep=0, show_result=False, allow_redirects=False, verify=False,change_ip_times=5):
    request_count = 0
    status_code_not_allow = 0
    while True:
        if proxy and status_code_not_allow > change_ip_times:
            proxy = get_ip()
        try:
            if method.lower() == 'get':
                response = conn.get(url=url, headers=headers, params=data, timeout=timeout,
                                    allow_redirects=allow_redirects,
                                    proxies=proxy, verify=verify)
                print("响应状态：{} 访问url：{}".format(response.status_code, url))
                if response.status_code in allow_status:
                    return {'res':response,'conn':conn,'proxy':proxy}
                if response.status_code not in allow_status:
                    status_code_not_allow += 1
                if proxy and response.status_code == 403:
                    proxy = get_ip()
                if show_result:
                    print(response.text)

            elif method.lower() == 'post':
                response = conn.post(url=url, headers=headers, params=data, timeout=timeout,
                                     allow_redirects=allow_redirects,
                                     proxies=proxy, verify=verify)
                print("响应状态：{} 访问url：{} 请求参数：{}".format(response.status_code, url, data))
                if response.status_code in allow_status:
                    return {'res': response, 'conn': conn, 'proxy': proxy}
                if response.status_code not in allow_status:
                    status_code_not_allow += 1
                if proxy and response.status_code == 403:
                    proxy = get_ip()
                if show_result:
                    print(response.text)
        except:
            print("本次请求失败,重试次数剩余：{}".format(retry-request_count))
            proxy = get_ip()
        request_count += 1
        time.sleep(timesleep)
        if request_count > retry - 1:
            red_print("请求失败 request_way：{} URL：{} data：{} retry_times：{}".format(method,url,data,retry))
            return

# 特征提取，获取图像二值化数学值
def getBinaryPix(im):
    im = Image.open(im)
    img = np.array(im)
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if (img[i, j] <= 128):
                img[i, j] = 0
            else:
                img[i, j] = 1
    binpix = np.ravel(img)
    return binpix


# ''' 根据该像素周围点为黑色的像素数（包括本身）来判断是否把它归属于噪声，如果是噪声就将其变为白色'''
# '''
# 	input:  img:二值化图
# 			number：周围像素数为黑色的小于number个，就算为噪声，并将其去掉，如number=6，
# 			就是一个像素周围9个点（包括本身）中小于6个的就将这个像素归为噪声
# 	output：返回去噪声的图像
# '''
def noise_removal(img_dir, save_dir=''):
    img_name = os.listdir(img_dir)  # 列出文件夹下所有的目录与文件
    for i in range(len(img_name)):
        _name = img_name[i]
        path = os.path.join(img_dir, _name)
        im = Image.open(path)
        pix = im.load()
        width = im.size[0]
        height = im.size[1]
        for x in range(width):
            for y in range(height):
                r, g, b = pix[x, y]
                r0, r1, r2 = r, g, b
                if r0 + r1 + r2 >= 400 or r0 >= 250 or r1 >= 250 or r2 >= 250:
                    im.putpixel((x, y), (255, 255, 255))
                elif x == 0 or x == width - 1 or y == 0 or y == height - 1:
                    im.putpixel((x, y), (255, 255, 255))
                else:
                    im.putpixel((x, y), (0, 0, 0))
        if save_dir:
            if not os._exists(save_dir):
                os.mkdir(save_dir)
            im.save(r'{}\new_{}'.format(save_dir, _name))
        else:
            im.save(r'{}\new_{}'.format(img_dir, _name))
            print(path)
    print("图片预处理完成！")


def get_xls_data(file_path, nrow=1, ncol=1, value="all_row", sheet='Sheet1'):
    # 文件路径的中文转码，如果路径非中文可以跳过
    # file_path = file_path.decode('utf-8')
    # 获取数据
    data = xlrd.open_workbook(file_path)
    # 获取sheet 此处有图注释（见图1）
    table = data.sheet_by_name(sheet)
    red_print("当前获取{}表格内容数据\n".format(sheet))
    # 获取总行数
    nrows = table.nrows
    # 获取总列数
    ncols = table.ncols
    if value == "nrow":
        rowvalue = table.row_values(nrow)
        return rowvalue
    # 获取一列的数值，例如第6列
    elif value == "ncol":
        col_values = table.col_values(ncol)
        return col_values
    # 获取一个单元格的数值，例如第5行第6列
    elif value == "cell":
        cell_value = table.cell(nrow, ncol).value
        return cell_value
    # 获取所有行
    elif value == "all_row":
        result_list_nrow = []
        for i in range(nrows):
            rowvalue = table.row_values(i)
            result_list_nrow.append(rowvalue)
        return result_list_nrow
    # 获取所有列
    elif value == "all_col":
        result_list_ncol = []
        for i in range(ncols):
            col_values = table.col_values(i)
            result_list_ncol.append(col_values)
        return result_list_ncol
    else:
        red_print(
            "请选择value值模式:{\n'all_row':'取出全部行',\n'all_col':'取出全部列',\n'nrow':'取出指定行',\n'n_col':'取出指定列',\n'cell':'取出指定单元格'}")
        return None


province = [
    '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南',
    '四川', '贵州', '云南', '陕西', '甘肃', '青海', '北京', '天津', '上海', '重庆', '内蒙古', '广西', '宁夏', '新疆', '西藏',
]
city0 = ['北京', '上海', '广州', '深圳']
city1 = ['成都', '杭州', '重庆', '武汉', '苏州', '西安', '天津', '南京', '郑州', '长沙', '沈阳', '青岛', '宁波', '东莞', '无锡']
city2 = [
    '昆明', '大连', '厦门', '合肥', '佛山', '福州', '哈尔滨', '济南', '温州', '长春', '石家庄', '常州', '泉州', '南宁', '贵阳', '南昌', '南通', '金华', '徐州',
    '太原', '嘉兴', '烟台', '惠州', '保定', '台州', '中山', '绍兴', '乌鲁木齐', '潍坊', '兰州',
]
city3 = [
    '珠海', '镇江', '海口', '扬州', '临沂', '洛阳', '唐山', '呼和浩特', '盐城', '汕头', '廊坊', '泰州', '济宁', '湖州', '江门', '银川', '淄博', '邯郸', '芜湖',
    '漳州', '绵阳', '桂林', '三亚', '遵义', '咸阳', '上饶', '莆田', '宜昌', '赣州', '淮安', '揭阳', '沧州', '商丘', '连云港', '柳州', '岳阳', '信阳', '株洲',
    '衡阳', '襄阳', '南阳', '威海', '湛江', '包头', '鞍山', '九江', '大庆', '许昌', '新乡', '宁德', '西宁', '宿迁', '菏泽', '蚌埠', '邢台', '铜陵', '阜阳',
    '荆州', '驻马店', '湘潭', '滁州', '肇庆', '德阳', '曲靖', '秦皇岛', '潮州', '吉林', '常德', '宜春', '黄冈',
]
city4 = [
    '舟山市', '泰安市', '孝感市', '鄂尔多斯市', '开封市', '南平市', '齐齐哈尔市', '德州市', '宝鸡市', '马鞍山市', '郴州市', '安阳市', '龙岩市', '聊城市', '渭南市', '宿州市',
    '衢州市', '梅州市', '宣城市', '周口市', '丽水市', '安庆市', '三明市', '枣庄市', '南充市', '淮南市', '平顶山市', '东营市', '呼伦贝尔市', '乐山市', '张家口市', '清远市',
    '焦作市', '河源市', '运城市', '锦州市', '赤峰市', '六安市', '盘锦市', '宜宾市', '榆林市', '日照市', '晋中市', '怀化市', '承德市', '遂宁市', '毕节市', '佳木斯市',
    '滨州市', '益阳市', '汕尾市', '邵阳市', '玉林市', '衡水市', '韶关市', '吉安市', '北海市', '茂名市', '延边朝鲜族自治州', '黄山市', '阳江市', '抚州市', '娄底市', '营口市',
    '牡丹江市', '大理白族自治州', '咸宁市', '黔东南苗族侗族自治州', '安顺市', '黔南布依族苗族自治州', '泸州市', '玉溪市', '通辽市', '丹东市', '临汾市', '眉山市', '十堰市', '黄石市',
    '濮阳市', '亳州市', '抚顺市', '永州市', '丽江市', '漯河市', '铜仁市', '大同市', '松原市', '通化市', '红河哈尼族彝族自治州', '内江市', '新余市',
]
city5 = [
    '长治市', '荆门市', '梧州市', '拉萨市', '汉中市', '四平市', '鹰潭市', '广元市', '云浮市', '葫芦岛市', '本溪市', '景德镇市', '六盘水市', '达州市', '铁岭市', '钦州市',
    '广安市', '保山市', '自贡市', '辽阳市', '百色市', '乌兰察布市', '普洱市', '黔西南布依族苗族自治州', '贵港市', '萍乡市', '酒泉市', '忻州市', '天水市', '防城港市', '鄂州市',
    '锡林郭勒盟', '白山市', '黑河市', '克拉玛依市', '临沧市', '三门峡市', '伊春市', '鹤壁市', '随州市', '晋城市', '文山壮族苗族自治州', '巴彦淖尔市', '河池市', '凉山彝族自治州',
    '乌海市', '楚雄彝族自治州', '恩施土家族苗族自治州', '吕梁市', '池州市', '西双版纳傣族自治州', '延安市', '雅安市', '巴中市', '双鸭山市', '攀枝花市', '阜新市', '兴安盟',
    '张家界市', '昭通市', '海东市', '安康市', '白城市', '朝阳市', '绥化市', '淮北市', '辽源市', '定西市', '吴忠市', '鸡西市', '张掖市', '鹤岗市', '崇左市',
    '湘西土家族苗族自治州', '林芝市', '来宾市', '贺州市', '德宏傣族景颇族自治州', '资阳市', '阳泉市', '商洛市', '陇南市', '平凉市', '庆阳市', '甘孜藏族自治州', '大兴安岭地区',
    '迪庆藏族自治州', '阿坝藏族羌族自治州', '伊犁哈萨克自治州', '中卫市', '朔州市', '儋州市', '铜川市', '白银市', '石嘴山市', '莱芜市', '武威市', '固原市', '昌吉回族自治州',
    '巴音郭楞蒙古自治州', '嘉峪关市', '阿拉善盟', '阿勒泰地区', '七台河市', '海西蒙古族藏族自治州', '塔城地区', '日喀则市', '昌都市', '海南藏族自治州', '金昌市', '哈密市',
    '怒江傈僳族自治州', '吐鲁番市', '那曲地区', '阿里地区', '喀什地区', '阿克苏地区', '甘南藏族自治州', '海北藏族自治州', '山南市', '临夏回族自治州', '博尔塔拉蒙古自治州', '玉树藏族自治州',
    '黄南藏族自治州', '和田地区', '三沙市', '克孜勒苏柯尔克孜自治州', '果洛藏族自治州',
]
department = [
    '外交部', '国防部', '国家发展和改革委员会', '教育部', '科学技术部', '工业和信息化部', '国家民族事务委员会', '公安部', '国家安全部', '民政部', '司法部', '财政部',
    '人力资源和社会保障部', '自然资源部', '生态环境部', '住房和城乡建设部', '交通运输部', '水利部', '农业农村部', '商务部', '文化和旅游部', '国家卫生健康委员会', '退役军人事务部',
    '应急管理部', '人民银行', '审计署', '国家语言文字工作委员会', '国家外国专家局', '国家航天局', '国家原子能机构', '国家海洋局', '国家核安全局', '国务院国有资产监督管理委员会', '海关总署',
    '国家税务总局', '国家市场监督管理总局', '国家广播电视总局', '国家体育总局', '国家统计局', '国家国际发展合作署', '国家医疗保障局', '国务院参事室', '国家机关事务管理局',
    '国家认证认可监督管理委员会', '国家标准化管理委员会', '国家新闻出版署（国家版权局）', '国家宗教事务局', '国务院港澳事务办公室', '国务院研究室', '国务院侨务办公室', '国务院台湾事务办公室',
    '国家互联网信息办公室', '国务院新闻办公室', '新华通讯社', '中国科学院', '中国社会科学院', '中国工程院', '国务院发展研究中心', '中央广播电视总台', '中国气象局', '中国银行保险监督管理委员会',
    '中国证券监督管理委员会', '国家行政学院', '国家信访局', '国家粮食和物资储备局', '国家能源局', '国家国防科技工业局', '国家烟草专卖局', '国家移民管理局', '国家林业和草原局', '国家铁路局',
    '中国民用航空局', '国家邮政局', '国家文物局', '国家中医药管理局', '国家煤矿安全监察局', '国家外汇管理局', '国家药品监督管理局', '国家知识产权局', '出入境管理局', '国家公园管理局',
    '国家公务员局', '国家档案局', '国家保密局', '国家密码管理局',
]
Over_the_Third_tier_Cities = city0 + city1 + city2
Over_the_Third_tier_Cities_and_province = list(set(province + city0 + city1 + city2))

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
number_string = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
Punctuation = ["`", "·", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "（", "）", "-", "—", "_", "=", "+", "{",
               "}", "[", "]", "【", "】", "\\", "、", "|", "；", ";", "：", ":", "'", '"', "‘", "’", '“', "”", ",", "，", ".",
               "。", "<", ">", "《", "》", "/", "？", "?"]
ZhEnLetterTable = [
    ("(", "（",), (")", "）"), ("０", "0"), ("１", "1"), ("２", "2"),
    ("３", "3"), ("４", "4"), ("５", "5"), ("６", "6"), ("７", "7"), ("８", "8"), ("９", "9"), ("ａ", "a"),
    ("ｂ", "b"), ("ｃ", "c"), ("ｄ", "d"), ("ｅ", "e"), ("ｆ", "f"), ("ｇ", "g"), ("ｈ", "h"), ("ｉ", "i"),
    ("ｊ", "j"), ("ｋ", "k"), ("ｌ", "l"), ("ｍ", "m"), ("ｎ", "n"), ("ｏ", "o"), ("ｐ", "p"), ("ｑ", "q"),
    ("ｒ", "r"), ("ｓ", "s"), ("ｔ", "t"), ("ｕ", "u"), ("ｖ", "v"), ("ｗ", "w"), ("ｘ", "x"), ("ｙ", "y"),
    ("ｚ", "z"), ("Ａ", "A"), ("Ｂ", "B"), ("Ｃ", "C"), ("Ｄ", "D"), ("Ｅ", "E"), ("Ｆ", "F"), ("Ｇ", "G"),
    ("Ｈ", "H"), ("Ｉ", "I"), ("Ｊ", "J"), ("Ｋ", "K"), ("Ｌ", "L"), ("Ｍ", "M"), ("Ｎ", "N"), ("Ｏ", "O"),
    ("Ｐ", "P"), ("Ｑ", "Q"), ("Ｒ", "R"), ("Ｓ", "S"), ("Ｔ", "T"), ("Ｕ", "U"), ("Ｖ", "V"), ("Ｗ", "W"),
    ("Ｘ", "X"), ("Ｙ", "Y"), ("Ｚ", "Z")
]

baijiaxing = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
              '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
              '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
              '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
              '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
              '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
              '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
xing = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何', '吕',
        '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛',
        '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉',
        '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康',
        '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝',
        '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵',
        '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '钟', '徐', '邱', '骆', '高', '夏',
        '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗',
        '丁', '宣', '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆',
        '荣', '翁', '荀', '羊', '於', '惠', '甄', '麴', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫',
        '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇',
        '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司', '韶', '郜', '黎', '蓟', '薄',
        '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '欎', '胥', '能',
        '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '舄', '璩', '桑', '桂',
        '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连',
        '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘',
        '匡', '国', '文', '寇', '广', '禄', '阙', '东', '殴', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾',
        '敖', '融', '冷', '訾', '辛', '阚', '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相',
        '查', '後', '荆', '红', '游', '竺', '权', '逯', '盖', '益', '桓', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方',
        '赫连', '皇甫', '尉迟', '公羊', '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '钟离', '宇文',
        '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空', '亓官', '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正', '壤驷', '公良',
        '拓跋', '夹谷', '宰父', '谷梁', '晋', '楚', '闫', '法', '汝', '鄢', '涂', '钦', '段干', '百里', '东郭', '南门', '呼延', '归', '海', '羊舌',
        '微生', '岳', '帅', '缑', '亢', '况', '后', '有', '琴', '梁丘', '左丘', '东门', '西门', '商', '牟', '佘', '佴', '伯', '赏', '南宫', '墨',
        '哈', '谯', '笪', '年', '爱', '阳', '佟',
        '付', '仝', '代', '令', '任', '但', '何', '欧', '佘', '余', '信', '修',
        '王', '李', '张', '刘', '陈', '杨', '黄', '吴', '赵', '周', '徐', '孙', '马', '朱', '胡', '林', '郭', '何', '高', '罗', '郑', '梁',
        '谢', '宋', '唐', '许', '邓', '冯', '韩', '曹', '曾', '彭', '萧', '蔡', '潘', '田', '董', '袁', '于', '余', '叶', '蒋', '杜', '苏',
        '魏', '程', '吕', '丁', '沈', '任', '姚', '卢', '傅', '钟', '姜', '崔', '谭', '廖', '范', '汪', '陆', '金', '石', '戴', '贾', '韦',
        '夏', '邱', '方', '侯', '邹', '熊', '孟', '秦', '白', '江', '阎', '薛', '尹', '段', '雷', '黎', '史', '龙', '陶', '贺', '顾', '毛',
        '郝', '龚', '邵', '万', '钱', '严', '赖', '覃', '洪', '武', '莫', '孔', '汤', '向', '常', '温', '康', '施', '文', '牛', '樊', '葛',
        '邢', '安', '齐', '易', '乔', '伍', '庞', '颜', '倪', '庄', '聂', '章', '鲁', '岳', '翟', '殷', '詹', '申', '欧', '耿', '关', '兰',
        '焦', '俞', '左', '柳', '甘', '祝', '包', '宁', '尚', '符', '舒', '阮', '柯', '纪', '梅', '童', '凌', '毕', '单', '季', '裴', '霍',
        '涂', '成', '苗', '谷', '盛', '曲', '翁', '冉', '骆', '蓝', '路', '游', '辛', '靳', '欧', '管', '柴', '蒙', '鲍', '华', '喻', '祁',
        '蒲', '房', '滕', '屈', '饶', '解', '牟', '艾', '尤', '阳', '时', '穆', '农', '司', '卓', '古', '吉', '缪', '简', '车', '项', '连',
        '芦', '麦', '褚', '娄', '窦', '戚', '岑', '景', '党', '宫', '费', '卜', '冷', '晏', '席', '卫', '米', '柏', '宗', '瞿', '桂', '全',
        '佟', '应', '臧', '闵', '苟', '邬', '边', '卞', '姬', '师', '和', '仇', '栾', '隋', '商', '刁', '沙', '荣', '巫', '寇', '桑', '郎',
        '甄', '丛', '仲', '虞', '敖', '巩', '明', '佘', '池', '查', '麻', '苑', '迟', '邝', '官', '封', '谈', '匡', '鞠', '惠', '荆', '乐',
        '冀', '郁', '胥', '南', '班', '储', '原', '栗', '燕', '楚', '鄢', '劳', '谌', '奚', '皮', '粟', '冼', '蔺', '楼', '盘', '满', '闻',
        '位', '厉', '伊', '仝', '区', '郜', '海', '阚', '花', '权', '强', '帅', '屠', '豆', '朴', '盖', '练', '廉', '禹', '井', '祖', '漆',
        '巴', '丰', '支', '卿', '国', '狄', '平', '计', '索', '宣', '晋', '相', '初', '门', '云', '容', '敬', '来', '扈', '晁', '芮', '都',
        '普', '阙', '浦', '戈', '伏', '鹿', '薄', '邸', '雍', '辜', '羊', '阿', '乌', '母', '裘', '亓', '修', '邰', '赫', '杭', '况', '那',
        '宿', '鲜', '印', '逯', '隆', '茹', '诸', '战', '慕', '危', '玉', '银', '亢', '嵇', '公', '哈', '湛', '宾', '戎', '勾', '茅', '利',
        '於', '呼', '居', '揭', '干', '但', '尉', '冶', '斯', '元', '束', '檀', '衣', '信', '展', '阴', '昝', '智', '幸', '奉', '植', '衡',
        '富', '尧', '闭', '由',
        ]
ming = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地',
        '为', '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自',
        '以', '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都',
        '好', '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开',
        '美', '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意',
        '动', '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯',
        '知', '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正',
        '感', '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果',
        '走', '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真',
        '打', '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界',
        '门', '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性',
        '马', '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让',
        '母', '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英',
        '军', '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快',
        '原', '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条',
        '呢', '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片',
        '罗', '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合',
        '反', '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运',
        '及', '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司',
        '巴', '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形',
        '影', '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈',
        '容', '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计',
        '您', '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻',
        '统', '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示',
        '愿', '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社',
        '算', '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息',
        '功', '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图',
        '具', '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引',
        '食', '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试',
        '怀', '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除',
        '跑', '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳',
        '验', '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿',
        '睡', '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店',
        '否', '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河',
        '续', '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪',
        '索', '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族',
        '低', '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅',
        '街', '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀',
        '律', '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职',
        '属', '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉',
        '遗', '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳',
        '差', '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府',
        '压', '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童',
        '顶', '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯',
        '巨', '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层',
        '付', '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀',
        '营', '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊',
        '降', '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙',
        '杰', '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡',
        '预', '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误', '乾',
        '坤']


