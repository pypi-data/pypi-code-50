#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from sprzedaz.models import CastoramaKli, CastoramaKar, CastoramaLog, Nag, Lin

import sys
import io
import getopt
from decimal import Decimal

from io import StringIO, BytesIO
from html.parser import HTMLParser

import urllib.request

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfdevice import TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams

from datetime import datetime, date

import requests
import base64

def process_pdf(rsrcmgr, device, fp, pagenos=None, maxpages=0, password='', caching=True, check_extractable=True):
  interpreter = PDFPageInterpreter(rsrcmgr, device)
  for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,
              caching=caching, check_extractable=check_extractable):
    interpreter.process_page(page)
  return


class StringIO2(StringIO):
    encoding = 'utf-8'


class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.in_div = False
        self.div_tag = None
        self.div_txt = ""
        self.data = []
        super().__init__()
        
    def handle_starttag(self, tag, attrs):        
        if tag.lower()=='div':
            x = dict(attrs)
            if 'style' in x:
                y1 = [ str(pos).split(':') for pos in x['style'].split(';') ]
                y2 = dict([ (pos2[0].strip(), pos2[1].strip())  for pos2 in y1 if len(pos2)==2 ] )               
                top = int(y2['top'].replace('px','')) if 'width' in y2 else None
                left = int(y2['left'].replace('px','')) if 'height' in y2 else None                
            else:
                top = 0
                left = 0
            self.div_tag = (top, left)
            self.in_div = True
            self.div_txt = ""

    def handle_endtag(self, tag):
        if tag.lower()=='div':
            if self.div_tag[0] and self.div_tag[1]:
                self.data.append((self.div_tag[0], self.div_tag[1], self.div_txt.strip()))
            self.in_div = False
            
    def handle_data(self, data):
        self.div_txt += data



def convert(fp):
    showpageno = True
    
    pagenos = set()
    laparams = LAParams()
    rsrcmgr = PDFResourceManager(caching=False)
    retstr = StringIO2()
    retstr.encoding = 'utf-8'
    device = HTMLConverter(rsrcmgr, retstr, scale=1, layoutmode='normal', laparams=laparams, debug=False, codec=None)
    
    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=0, password='', caching=False, check_extractable=True)
    device.close()
    
    return  retstr.getvalue()


def getKey(item):
    return item[0]*1000+item[1]


def pdf_to_order(fp):

    x = convert(BytesIO(fp))

    parser = MyHTMLParser()
    parser.feed(x)

    data = sorted(parser.data, key=getKey)

    header = []
    table = []
    footer = []

    status = 0
    for pos in data:
        if status == 0:
            if pos[2] =='Total':
                status = 1
                continue
            if '\n' in pos[2]:
                pos[2].split('\n')
                for pos2 in pos[2].split('\n'):
                    header.append((pos2, pos[0], pos[1]))
            else:
                header.append((pos[2], pos[0], pos[1]))
        if status==1:
            if 'Total Zamowienia' in pos[2]:
                status = 2
                continue
            table.append((pos[2], pos[0], pos[1]))            
        if status == 2:        
            footer.append((pos[2], pos[0], pos[1]))
            
    i = 0
    lp = 1
    rows = []
    row = []
    for pos in table: 
        if len(row)==0:
            row.append(pos)
        else:
            if pos[1]==row[0][1]:
                row.append(pos)
            else:
                rows.append(row)
                row=[pos,]
    if len(row)>0:
        rows.append(row)
        
    clean_rows = []

    lp=1
    for row in rows:
        try:
            row2 = list([pos[0] for pos in row])
            print("WWWWWWWWWWWWWWW", row2)
            
            try:
                lp2 = int(row2[0])
            except:
                lp2 = 0
            
            if lp2 != lp:
                continue
                
            lp +=1
            if len(row2)<10:
                row3 = []
                #k = 0
                for pos in row2:
                    pos2 = pos.split(' ', 1)
                    if len(pos2)>1 and pos2[0] and pos2[1] and (pos2[0][0].isdigit() or pos2[0][0].isdigit()):
                        row3.append(pos2[0].strip())
                        row3.append(pos2[1].strip())
                    else:
                        row3.append(pos)
                    #if ' ' in pos and k!=3:                        
                    #    for pos2 in pos.split(' ', 1):
                    #        row3.append(pos2)
                    #else:
                    #    row3.append(pos)
                    # k +=1
                row2 = row3
                print("UUUUUUU", row2)
                
            
            row2[0] = int(row2[0])
            row2[4] = row2[4].replace('\n', ' ')
            
            row2[5] = Decimal(row2[5])
            
            row2[7] = Decimal(row2[7])
            row2[8] = Decimal(row2[8])
            
            row2[9] = Decimal(row2[9].replace('\n', '').replace(' ',''))
        except:
            print("##################################################################")
            #for row in table:
            #    print(row)                        
            print(len(row2), row2)
            print("##################################################################")
        
        clean_rows.append(row2)
        
            

    order_id = None
    data_dok = None

    nazwa_klienta = None
    adres_klienta = None

    data_dost = None
    komentarz = None 
    adres_dostawy = None

    status = 0
    status2 = 0
    for pos in header:
        if status == 0:
            if pos[0].startswith('ORDERS'):
                order_id = pos[0].split(' ')[1]
                status = 1
                continue
        if status == 1:
            data_dok = pos[0]
            status = 2
            status2 = 0
            continue
        if status == 2:
            if status2 == 0:
                nazwa_klienta = pos[0]
                status2 = 1
            if status2 == 1:
                if pos[0].startswith('POLBRUK'):
                    status2 = 2
                    continue
            if status2 == 2:
                adres_klienta = pos[0]
                status2 = 3
                continue
            if status2 == 3:
                if pos[0].startswith('Waluta'):
                    status2 = 0
                    status = 3
                    continue
        if status == 3:
            if pos[0].startswith('Data'):
                data_dost = pos[0].replace('Data dostawy : ','')
            if pos[0].startswith('Komentarz'):
                komentarz = pos[0].replace('Komentarz :','')
            if pos[0].startswith('Adres'):
                adres_dostawy = pos[0].replace("Adres dostawy : ",'')

    clean_header = [order_id, data_dok, nazwa_klienta, adres_klienta, data_dost, komentarz, adres_dostawy]            
    
    try:
        total = Decimal(footer[0][0].replace(' ',''))
        total2 = sum([pos[9] for pos in clean_rows])
    except:
        total2 = 0
        
    if total != total2:
        print(total, total2)
        for pos in clean_rows:
            print("clean_rows", pos[9])
        #print("Footer1:", footer)
        #print("Footer2:",footer[0][0].replace(' ',''))
        #print("Footer3:",footer[0][0].replace(' ',''))
    return (total == total2, clean_header, clean_rows)


