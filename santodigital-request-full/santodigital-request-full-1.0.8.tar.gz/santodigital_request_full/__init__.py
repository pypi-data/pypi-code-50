import json
import requests
import math
from santodigital_request_full.validator.UrlValidator import UrlValidator

class RequestFull():
    def execute(self, url=None, paginate_type=None, auth=None, object_name=None, params=None, extraParams=None):
        res = self.validate(url, paginate_type, auth, object_name, params)
        if (res["error"] != None):
            return res
        
        if (paginate_type == 1):
            res = self.fetchDataUntilEnd(url, auth, params, extraParams, object_name)
            
        if (paginate_type == 2):
            res = self.fetchDataUntilControl(url, auth, params, extraParams, object_name)
            
        if (paginate_type == 3):
            res = self.fetchPageData(url, auth, params, extraParams, object_name)
            
        return res
    
    def fetchDataUntilEnd(self, url, auth, params, extraParams, object_name):
        allData = { object_name: [], 'total': 0 }
        
        flag = params["flag"]
        data = { flag: False,  "total": 0 }

        while (data[flag] == False):
            # TODO: Criar loop para adicionar params e valores
            data = self.fetchData(url, auth);
            if ('error' in data):
                return { 'error': data["error"] }

            if (flag not in data):
                return { 'error': "flag não encontrada no objeto de retorno" }

            allData[object_name] += data[object_name]
        
        allData['total'] += len(allData[object_name])

        return allData

    def fetchDataUntilControl(self, url, auth, params, extraParams, object_name):
        allData = { object_name: [], 'total': 0 }
        
        init = params["init"]
        pageSize = params["pageSize"]
        pageSizeNum = params["pageSizeNum"]
        total = params["total"]

        startAt = 0

        data = { init: 0, pageSize: pageSizeNum, total: 100 }

        while (startAt < data['total']):
            # TODO: Criar loop para adicionar params e valores
            if (extraParams != None):
                url = f"{url}?{pageSize}={pageSizeNum}&{init}={startAt}&{extraParams}";
            else:
                url = f"{url}?{pageSize}={pageSizeNum}&{init}={startAt}";
            
            data = self.fetchData(url, auth);
            if ('error' in data):
                return { 'error': data["error"] }

            allData[object_name] += data[object_name]
            startAt += data[total];
            
            if (startAt + data[pageSize] > data[total]):
                pageSizeNum = data[total] - startAt

        allData['total'] += len(allData[object_name])

        return allData

    # TODO: Criar método para paginação por controle de página
    def fetchPageData(self, url, auth, params, extraParams, object_name):
        allData = { object_name: [], 'total': 0 }
        
        pageField = params["pageField"]
        pageLenField = params["pageLenField"]
        total = params["total"]

        data = { pageField: 1, pageLenField: 100 }
        maxPages = 1000

        while (data[pageField] <= maxPages):
            # TODO: Criar loop para adicionar params e valores
            if (extraParams != None):
                api_url = f"{url}?{pageField}={data[pageField]}&{extraParams}&size=100";
            else:
                api_url = f"{url}?{pageField}={data[pageField]}&size=100";
            data = self.fetchData(api_url, auth);

            if ('error' in data):
                return { 'error': data["error"] }

            if (data[pageField] == 1):
                total = data[total]
                maxPages = math.ceil(total / data[pageLenField])

            allData[object_name] += data[object_name]

            data[pageField] = data[pageField] + 1;
            
        allData['total'] += len(allData[object_name])

        return allData

    def fetchData(self, urlFull, auth):
        """
        Executa a chamada para a API com autenticação Oauth
        
        :session: Sessão Oauth
        :urlFull: URI para requisião
        """

        session = None
        if (auth["type"] == "OAuth"):
            session = auth["session"]

            try:
                result = session.get(urlFull)
                if (result.status_code >= 401 and result.status_code <= 403):
                    return { 'error': 'Invalid Authentication' }

                data = json.loads(result.text)
            except Exception as e:
                return { 'error': e }
        else:
            if (auth["type"] == "OAuth2"):
                token = auth["token"]
                try:
                    headers = {"Authorization": "Bearer " + token}
                    result = requests.get(urlFull, headers=headers)
                    data = json.loads(result.text)
                except Exception as e:
                    return { 'error': e }

        return data

    def validate(self, url=None, paginate_type=None, auth=None, object_name=None, params=None):
        if (url == None):
            return { "error": "url não preenchida. Informar a url na chamada do método" }

        if (UrlValidator().validate(url) == False):
            return { "error": "url inválida" }
        
        if (paginate_type == None):
            return { "error": "paginate_type não preenchido. Informar o paginate_type (1 - Flag ou 2 - Totalizadores) na chamada do método" }

        valid_types = {1, 2, 3}

        if (paginate_type not in valid_types):
            return { "error": "paginate_type inválido. Informar o paginate_type = [1 - Flag ou 2 - Totalizadores]" }
        
        if (paginate_type == 1 and "flag" not in params):
            return { "error": "flag inválida. Informar o nome da variável (flag) no retorno da API para controle de fim de processamento" }

        if (paginate_type == 1 and params["flag"] == None):
            return { "error": "flag inválida. Informar o nome da variável (flag) no retorno da API para controle de fim de processamento" }

        if  ( paginate_type == 2
        and ( "init" not in params or "pageSize" not in params or "pageSizeNum" not in params or "total" not in params)):
            return { "error": "params inválido. Informar um objeto params com as variáveis de controle no retorno da API" }

        if  ( paginate_type == 2
        and ( params["init"] == None or params["pageSize"] == None or params["total"] == None)):
            return { "error": "params inválido. Informar um objeto params com as variáveis de controle no retorno da API" }

        if (auth == None):
            return { "error": "auth não informado. Informar um objeto do tipo OAuth1" }

        if (isinstance(auth, list)):
            return { "error": "auth não preenchida. Enviar os parametros de autenticação na chamada do método" }
        
        valid_auth = {"OAuth", "OAuth2"}

        if (auth["type"] not in valid_auth):
            return { "error": "auth inválido. Métodos permitidos: OAuth ou OAuth2" }
        
        if (auth["type"] == "OAuth" and (auth["session"] == None or auth["session"] == "")):
            return { "error": "auth inválido. Métodos permitidos: OAuth ou OAuth2" }
        
        if (auth["type"] == "OAuth2" and (auth["token"] == None or auth["token"] == "")):
            return { "error": "auth inválido. Métodos permitidos: OAuth ou OAuth2" }
        
        if (object_name == None):
            return { "error": "object_name inválido. Informar o object_name com o nome do objeto de retorno da API" }
        
        return { "error": None }