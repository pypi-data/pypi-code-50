from pyquery.pyquery import PyQuery
import urllib.parse as up
import requests
import re

NW = re.compile(r'\W')

def GetLinks(url, proxy=None, text=False):
    doc = None
    basehost = None
    if url.startswith("http"):
        basehost = up.urlsplit(url).hostname 
        sess = requests.Session()
        if proxy != None:
            sess.proxies['http'] = sess.proxies['https'] = proxy
        doc = PyQuery(sess.get(url).text)
    else:
        if text == False:
            with open(url) as fp:
                text = fp.read()
        else:
            text = url
        doc = PyQuery(text)
    if doc == None:
        doc = PyQuery("<html></html>")
    for l in doc("a[href]"):
        link = l.attrib['href']
        if link  == "#":continue
        if link.startswith("http") or link.startswith("//"):
            if not text:
                res = up.urlsplit(url)
                if basehost != None and res.hostname != basehost:continue
        yield link,l.text


class Url(str):
    urls = {}
    def __init__(self, url):
        self.l = len(url)
        self.url = url
        self.no_w = set(NW.findall(url))
        self.structs = NW.split(url)
        self.w = set(url)
        self.host = up.urlsplit(url).hostname
        self.rank = len(self.structs)
        # self._like = []
        Url.urls[url] = self
    
    def __sub__(self, other):
        if isinstance(other, str):
            other = Url(other)
        if self.url == other.url:
            return 0
        
        sam = 0
        # if self.url.startswith("http"):
        #     url = self.url.split("//")[1]
        # else:
        #     url = self.url
        
        # if other.url.startswith("http"):
        #     otherurl = other.url.split("//")[1]
        # else:
        #     otherurl = other.url
        
        # mm = min(len(url), len(otherurl))
        mm = min(self.l, other.l)
        
        for i in range(mm):
            if self.url[i] != other.url[i]:
                break
            sam +=1
        
        # print(sam)
        score = 1 - (sam / max(self.l , other.l))
        if score > 0.4:
            mms = min(len(self.structs), len(other.structs))
            ssam = 0
            for i in range(mms):
                if self.structs[i] == other.structs[i]:
                    ssam += 1
                else:
                    ssam += (len(set(self.structs[i]) &  set(other.structs[i])) / len(set(self.structs[i]) |  set(other.structs[i])))
            score = 1 - (ssam / max(len(self.structs), len(other.structs)))
        # print("1",score)
        ld = abs(self.l - other.l)
        # print("scrore:", score,end=" => ")
        score += (ld**3) / max(self.l, other.l)
        # print("scrore:", score)
        # print("2",score)
        if self.l < 10:
            score += 0.2
            # print("3",score)
        
        if self.no_w == other.no_w:
            score -= 0.1
            # print("4",score)
        else:
            mm_no_w = min(len(self.no_w), len(other.no_w))
            sam = 0
            for i in range(mm_no_w):
                if list(self.no_w)[i] != list(other.no_w)[i]:    
                    break
                sam +=1
            score += (1-sam / len(self.no_w | other.no_w))
            # print("5",score)
        return score
        
    @classmethod
    def group(cls, urls, distance=0.2):
        urls_g = dict()
        # last = None
        for i in urls:
            ui = Url(i)
            urls_g[i] = set()
            for ii in urls:
                ui2 = Url(ii)

                d = ui - ui2 
                if d < distance:
                    urls_g[i].add(ui2)
            if len(urls_g[i]) < 3:
                del urls_g[i]

        while 1:
            found = None
            for k,v in urls_g.items():
                for k2, v2 in urls_g.items():
                    if k2 in v and k2 != k:
                        v |= v2
                        found = k2
                        break
                        
            if found:
                del urls_g[found]
            else:
                break
        
        return list(urls_g.values())
    
    @classmethod
    def Index(cls, url, distance=0.2, rank=2):
        ls = []
        if not isinstance(url, (list, tuple)):
            for l  in GetLinks(url):
                if isinstance(l, (list, tuple)):
                    l = l[0]
                
                ls.append(l)
        else:
            ls = url
        res = cls.group(ls, distance=distance)
        def _key(i):
            t = len(i) 
            # print(list(i)[0].rank)
            
            t += (list(i)[0].rank  * 20)
            # print(t)
            
            return t

        res =  sorted(res, key=_key, reverse=True)
        if rank < len(res):
            return res[:rank]
        return res