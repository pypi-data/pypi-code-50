import http.client
import hashlib
import urllib
import random
import json



class Translate:
    def __init__(self, appid, secret):
        self.appid = appid
        self.secret = secret

    def trans(self, query,toLang = 'en', fromLang = 'auto'):
        
        httpClient = None
        myurl = '/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = self.appid + query + str(salt) + self.secret
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(query) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            return result['trans_result'][0]['dst']

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()

# appid = '20180507000154923'  # 填写你的appid
# secretKey = 'FW_nV4HzuNWuzR34pPNG'  # 填写你的密钥

# httpClient = None
# myurl = '/api/trans/vip/translate'

# fromLang = 'auto'   #原文语种
# toLang = 'en'   #译文语种
# salt = random.randint(32768, 65536)
# q= 'ubuntu service 说明与用法'
# sign = appid + q + str(salt) + secretKey
# sign = hashlib.md5(sign.encode()).hexdigest()
# myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
# salt) + '&sign=' + sign

# try:
#     httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
#     httpClient.request('GET', myurl)

#     # response是HTTPResponse对象
#     response = httpClient.getresponse()
#     result_all = response.read().decode("utf-8")
#     result = json.loads(result_all)
#     # return result['trans_result'][0]['dst']

# except Exception as e:
#     print (e)
# finally:
#     if httpClient:
#         httpClient.close()