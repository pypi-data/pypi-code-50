from pyquery.pyquery import PyQuery
import urllib.parse as up
import requests
import re

NW = re.compile(r'\W')

def GetLinks(url, proxy=None):
    doc = None
    basehost = None
    if url.startswith("http"):
        basehost = up.urlsplit(url).hostname 
        sess = requests.Session()
        if proxy != None:
            sess.proxies['http'] = sess.proxies['https'] = proxy
        doc = PyQuery(sess.get(url).text)
    else:
        with open(url) as fp:
            doc = PyQuery(fp.read())
    if doc == None:
        doc = PyQuery("<html></html>")
    for l in doc("a[href]"):
        link = l.attrib['href']
        if link  == "#":continue
        if link.startswith("http") or link.startswith("//"):
            res = up.urlsplit(url)
            if basehost != None and res.hostname != basehost:continue
        yield link

        
class Url(str):
    urls = {}
    def __init__(self, url):
        self.l = len(url)
        self.url = url
        self.no_w = set(NW.findall(url))
        self.w = set(url)
        self.host = up.urlsplit(url).hostname
        # self._like = []
        Url.urls[url] = self
    
    def __sub__(self, other):
        if isinstance(other, str):
            other = Url(other)
        if self.url == other.url:
            return 0
        mm = min(self.l, other.l)
        sam = 0
        for i in range(mm):
            if self.url[i] != other.url[i]:
                break
            sam +=1
        # print(sam)
        score = 1 - (sam / max(self.l , other.l))
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
        last = None
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
    def Index(cls, url, distance=0.2):
        host = up.urlsplit(url)
        ls = []

        for l in GetLinks(url):
            ls.append(l)
        #     if l.startswith("http"):
        #         ls.append(l)
        #     else:
        #         ls.append(up.urljoin(host.scheme + "://" + host.hostname, l))
        res = cls.group(ls, distance=distance)
        return sorted(res, key=lambda i:len(i), reverse=True)