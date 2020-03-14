import time
import sqlite3
import requests
from bs4 import BeautifulSoup


def getsongtype():
    songtype = []
    url = "http://www.9ku.com/"
    wbdata = requests.get(url).content
    soup = BeautifulSoup(wbdata, "lxml")

    data1 = soup.select(".indexTagHd li")
    data2 = soup.select(".indexTagBd .indexTagItem")
    for idx, item in enumerate(data1):
        data11 = data1[idx].text  # item.text #一级名称
        data22 = data2[idx].select("li")
        for idx2, item2 in enumerate(data22):
            data222 = item2.select("a")[0]
            data222name = data222.text  # 二级名称
            data222href = data222.attrs["href"]
            songtype.append(
                {"type1": data11, "type2": data222name, "href": data222href}
            )
    return songtype


def getsongs(url):
    try:
        if "http://" in url:
            url = url
        else:
            url = "http://www.9ku.com" + url
        # url = 'http://www.9ku.com/laoge/500shou.htm' .musicList
        # http://www.9ku.com/zhuanji/151.htm  .intro_item
        wbdata = requests.get(url).content
        soup = BeautifulSoup(wbdata, "lxml")
        # print(soup)
        # 歌曲
        songs = soup.select(".musicList li,.intro_item li")  # .songList li,

        # songs = soup.select('.intro_item li')

        # print(len(songs))  # 496
        songlist = []
        for idx, song in enumerate(songs):
            songinfo = song.select("a")[0]
            if "target" in songinfo.attrs:
                songname = songinfo.text
                songhref = songinfo.attrs["href"]
                songlist.append({"songname": songname, "songhref": songhref})
        return songlist
    except BaseException as ex:
        print(ex)
        return []


# 查询辅助方法-转db


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# 通用建表


def createdb(dbname, tbname, fields):
    conn = sqlite3.connect(dbname + ".db")
    try:
        # 表名,主键
        sqlstr = (
            "CREATE TABLE IF NOT EXISTS %s (%s_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
            % (tbname, tbname)
        )
        #
        if type(fields) == list:
            for field in fields:
                sqlstr += field + " TEXT,"
        #
        if type(fields) == dict:
            for key, value in fields.items():
                if value in ["TEXT", "INTEGER", "DATETIME"]:
                    sqlstr += key + " " + value + ","
                else:
                    print("不支持类型:" + value + ",字段:" + key)
        # 添加备注
        sqlstr += "remark TEXT,"
        sqlstr += "createone INTEGER,"
        sqlstr += "createtime DATE,"
        sqlstr += "updateone INTEGER"
        sqlstr += "updatetime DATE"
        sqlstr += ")"
        print(sqlstr)
        conn.execute(sqlstr)
    except Exception as inst:
        print("Create table %s failed:" % (tbname), inst)
        return False
    conn.commit()
    conn.close()


# 通用查询


def querydb(dbname, tbname, fields, data):
    conn = sqlite3.connect(dbname + ".db")
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    sqlstr = "select * from %s" % (tbname)
    # wherestr = ""
    wherearr = []
    # for index, item in enumerate(fields):
    for key, value in fields.items():
        if value in ["=", "!=", ">", ">=", "<", "<="]:
            # wherestr += key + value + "'{" + key + "}'"
            # wherearr += key + value + ":" + key + ""
            wherearr.append(key + value + ":" + key + "")
        else:
            print("不支持的查询条件:%s" % (value))

    if len(wherearr) > 0:
        sqlstr += " where " + " ".join(wherearr)

    # execsql = sqlstr.format(**data)
    # cursor.execute(execsql)
    cursor.execute(sqlstr, data)
    return cursor.fetchall()


# 通用插入


