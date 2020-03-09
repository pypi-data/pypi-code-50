#!/usr/bin/env python
from seoaudit.checks.element import ElementCheck
from seoaudit.checks.page import PageCheck
from seoaudit.checks.site import SiteCheck

stop_words = ["a","ako","ali","bi","bih","bila","bili","bilo","bio","bismo","biste","biti","bumo","da","do","duž","ga","hoće","hoćemo","hoćete","hoćeš","hoću","i","iako","ih","ili","iz","ja","je","jedna","jedne","jedno","jer","jesam","jesi","jesmo","jest","jeste","jesu","jim","joj","još","ju","kada","kako","kao","koja","koje","koji","kojima","koju","kojega","kroz","li","me","mene","meni","mi","mimo","moj","moja","moje","mu","na","nad","nakon","nam","nama","nas","naš","naša","naše","našeg","ne","nego","neka","neki","nekog","neku","nema","netko","neće","nećemo","nećete","nećeš","neću","nešto","ni","nije","nikoga","nikoje","nikoju","nisam","nisi","nismo","niste","nisu","njega","njegov","njegova","njegovo","njemu","njezin","njezina","njezino","njih","njihov","njihova","njihovo","njim","njima","njoj","nju","no","o","od","odmah","on","ona","oni","ono","ova","pa","pak","po","pod","pored","prije","s","sa","sam","samo","se","sebe","sebi","si","smo","ste","su","sve","svi","svog","svoj","svoja","svoje","svom","ta","tada","taj","tako","te","tebe","tebi","ti","to","toj","tome","tu","tvoj","tvoja","tvoje","u","uz","vam","vama","vas","vaš","vaša","vaše","već","vi","vrlo","za","zar","će","ćemo","ćete","ćeš","ću","što"]


import re
import sys
stop=set(['biti','jesam','budem','sam','jesi','budeš','si','jesmo','budemo',
   'smo','jeste','budete','ste','jesu','budu','su','bih','bijah','bjeh',
   'bijaše','bi','bje','bješe','bijasmo','bismo','bjesmo','bijaste','biste',
   'bjeste','bijahu','biste','bjeste','bijahu','bi','biše','bjehu','bješe',
   'bio','bili','budimo','budite','bila','bilo','bile','ću','ćeš','će',
   'ćemo','ćete','želim','želiš','želi','želimo','želite','žele','moram',
   'moraš','mora','moramo','morate','moraju','trebam','trebaš','treba',
   'trebamo','trebate','trebaju','mogu','možeš','može','možemo','možete'])

class CroatianStemmer(object):
    def __init__(self):
        self.pravila=[re.compile(r'^('+osnova+')('+nastavak+r')$') for osnova, nastavak in [e.strip().split(' ') for e in open('rules.txt', encoding='utf8')]]
        self.transformacije=[e.strip().split('\t') for e in open('transformations.txt', encoding='utf8')]

    def stem(self, token):
        if token.lower() in stop:
            return token.lower()
        else:
            return self.korjenuj(self.transformiraj(token.lower()))

    def istakniSlogotvornoR(self, niz):
        return re.sub(r'(^|[^aeiou])r($|[^aeiou])',r'\1R\2',niz)

    def imaSamoglasnik(self, niz):
        if re.search(r'[aeiouR]', self.istakniSlogotvornoR(niz)) is None:
            return False
        else:
            return True

    def transformiraj(self, pojavnica):
        for trazi,zamijeni in self.transformacije:
            if pojavnica.endswith(trazi):
                return pojavnica[:-len(trazi)]+zamijeni
        return pojavnica

    def korjenuj(self, pojavnica):
        for pravilo in self.pravila:
            dioba=pravilo.match(pojavnica)
            if dioba is not None:
                if self.imaSamoglasnik(dioba.group(1)) and len(dioba.group(1))>1:
                    return dioba.group(1)
        return pojavnica

stemmer = CroatianStemmer()
page_tests = [(PageCheck.TEXT_TO_CODE_RATIO, {"min_ratio": 0.1}),
              (PageCheck.DOM_SIZE, {"max_size": 1500}),
              [PageCheck.ELEMENTS_SIMILARITY,
               {"el1_query": "/*", "el2_query": "/html/head/title", "match_most_common": 1, "stop_words": stop_words, "stemmer": stemmer}],
              [PageCheck.ELEMENTS_SIMILARITY,
               {"el1_query": "/*", "el2_query": "/html/head/meta[@name='description']/@content",
                "match_most_common": 1, "stop_words": stop_words, "stemmer": stemmer}],
              [PageCheck.ELEMENTS_SIMILARITY,
               {"el1_query": "//h1", "el2_query": "/html/head/meta[@name='description']/@content",
                "match_most_common": 1, "stop_words": stop_words, "stemmer": stemmer}],
              [PageCheck.ELEMENTS_COUNT, {"query": "(//h2)", "min_count": 2}],
              [PageCheck.STRUCTURED_DATA_FOUND, {"type": "json-ld", "property": "@type", "value": "Organization"}],
                [PageCheck.STRUCTURED_DATA_FOUND, {"type": "json-ld", "property": "@type", "value": "Article"}],
              [SiteCheck.TITLE_REPETITION],
              [SiteCheck.DESCRIPTION_REPETITION],
              [SiteCheck.PAGE_IN_SITEMAP],
              [SiteCheck.PAGE_CRAWLABLE]]

# Todo: add regex check for charset = utf-8
# Todo: add regex check for robots not block page
element_tests = [
    ("/html", 'lang'),
    ("(/html/head/meta[@charset])", 'charset'),
    ("/html/head/title", 'textContent',
     [(ElementCheck.MIN_LENGTH, {"min_length": 40}),
      (ElementCheck.MAX_LENGTH, {"max_length": 70})]),
    ("(/html/head/meta[@name='description'])", 'content',
     [(ElementCheck.MIN_LENGTH, {"min_length": 50}), (ElementCheck.MAX_LENGTH, {"max_length": 160})]),
    ("(/html/head/meta[@name='viewport'])", 'content'),
    ("(//img)", 'alt'),
    ("(//a[@href])", 'title'),
    ("(/html/head/meta[@property='og:locale'])", 'content'),
    ("(/html/head/meta[@property='og:title'])", 'content'),
    ("(/html/head/meta[@property='og:description'])", 'content'),
    ("(/html/head/meta[@property='og:type'])", 'content'),
    ("(/html/head/meta[@property='og:url'])", 'content'),
    ("(/html/head/meta[@property='og:image'])", 'content'),
    ("(/html/head/meta[@name='twitter:title'])", 'content'),
    ("(/html/head/meta[@name='twitter:description'])", 'content'),
    ("(/html/head/meta[@name='twitter:image'])", 'content'),
    ("(/html/head/meta[@name='twitter:card'])", 'content'),
    ("(/html/head/link[@rel='canonical'])", 'href')
]
