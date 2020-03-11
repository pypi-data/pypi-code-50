import requests
import json

def get(url,params=None,headers=None,local_response_header=None,local_response_body=None):
    # Отправляет get запрос на сервис.
    # url - mandatory, URL ресурса
    # params - optional, параметры запроса
    # headers - optional, хедеры запроса
    # local_response_body - optional, имя файла, куда будет сохранен body ответа. При нахождении существующего файла перезапись, при отсутствии создание нового
    # local_response_header - optional, имя файла, куда будет сохранен header ответа. При нахождении существующего файла перезапись, при отсутствии создание нового
    #
    #При вызове метода с параметрами local_response_body и local_response_header возвращает status_code
    #При отсутствии возвращает ответ в виде кортежа (header,body,status_code)

    r = requests.get(url=url,verify=False,params=params,headers=headers)
    if (not local_response_body) & (not local_response_header):
        return r.status_code,r.headers,r.content
    else:
        if local_response_header:
            with open(local_response_header,'w') as f:
                f.write(json.dumps(dict(r.headers)))
                f.close()
        if local_response_body:
            with open(local_response_body,'wb') as f:
                f.write(r.content)
                f.close()
        return r.status_code


def post(url,local_request_body,params=None,headers=None,local_response_header=None,local_response_body=None):
    # Отправляет post запрос на сервис.
    # url - mandatory, URL ресурса
    # local_request_body - mandatory, путь к файлу с телом запроса
    # params - optional, параметры запроса
    # headers - optional, хедеры запроса
    # localbody - optional, имя файла, куда будет сохранен body ответа. При нахождении существующего файла перезапись, при отсутствии создание нового
    # localheader - optional, имя файла, куда будет сохранен header ответа. При нахождении существующего файла перезапись, при отсутствии создание нового
    #
    # При вызове метода с параметрами local_response_header и local_response_body возвращает status_code
    # При отсутствии возвращает ответ в виде кортежа (header,body,status_code)
    with open(local_request_body,'r') as f:
        data = f.read()
        f.close()
    r = requests.post(url,data=data,params=params,headers=headers, verify=False)
    if (not local_response_body) & (not local_response_header):
        return r.status_code,r.headers,r.content
    else:
        if local_response_header:
            with open(local_response_header, 'w') as f:
                f.write(json.dumps(dict(r.headers)))
                f.close()
        if local_response_body:
            with open(local_response_body, 'wb') as f:
                f.write(r.content)
                f.close()
        return r.status_code