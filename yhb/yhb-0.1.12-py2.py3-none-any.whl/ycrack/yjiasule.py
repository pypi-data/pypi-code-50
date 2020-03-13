import re
import execjs


def prepare_cookie(html):
    try:
        js_match = re.findall(r'<script>(.*?)</script>', html)
        js = js_match[0]
        key_js = re.findall(r'eval\((.*?)\);', js)[0]
        replace = 'var cookie_js={};'.format(key_js)
        js = re.sub(r'eval\(.*?\);', replace, js)
        js = js.replace(
            'break',
            'if(cookie_js.indexOf("document.cookie=\'__jsl_clearance=")!=-1)'
            '{cookie_js = cookie_js.match(/document.cookie=(.*?)\+\';Expires/i)[1];break}')
        js = 'var cookie_js, window={};' + js + 'function get_cookie(){return cookie_js;}'
        js = js.replace('', '')
        ctx = execjs.compile(js)
        more_code_ori = ctx.call("get_cookie")
        more_code = re.sub('(document.*?ase\(\);)', "'{0}/';".format("www.cbrc.gov.cn"), more_code_ori)
        more_code = re.sub("window\[\'_p\'\+\'hantom\'\]", "undefined", more_code)
        more_code = re.sub("window\[\'callP\'\+\'hantom\'\]", "undefined", more_code)
        more_code = re.sub("window\[\'__p\'\+\'hantom\'\+\'as\'\]", "undefined", more_code)
        more_code = re.sub("_2t.parseInt", "undefined", more_code)
        more_code = re.sub("window.headless", "undefined", more_code)
        more_code = "function get_result(){return " + more_code + ";}"
        ctx_more = execjs.compile(more_code)
        result = ctx_more.call("get_result")
        my_cookie = {
            'domain': "www.cbrc.gov.cn",
            'expires': None,
            'name': result.split("=")[0],
            'path': '/',
            'value': result.split("=")[1].split(";")[0],
        }
        return my_cookie
    except Exception as e:
        return None