def export_dok(link, row, header, table):
    print(header)
    errors = False 
    nag = Nag()
    nag.nr_zam = header[0]
    nag.data_dok = datetime.strptime(header[1], '%d/%m/%Y')
    nag.lokalizacja = header[2]
    nag.adres = header[3]
    
    d = header[4].split(' ')
    
    dzien = int(d[0])
    rok = int(d[2])
    m = ['sty', 'lut', 'mar', 'kwi', 'maj', 'cze', 'lip', 'sie', 'wrz', 'paź', 'lis', 'gru'].index(d[1][:3].lower())
    m+=1
    
    nag.data_dost =date(rok, m, dzien)
    nag.komentarz = header[5]
    nag.nr_lok_dost = header[6].split(' ')[0]
    
    lok = CastoramaKli.objects.filter(numer=nag.nr_lok_dost)
    if len(lok)==1:    
        nag.logo = lok[0].logo
        nag.mag = lok[0].mag
    else:
        errors = True
    if errors:
        nag.status = '2'
    else:
        nag.status = '5'
    
    nag.pdf_link = link
        
    nag.save()
    
    for pos in table:
        lin = Lin()
        lin.parent=nag
        lin.lp = pos[0]
        lin.castorama_kar = pos[1]
        if pos[2] and pos[2]!='???':
            lin.symkar = pos[2]
        else:
            x = CastoramaKar.objects.filter(id_castorama = pos[1])
            if len(x)==1:
                lin.symkar = x[0].id_softlab
            else:
                errors = True
        
        lin.opis = pos[4]
        lin.ilosc = pos[5]
        lin.jz = pos[6]
        lin.cena = pos[8]
        lin.netto = pos[9]
        lin.save()
        
    if errors:
        nag.status='2'
        nag.save()
    
    
def process_row(row):    
    if '.pdf' in row[2].lower():
        file_name = row[2]        
        #link = "https://intranet.crhem.pl/castorama_files/"+file_name
        link = 'http://pomoc.crhem.pl/polbruk/sprzedaz/castorama_files/'+file_name
        data = base64.b64decode(row[3].encode('utf-8'))

        #with open(file_name, "wb") as fff:
        #    fff.write(data)

        x = Nag.objects.filter(pdf_link = link)
        if len(x)==0:
            ok, header, table = pdf_to_order(data)
            if not ok:
                print(header)
                print(table)
                #raise Exception('Error') 
                print("Error")
            else:
                export_dok(link, row, header, table)
                print(row[3], "OK")


class Command(BaseCommand):
    help = 'Scan pdf files'

    def handle(self, *args, **options):
        lp=1
        s = requests.Session()
        s.headers.update({'Authorization': 'JhLjgpRZm7ALNPcxp2kiZrW0dwp-1mTh'})
        #r = s.get('https://pomoc.crhem.pl/api/rest/issues?filter_id=23&project_id=4&pagesize=10000')
        for page in range(1,100):
            print("PAGE: ", page)
            #r = s.get('https://pomoc.crhem.pl/api/rest/issues?filter_id=23&project_id=4&page=%d&pagesize=50' % page)
            r = s.get('http://mantis/api/rest/issues?filter_id=23&project_id=4&page=%d&pagesize=50' % page)
            try:
                x = r.json()
            except:
                break
            if 'issues' in x:
                tab = x['issues']
                if len(tab)==0:
                    break
                for pos in tab:
                    if 'attachments' in pos:
                        for f in pos['attachments']:
                            #r2 = s.get('https://pomoc.crhem.pl/api/rest/issues/%s/files/%s' % (pos['id'], f['id']) )
                            r2 = s.get('http://mantis/api/rest/issues/%s/files/%s' % (pos['id'], f['id']) )
                            x2 = r2.json()
                            if 'files' in x2:
                                files = x2['files']
                                for f2 in files:
                                    if 'content' in f2:
                                        process_row((pos['id'], f['id'], f['filename'], f2['content']))
                                        #print(lp, pos['id'], f['id'], f['filename'])
                                        lp+=1
