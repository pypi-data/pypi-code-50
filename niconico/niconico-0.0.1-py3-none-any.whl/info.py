#coding=utf-8

# import logging
# logging.basicConfig(filename='logging.log',
#                     format='%(asctime)s %(message)s',
#                     filemode="w", level=logging.DEBUG)


#  更新：
#  1、user_bilibili的在线更新和导出完成了，还缺少video_bilibili.
#
#
#
#
#
#
#
#
#

loginParam={
    'com': {
        'mid': 37663924,
        'jsonp': 'jsonp',
    },
    'vcom': {
        'vmid': 37663924,
        'jsonp': 'jsonp',
    },
    'search': {
        'pn': 1,
        'ps': 25,
        'mid': 37663924,
        'jsonp': 'jsonp',
    },
    'article': {
        'mid': 37663924,
        'pn': 1,
        'jsonp': 'jsonp',
    },
    'album': {
        'mid': 37663924,
        'ps': 10,
        'jsonp': 'jsonp',
    },
}

loginUrls =  {
    'proxyWeb': 'https://www.xicidaili.com/nn/',
    'proxies': {
        'http': 'http://104.224.154.185:8118',
        'https': 'https://104.224.154.185:8118',
    },
    'accinfo':'https://api.bilibili.com/x/space/acc/info?',
    'toparc':'https://api.bilibili.com/x/space/top/arc?',
    'masterpiece': 'https://api.bilibili.com/x/space/masterpiece?',
    'search': 'https://api.bilibili.com/x/space/arc/search?',
    'rooom': 'https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?',
    'rank': 'https://elec.bilibili.com/api/query.rank.do?',
    'article': 'https://api.bilibili.com/x/space/article?',
    'album': 'https://api.bilibili.com/x/space/album/index?',
    'upstat': 'https://api.bilibili.com/x/space/upstat?',
    'stat': 'https://api.bilibili.com/x/relation/stat?',
    'navnum': 'https://api.bilibili.com/x/space/navnum?'

}

loginHeaders = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'api.bilibili.com',
    'Origin': 'https://www.bilibili.com',
    # 'Referer': 'https://www.bilibili.com/video/' + str(i) + '?spm_id_from=333.338.recommend_report.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36',
}

loginCookie='buvid3=E7F541F8-384E-41C4-836B-ED1C8DF1234947188infoc; sid=jp20sj8b; rpdid=kwxoilkilwdosskwlomqw; LIVE_BUVID=AUTO2015530935579156; stardustvideo=1; CURRENT_FNVAL=16; INTVER=1; _uuid=64C277E1-7165-4D6E-8D8F-ED242DFB442557392infoc; DedeUserID=53178025; DedeUserID__ckMd5=81f4f87e08c1a74a; SESSDATA=bc87c7f6%2C1585472965%2C08606d21; bili_jct=e0cd73565eabbac8286f98044e20aca0; bp_t_offset_53178025=360960918554747824'
