import json
import re
import requests

from nlutools.config import env, mapConf, supportConf
from nlutools.utils import printException

http_headers = {"Content-type":"application/json", "Connection":'close'}

def doTask(serverName, data, local_test=False):
    if env == "dev" and serverName in ["w2v", "sentencevec", "sentencesim", "verbobject", "keywords", "segmentor"]:
        return {"msg": "Dev environment is not supported yet."}
    try:
        if serverName == "sentence_bert":
            data = json.dumps(data)
        else:
            data = json.dumps({'server_name':serverName, 'traffic_paramsDict':data})
        if local_test:
            taskUrl = re.sub(r"\d{2,3}\.\d{1,3}\.\d{1,2}\.\d{2,3}", "127.0.0.1", mapConf[serverName + "_test"])
        else:
            taskUrl = mapConf[serverName + '_' + env]
        requests.adapters.DEFAULT_RETRIES = 5
        session = requests.session()
        session.keep_alive = False
        ret = session.post(taskUrl, data, headers=http_headers, timeout=3)
        response_status = ret.status_code
        if response_status == 200:
            result = json.loads(ret.text)
            if serverName == "sentence_bert":
                return result
            if result['status'] == True:
                return result['result']
            return None
        else:
            printException('response error with status code: %s' % response_status)
            printException('please contact supporter %s for this exception' % (supportConf[serverName]))
            return None
    except Exception as e:
        printException('%s exception \nplease contact supporter %s for this exception : \n%s' % (serverName, supportConf[serverName], e))

entity_request_header = {"log_id":"0x111", "user_ip":"", "provider":"algo_survey", "product_name":"algo_survey", "uid":"0x111"}
def doCustomTask(serverName, data, m, c="tagging"):
    # if env == "dev":
    #     return {"msg": "Dev environment is not supported yet."}
    try:
        request_data = {"header":entity_request_header, "request":{"c":c, "m":m, "p":{"query_body":{"text_list":data}}}}
        request_data = json.dumps(request_data)
        taskUrl = mapConf[serverName + '_' + env]
        requests.adapters.DEFAULT_RETRIES = 5
        session = requests.session()
        session.keep_alive = False
        ret = session.post(taskUrl, request_data, headers=http_headers, timeout=3)
        response_status = ret.status_code
        if response_status == 200:
            result = json.loads(ret.text)['response']['results']
            if result:
                return result
            return None
        else:
            printException('response error with status code:%s ' % response_status)
            printException('please contact supporter %s for this exception' % (supportConf[serverName]))
            return None
    except Exception as e:
        printException('%s exception \nplease contact supporter %s for this exception : \n%s' % (serverName, supportConf[serverName], e))

def doNameEntity(line):
    # if env == "dev":
    #     return {"msg": "Dev environment is not supported yet."}
    header = {}
    request = {"c":"", "m":"", "p":{"text":line}}
    try:
        data = {"header":header, "request":request}
        request_data = json.dumps(data)
        taskUrl = mapConf["name_" + env]
        requests.adapters.DEFAULT_RETRIES = 5
        session = requests.session()
        session.keep_alive = False
        ret = session.post(taskUrl, request_data, headers=http_headers, timeout=3)
        response_status = ret.status_code
        if response_status == 200:
            result = json.loads(ret.text)['response']['results']
            return result
        else:
            printException('response error with status code:%s ' % response_status)
            printException('please contact supporter %s for this exception' % (supportConf['name']))
            return []
    except Exception as e:
        printException('%s exception \nplease contact supporter %s for this exception : \n%s'%('name_entity', supportConf['name'], e))
        return []
