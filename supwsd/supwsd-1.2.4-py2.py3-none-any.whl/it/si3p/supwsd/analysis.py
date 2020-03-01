'''
Created on 9 apr 2019

@author: papan
'''
from enum import Enum
from it.si3p.supwsd.config import License
from it.si3p.supwsd.config import Language

class Result(object):
  
    def __init__(self,json):
        self._token=Token(json['token'])
        self._senses=list()
        self._translations=list()
         
        for sense in json['senses']:
            self._senses.append(Sense(sense))
        
        if 'translations' in json:
            for translation in json['translations']:
                self._translations.append(Translation(translation))
            
    @property
    def token(self):
        return self._token
    
    @property
    def senses(self):
        return self._senses
    
    @property
    def translations(self):
        return self._translations
    
    def sense(self):
        return self.senses[0]
    
    def miss(self):
        return self.sense().id=='U'
    

class Token(object):
  
    def __init__(self,json):
        self._word=json['word']
        self._lemma=json['lemma']
        self._tag=json['tag']
        self._pos=Pos[json['pos']]
        
    @property
    def word(self):
        return self._word
    
    @property
    def lemma(self):
        return self._lemma
      
    @property
    def tag(self):
        return self._tag
    
    @property
    def pos(self):
        return self._pos
      
    def __str__(self):
        return self.word


class Sense(object):
  
    def __init__(self,json):
        self._id=json['id']
        self._probability=json['probability']
        
        if 'gloss' in json:
            self._gloss=Gloss(json['gloss'])
        else:
            self._gloss=None;
            
    @property
    def id(self):
        return self._id
    
    @property
    def probability(self):
        return self._probability
    
    @property
    def gloss(self):
        return self._gloss
    
    def __cmp__(self, other):
        return (self.probability > other.probability) - (self.probability< other.probability)
    
    def __eq__(self, other):
        return isinstance(other, Sense) and self.id == other.id
    
    def __str__(self):
        return self.id


class Gloss(object):
  
    def __init__(self,json):
        self._description=json['description']
        self._license=License[json['license']]
        
    @property
    def description(self):
        return self._description
    
    @property
    def license(self):
        return self._license
        
    def __str__(self):
        return self.description
    

class Translation(object):
  
    def __init__(self,json):
        self._lemma=json['lemma']
        
        if 'definition' in json:
            self._definition=json['definition']
            
        self._language=Language[json['language']]
        self._resource=Resource[json['resource']]
        
    @property
    def lemma(self):
        return self._lemma
    
    @property
    def definition(self):
        return self._definition
    
    @property
    def language(self):
        return self._language
    
    @property
    def resource(self):
        return self._resource
        
    def __str__(self):
        return "{}:{}".format(self.language,self.lemma);
    
    
class Pos(Enum):    
    NOUN=1,
    VERB=2,
    ADJ=3,
    ADV=4
    

class Resource(Enum):
    UNDEFINED=0,
    BABELNET=1,
    WN = 2,
    OMWN = 3,
    IWN = 4,
    WONEF = 5,
    WIKI = 6,
    WIKIDIS = 7,
    WIKIDATA = 8,
    OMWIKI = 9,
    WIKICAT = 10,
    WIKIRED = 11,
    WIKT = 12,
    WIKIQU = 13,
    WIKIQUREDI = 14,
    WIKTLB = 15,
    VERBNET = 16,
    FRAMENET = 17,
    MSTERM = 18,
    GEONM = 19,
    WNTR = 20,
    WIKITR = 21,
    MCR_EU = 22,
    OMWN_HR = 23,
    SLOWNET = 24,
    OMWN_ID = 25,
    OMWN_IT = 26,
    MCR_GL = 27,
    ICEWN = 28,
    OMWN_ZH = 29,
    OMWN_NO = 30,
    OMWN_NN = 31,
    SALDO = 32,
    OMWN_JA = 33,
    MCR_CA = 34,
    OMWN_PT = 35,
    OMWN_FI = 36,
    OMWN_PL = 37,
    OMWN_TH = 38,
    OMWN_SK = 39,
    OMWN_LT = 40,
    OMWN_NL = 41,
    OMWN_AR = 42,
    OMWN_FA = 43,
    OMWN_EL = 44,
    MCR_ES = 45,
    OMWN_RO = 46,
    OMWN_SQ = 47,
    OMWN_DA = 48,
    OMWN_FR = 49,
    OMWN_MS = 50,
    OMWN_BG = 51,
    OMWN_HE = 52,
    OMWN_KO = 53,
    MCR_PT = 54,
    OMWN_GAE = 55,
    OMWN_CWN = 56,
    WORD_ATLAS = 57
