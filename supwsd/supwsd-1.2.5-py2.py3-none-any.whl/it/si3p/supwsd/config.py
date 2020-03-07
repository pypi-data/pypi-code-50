'''
Created on 03 mag 2018

@author: Simone Papandrea
'''
from enum import Enum

class License(Enum):
   
    OTHER=('Items without specific licenses')
    
    UNRESTRICTED=('All the permissive licenses without specific restrictions')

    MLP=('Microsoft language portal materials license')

    CC_BY_SA_30=('Creative Commons Attribution-ShareAlike 3.0 License')
    
    CC_BY_30=('Creative Commons Attribution 3.0 License')
    
    CC_BY_NC_SA_30=('Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License')

    WORDNET=('WordNet license')
    
    WORDNET_SEMANTIC_CONCORDANCE=('WordNet Semantic Concordance Release 1.6 License')
    
    BABELNET=('BabelNet license')
    
    def __init__(self,description):
        self._description=description

    def description(self):
        return self._description


class Model(Enum):
  
    SEMCOR=1
    TRAIN_O_MATIC=2
    ONE_SEC=3
    SEMCOR_OMSTI=4
    SEMCOR_OMSTI_ONESEC=5
    SEMCOR_OMSTI_ONESEC_WORDNET=6
    
    @staticmethod
    def get_license(model):
        
        if model==Model.SEMCOR:
            return License.CC_BY_NC_SA_30  
          
        elif model==Model.SEMCOR_OMSTI:
            return License.OTHER
         
        elif model==Model.TRAIN_O_MATIC:
            return License.CC_BY_NC_SA_30
        
        else:
            return License.OTHER
     
   
class Source(Enum):
  
    BABELNET=1
    WORDNET=2
    
    @staticmethod
    def get_license(source):
        
        if source==Source.BABELNET:
            return License.BABELNET
          
        elif source==Source.WORDNET:
            return License.WORDNET
        
        else:
            return License.OTHER
        
        
class Language(Enum):
  
    EN='en'
    IT='it'
    FR='fr'
    DE='de'
    ES='es'
    
    def __init__(self,language):
        self._language=language
    
    def __str__(self):
        return self._language