def insertdb(dbname, tbname, fields, list, remark):
    conn = sqlite3.connect(dbname + ".db")
    try:
        # 表名,主键
        fieldlist = []
        valuelist = []
        #
        if type(fields).__name__ == "list":
            for field in fields:
                fieldlist.append("%s" % (field))
                valuelist.append("'{%s}'" % (field))
        #
        if type(fields).__name__ == "dict":
            for key, value in fields.items():
                fieldlist.append("%s" % (key))
                valuelist.append("'{%s}'" % (value))

        # 添加备注
        fieldlist.append("remark")
        valuelist.append("'%s'" % (remark))
        # 添加日期
        fieldlist.append("createtime")
        valuelist.append(
            "'%s'" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        )
        # 添加备注
        sqlstr = " insert into %s(%s) values(%s)" % (
            tbname,
            ",".join(fieldlist),
            ",".join(valuelist),
        )
        # print(sqlstr, list)

        for index, item in enumerate(list):
            execsql = sqlstr.format(**item)
            conn.execute(execsql)
        conn.commit()
    except Exception as inst:
        print("Create table %s failed:" % (tbname), inst)
        return False
    conn.close()


def updatedb(dbname, tbname, fields, list, remark):
    conn = sqlite3.connect(dbname + ".db")
    try:
        # 表名,主键
        valuelist = []
        #
        if type(fields).__name__ == "list":
            for field in fields:
                valuelist.append("%s='{%s}'" % (field, field))
        #
        if type(fields).__name__ == "dict":
            for key, value in fields.items():
                valuelist.append("%s='{%s}'" % (key, value))

        # 添加备注
        if remark != "":
            valuelist.append("remark='{%s}'" % (remark))
        # 添加日期
        valuelist.append(
            "updatetime='%s'" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        )
        # 添加备注
        sqlstr = " update %s set %s where %s_id={id}" % (
            tbname,
            ",".join(valuelist),
            tbname,
        )
        # print(sqlstr, list)

        for index, item in enumerate(list):
            execsql = sqlstr.format(**item)
            print(execsql, item)
            conn.execute(execsql)
        conn.commit()
    except Exception as inst:
        print("update table [%s] failed:" % (tbname), inst)
        return False
    conn.close()


def deletedb(dbname, tbname, id):
    return 0


def execdb(dbname, tbname, fields, id, list):
    return 0


# 歌曲类型,爬取257条,已完成
# songtype = getsongtype()
# print(songtype)
# createdb('song', 'songtype', ['type1', 'type2', 'href', 'songnum'])
# insertdb('song', 'songtype', ['type1', 'type2', 'href'], songtype)


# 创建歌曲表和歌曲日志表
# createdb("song", "songlist", ["type1", "type2", "href", "songname", "songhref"])
# createdb("song", "songlist_log", ["type1", "type2", "href", "sl"])

# 查询类型表
# songtypelist = querydb("song", "songtype", {"sl": "="}, {"sl": 0})
# 查询歌曲日志表
# songtypelist = querydb("song", "songlist_log", {"sl": "="}, {"sl": 0})
# print(songtypelist)
# print(len(songtypelist))

# 添加
# for songtype in songtypelist:
#     songlist = getsongs(songtype["href"])
# print(songtype['href'], len(songlist))
#     songtype["sl"] = len(songlist)
#     for song in songlist:
#         song = {**song, **songtype}
#         insertdb(
#             "song",
#             "songlist",
#             ["type1", "type2", "href", "songname", "songhref"],
#             [song],
#             "www.9ku.com",
#         )
#     insertdb(
#         "song",
#         "songlist_log",
#         ["type1", "type2", "href", "sl"],
#         [songtype],
#         "www.9ku.com",
#     )


# 更新
updatedb("song", "songtype", {"songnum": "songnum"}, [{"id": 1, "songnum": 1}], "")

# songlist = getsongs()
# print(songlist)
# insertdb('song', 'songlist', ['songname', 'songhref'], songlist)

# http://www.9ku.com/play/469728.htm#歌词 #lrctext .text
# http://www.9ku.com/html/dingcai/47/469728.js
# cai: "21578"
# ding: "105684"
# pingfen: "83.04"

# http://www.9ku.com/html/playjs/470/469728.js
# gsid: "9255"
# gspic: "http://aliyunimg.9ku.com/pic/gstx/1/9255.jpg"
# id: "469728"
# id2: null
# m4a: "http://mp3.9ku.com/m4a/469728.m4a"
# mname: "哥有老婆"
# singer: "纪晓斌"
# status: "0"
# wma: "http://mp3.9ku.com/hot/2012/08-06/469728.mp3"
# zjid: "140465"
# zjname: "哥有老婆"
# zjpic: "http://aliyunimg.9ku.com/pic/zjpic/15/140465.jpg"
