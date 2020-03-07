'''
Created on 03 mag 2018

@author: Simone Papandrea
'''
import requests
import json
import base64
from it.si3p.supwsd.analysis import Result

class SupException(Exception):
    pass

class SupWSD(object):
  
    MAX_PAYLOAD=200
    SENSE_TAG = "<SENSE>"
        
    class __SupWSD:
        
        def __init__(self,apikey):
            self._service=SupService(apikey)
            
        
        def disambiguate(self,text,model,language=None,distribution=False,*translations):

            results=None
            
            if len(text) >SupWSD.MAX_PAYLOAD:
                raise ValueError("The text in the input must be at most " + SupWSD.MAX_PAYLOAD + " characters long")
                        
            try:
                result = self._service.post("wsd" if language is None else "api/v2/{}".format(language),{'supRequest':Request(text,model,distribution,list(translations)).to_json()})
                            
                if not result is None:
                    results=list()
                    for result in json.loads(result):
                        results.append(Result(result))
                        
            except Exception as e:
                raise SupException(e)
        
            return results

    _instance = None
        
    def __new__(cls,apikey):
        if not SupWSD._instance:
            SupWSD._instance = SupWSD.__SupWSD(apikey)
        return SupWSD._instance
        

class SupService(object):

    _url='https://supwsd.net/supwsd/'

    def __init__(self, apikey):
        self._apikey=apikey       
        
    def post(self, resource, params):
        r = requests.post(self._url+resource,data = params,headers=self.__headers(), timeout=120)
        r.raise_for_status()
        return r.text
    
    def get(self, resource,params=None):
        r = requests.get(self._url+resource,data = params,headers=self.__headers(), timeout=30)
        r.raise_for_status()
        return r.text

    def __headers(self):
        return {'content-type': 'application/x-www-form-urlencoded',
                "accept-encoding": 'gzip',
                'accept-charset':'UTF8',
                'authorization':  "Basic " +base64.b64encode(bytes(self._apikey,'utf-8')).decode("utf-8")}
        
class Request(object):

    def __init__(self, content, model,distribution=False,languages=None):
        self._content=content
        self._model=model
        self._distribution=distribution
        self._languages=languages;
        
    @property        
    def content(self):
        return self._content
    
    @property
    def model(self):
        return self._model
     
    @property
    def languages(self):
        return self._languages
       
    @property
    def distribution(self):
        return self._distribution
    
    def to_json(self):
        return json.dumps({"content":self.content,"model":self.model.name,"distribution":self.distribution,"languages":[lang.name for lang in self.languages]})
