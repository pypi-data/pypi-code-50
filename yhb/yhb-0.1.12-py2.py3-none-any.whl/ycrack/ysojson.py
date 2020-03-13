import requests
import re
import execjs

url = 'http://www.pbc.gov.cn/tiaofasi/144941/144957/index.html'
session = requests.session()

headers = {
    'Host': 'www.pbc.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Referer': 'http://www.pbc.gov.cn/WZWSREL3RpYW9mYXNpLzE0NDk0MS8xNDQ5NTcvaW5kZXguaHRtbA==',
    'Cookie': '',
}

# 第一次请求、通过它的resp对象、获取到一个cookies字典、然后获取其中wzws_id的值
resp = session.get('http://www.pbc.gov.cn/tiaofasi/144941/144957/index.html', headers=headers)
# 第一次请求该页面、目的是为了获取他cookie中的wzxz_id字段和他的加密js
first_resp = resp.content.decode()
# 使用正则获取到scrpit脚本
script = re.search(r'(eval.*?)</script>', first_resp, re.S).group(1)
script = re.sub(r'\r\n', '', script)
# 美化js
beautify_script = script

# 获取所有需要的变量
dynamicurl = re.search(r'var dynamicurl = "(.*?)";', beautify_script, re.S).group(1)
wzwschallenge = re.search(r'var wzwschallenge = "(.*?)";', beautify_script, re.S).group(1)
wzwschallengex = re.search(r'var wzwschallengex = "(.*?)";', beautify_script, re.S).group(1)
template = re.search(r'var template = (\d{1,2});', beautify_script, re.S).group(1)
return_number = re.search(r'(return "WZWS_CONFIRM_PREFIX_LABEL\d{1,2}" \+ hash;)', beautify_script, re.S).group(1)
hash = re.search(r'hash \*= (\d{1,2});', beautify_script, re.S).group(1)

# js代码
hehe = '''
var dynamicurl = ''' + '"{}"'.format(str(dynamicurl)) + ''';
var wzwschallenge = ''' + '"{}"'.format(wzwschallenge) + ''';
var wzwschallengex = ''' + '"{}"'.format(wzwschallengex) + ''';
var template = ''' + '{}'.format(template) + ''';
var encoderchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
function KTKY2RBD9NHPBCIHV9ZMEQQDARSLVFDU(str) {
	var out, i, len;
	var c1, c2, c3;
	len = str.length;
	i = 0;
	out = "";
	while (i < len) {
		c1 = str.charCodeAt(i++) & 0xff;
		if (i == len) {
			out += encoderchars.charAt(c1 >> 2);
			out += encoderchars.charAt((c1 & 0x3) << 4);
			out += "==";
			break;
		}
		c2 = str.charCodeAt(i++);
		if (i == len) {
			out += encoderchars.charAt(c1 >> 2);
			out += encoderchars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xf0) >> 4));
			out += encoderchars.charAt((c2 & 0xf) << 2);
			out += "=";
			break;
		}
		c3 = str.charCodeAt(i++);
		out += encoderchars.charAt(c1 >> 2);
		out += encoderchars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xf0) >> 4));
		out += encoderchars.charAt(((c2 & 0xf) << 2) | ((c3 & 0xc0) >> 6));
		out += encoderchars.charAt(c3 & 0x3f);
	}
	return out;
}
function findDimensions() {
	return false;
}
function QWERTASDFGXYSF() {
	var tmp = wzwschallenge + wzwschallengex;
	var hash = 0;
	var i = 0;
	for (i = 0; i < tmp.length; i++) {
		hash += tmp.charCodeAt(i);
	}
	hash *= ''' + '{}'.format(hash) + ''';
	hash += 111111;
	''' + '{}'.format(return_number) + ''';
}
function HXXTTKKLLPPP5() {
	if (findDimensions()) {} else {
		var cookieString = "";
		cookieString = "wzwstemplate=" + KTKY2RBD9NHPBCIHV9ZMEQQDARSLVFDU(template.toString()) + "; path=/";
		cookieString01 = cookieString;
		var confirm = QWERTASDFGXYSF();
		cookieString = "wzwschallenge=" + KTKY2RBD9NHPBCIHV9ZMEQQDARSLVFDU(confirm.toString()) + "; path=/";
		var haha = new Array();
		haha = [cookieString01, cookieString]
		return haha
	}
}
HXXTTKKLLPPP5();
'''

result = execjs.eval(hehe)

# 解释js后获取cookie中的template
template = list(result)[0].split('path=/')[0]
# 解释js后获取cookie中的challenge
challenge = list(result)[1].split('path=/')[0].split(';')[0]

# 获取第一次请求返回的cookie 下面是两种方法获取cookie 获取到的都是一样的
cookie = str(requests.utils.dict_from_cookiejar(resp.cookies))
cookie02 = resp.cookies.get_dict()

# cookie_key是通过请求首页获取到的wzws_cid
cookie_key = 'wzws_cid=' + eval(cookie.split(':')[-1][1:-1])
# 然后再将js解密出来的template和challenge拼接起来 获得cookies
cookie_key = cookie_key + '; ' + template + challenge
# 请求头设置生成的cookie
headers['Cookie'] = cookie_key

# 带着headers重新请求url
final_resp = session.get('http://www.pbc.gov.cn/tiaofasi/144941/144957/index.html', headers=headers).content.decode()
print(final_resp)
