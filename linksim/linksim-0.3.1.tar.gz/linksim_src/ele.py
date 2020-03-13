import re, datetime, requests
import chardet
from pyquery.pyquery import PyQuery
from lxml.html import HtmlElement

T = re.compile(r'(\d{4}[:\/]\d{1,2}[:\/]\d{1,3})')
TAG = re.compile(r'<(\w+)')
TODAY = datetime.datetime.today()

def more_like_today(i):
    if isinstance(i, HtmlElement):
        i = i.text
    y,m,d = re.split(r'\D', T.findall(i)[0])
    dd = TODAY - datetime.datetime(int(y), int(m), int(d))
    return dd.days

def get_css(e):
    css = e.tag
    if "class" in e.attrib:
        css += "." + e.attrib.get("class")
    
    if "id" in e.attrib:
        css += "#" + e.attrib.get("id")
        return css
    p = e
    while 1:
        p = p.getparent()
        
        if p.tag == "body":break
        pcss = p.tag
        if "class" in p.attrib:
            pcss += "." + p.attrib["class"]
        if "id" in p.attrib:
            pcss += "#" + p.attrib["id"]
            css = pcss + " > " + css
            break
        
        css = pcss + " > " + css
    return css

def detect_content(doc:[PyQuery, str]):
    if isinstance(doc, str):
        doc = PyQuery(doc)
    # H = doc.html()
    skip_words = ("Copyright", "友情链接")
    more_max = None
    for p in doc("p"):
        for w in skip_words:
            if w in p.text_content():
                continue
        if more_max == None:
            more_max = p
        elif len(p.text_content().replace(" ",""))>= len(more_max.text_content().replace(" ","")):
            more_max = p
    return get_css(more_max)



def detect_date(doc:[PyQuery,str]):
    if isinstance(doc, str):
        doc = PyQuery(doc)
    H = doc.html()
    more_accuracy = None
    
    for mat in T.finditer(H):
        ps,pe = mat.span()
        name = mat.group()
        found_tag = set()
        for p in TAG.findall(H[ps-100:pe]):
            if p in found_tag:continue
            found_tag.add(p)
            
            for ele in doc(p):
                
                if ele.text is None:continue
                # print(ele, ele.text)
                # import pdb;pdb.set_trace()

                if name in ele.text:
                    # print(ele, ele.text)
                    if more_accuracy == None:
                        # print(p, name, ele.text)
                        more_accuracy = ele
                    else:
                        if more_like_today(ele.text) < more_like_today(more_accuracy.text):
                            # print(p, name, ele.text)
                            more_accuracy = ele
    if more_accuracy is not None:
        return get_css(more_accuracy)
        



# class Doc:
#     def __init__(self, c):
#         self._c = PyQuery(c)
    
#     def links
def detect(url:[PyQuery,str], proxy=""):
    url = url.strip()
    if isinstance(url, str):
        if url.startswith("http"):
            sess = requests.Session()
            sess.proxies['http'] = sess.proxies['https'] = proxy
            raw = sess.get(url).content
            en = chardet.detect(raw).get("encoding")
            content = raw.decode(en, "ignore")
            doc = PyQuery(content)
        else:
            content = url
            doc = PyQuery(content)
    else:
        content = url.html()
        doc = url
    ct = detect_date(content)
    cc = detect_content(content)

    return {
        "date": (ct, doc(ct).text(),),
        "content": (cc, doc(cc).text(),)
    }
    
    