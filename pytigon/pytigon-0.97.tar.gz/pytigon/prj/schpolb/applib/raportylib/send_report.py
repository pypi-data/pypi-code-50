# -*- coding: utf-8 -*-

from schreports.models import CommonGroup
from django.conf import settings
from django.db import connection
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from pytigon_lib.schparser.html_parsers import SimpleTabParserBase
from pytigon_lib.schdjangoext.render import render_doc


import io
import zipfile
import datetime
import requests

import logging
logger = logging.getLogger("pytigon_task")    

MAIL_CONTENT = """
W załączeniu raport odświeżany i wysyłany automatycznie. W razie uwag proszę o kontakt z osobami:
- Sławomir Chołaj (slawomir.cholaj@polbruk.pl) - 502 620 952
- Robert Cmiel (robert.cmiel@polbruk.pl) - 694 485 136

Polbruk S.A. Siedziba Spółki: 80-299 Gdańsk, ul. Nowy Świat 16 c, tel. 58 554 97 45, fax 58 554 59 50
NIP: 584-025-35-91 | Sąd Rejonowy Gdańsk-Północ w Gdańsku, VII Wydz. Gospodarczy KRS, KRS: 0000062419 |Regon: 001388727 | Wysokość kapitału zakładowego: 31 766 250,00 zł
Otrzymana przez Panią / Pana wiadomość oraz załączone do niej pliki stanowią tajemnicę Przedsiębiorstwa i są przeznaczone tylko dla wymienionych adresatów. 
Jeżeli nie są Państwo zamierzonym odbiorcą, proszę poinformować o tym fakcie nadawcę oraz usunąć wiadomość ze swojego systemu. Nie powinni Państwo również nikomu ujawniać otrzymanych 
informacji ani sporządzać / zachowywać / dystrybuować żadnej kopii otrzymanych informacji. | This message and any attachments are confidential as a business secret and are intended solely for the 
use of the individual or entity to whom they are addressed. If you are not the intended recipient, please telephone or e-mail the sender and delete this message and any attachment from your system. 
Also, if you are not the intended recipient you should not disclose the content or take / retain / distribute any copies. 
Zanim wydrukujesz wiadomość - pomyśl o środowisku. Please consider the environment before printing out this e-mail.
"""

import os
import pendulum
from pytigon_lib.schfs.vfstools import get_temp_filename
from pytigon_lib.schtools.process import py_run


#date
#today
#start_of_year
#end_of_year
#start_of_month
#end_of_month
#start_of_last_month
#end_of_last_month
#start_of_next_month
#end_of_last_month

def _d2s(date):
    return date.isoformat()[:10].replace('-','').replace('.','')
    
def _replace(s, date, param):
    ret = s
    date_alt = date.add(days=-15)
    replace_tab = (
        ('date', _d2s(date)), 
        ('today', _d2s(date)), 

        ('start_of_year', _d2s(date_alt.replace(month=1, day=1))), 
        ('end_of_year', _d2s(date_alt.replace(year=date_alt.year+1, month=1, day=1).add(days=-1))), 
        
        ('start_of_current_year', _d2s(date.replace(month=1, day=1))), 
        ('end_of_current_year', _d2s(date.replace(year=date.year+1, month=1, day=1).add(days=-1))), 
        
        ('start_of_month', _d2s(date.replace(day=1))), 
        ('end_of_month', _d2s(date.replace(day=1).add(months=1).add(days=-1))), 

        ('start_of_last_month', _d2s(date.replace(day=1).add(months=-1))), 
        ('end_of_last_month', _d2s(date.replace(day=1).add(days=-1))), 

        ('start_of_next_month', _d2s(date.replace(day=1).add(months=1))), 
        ('end_of_next_month', _d2s(date.add(months=2).replace(day=1).add(days=-1))), 
        
        ('param', param),
    )
    for pos in replace_tab:
        d1 = pos[1]
        d2 = d1[:4]+'-'+d1[4:6]+'-'+d1[6:]
        ret = ret.replace('[['+pos[0]+'_str]]', d2)
        ret = ret.replace('{{'+pos[0]+'_str}}', d2)
        ret = ret.replace('[['+pos[0]+']]', d1)
        ret = ret.replace('{{'+pos[0]+'}}', d1)
    return ret
    
    
def gen_report(report_name, date=None, report_type=None, destination=None, date_gen=None):
    reports = CommonGroup.objects.filter(group_def_name='SimpleReport', title=report_name)
    if len(reports)!=1:
        return None
    report = reports[0]

    logger.info(f"Start report: {report_name}")

    if report.json_code:
        exec(report.json_code)

    fun = locals().get('init', None)
    if fun:
        x = fun()
        if 'date_gen' in x:
            date_gen = x['date_gen']

    ret_files = []

    if date_gen == None:
        date_gen = pendulum.now()
    if date==None:
        date = date_gen
    #else:
    #    date = pendulum.datetime(date)
    
    date_gen_str = date_gen.isoformat()[:10]
    datetime_gen_str = date_gen.isoformat()[:16].replace('T',' ')

    date_gen_year = date_gen_str[:4]
    date_gen_month = date_gen_str[5:7]
    date_gen_id = date_gen_str[:10].replace('-','').replace('.','')
    
    param=""
    
    if not report_type:
        report_type = report.json_rep_type.split('.')[-1].strip()

    if not destination:
        destination = report.json_dest.split('.')[0].strip()

    columns = report.json_columns.split(';')
    width_sum = 0
    columns2 = []
    width = []
    for pos in columns:
        c = pos.split(":")
        columns2.append(c[0])
        if len(c)>1:
            try:
                w = int(c[1])
            except:
                w=0
        else:
            w = 0
        width.append(w)
        width_sum+=w

    if width_sum<100:
        c = 0
        for pos in width:
            if pos==0:
                c+=1
        if c>0:
            dx = int((100-width_sum)/c)
            width2 = []
            for pos in width:
                if pos==0:
                    width2.append(dx)
                else:
                    width2.append(pos)
            width = width2

    columns = []
    for i in range(len(columns2)):
        columns.append((columns2[i], width[i]))

    if 'select' in report.json_mail.lower():
        sel = _replace(report.json_mail, date, "")
        if 'mysql' in sel:
            cursor = connection.cursor()
            cursor.execute(sel)
            parameters=cursor.fetchall()
        elif 'http' in sel and '://' in sel:
            r = requests.get(sel)
            p = r.text
            parser = SimpleTabParserBase()
            parser.feed(p)
            parameters = parser.tables[0][1:]
        else:
            with settings.DB as db:
                db.execute(sel)
                parameters=db.fetchall()
    else:
        parameters = ( ('', report.json_mail), )

    count = 0    
    for param, mail in parameters: 
        mail_to = [p for p in mail.split(';') if p]
        sel = _replace(report.json_select, date, param)
        desc = _replace(report.json_desc, date, param)
        desc2  = desc.split('<')[0]
        
        attachment_name = None

        if 'to_print' in sel:
            if param:
                address = sel + "&param="+param
            else:
                address = sel
            if report_type == 'pdf' and destination!='2':
                temp_file_name  = get_temp_filename()                
                base_path = os.path.dirname(os.path.abspath(__file__))
                pypath = os.path.join(base_path, "gen_pdf.py")
                ret_code, info_tab, err_tab = py_run([pypath, address, temp_file_name])
                if info_tab:
                    for pos in info_tab:
                        print("INFO: ", pos)
                if err_tab:
                    for pos in err_tab:
                        print("ERR: ", pos)                    
                with open(temp_file_name, "rb") as f:
                    content = f.read()
                doc_type = 'pdf'
                attrs = { 'Content-Type': 'application/pdf', 'Content-Disposition': '' }                
            else:
                pass
            
        else:    
            if 'mysql' in sel:
                cursor = connection.cursor()
                cursor.execute(sel)
                object_list=cursor.fetchall()
            elif 'http' in sel and '://' in sel:
                r = requests.get(sel)    
                p = r.text
                parser = SimpleTabParserBase()
                parser.feed(p)
                object_list = parser.tables[0][1:]
            else:
                with settings.DB as db:
                    if '$$$' in sel:
                        sel_list = sel.split('$$$')
                        object_list = []
                        for sel2 in sel_list:
                            if sel.strip():
                                db.execute(sel2)
                                ret=db.fetchall()
                                for pos in ret:
                                    object_list.append(pos)
                    else:
                        db.execute(sel)
                        object_list=db.fetchall()
            
            fun = locals().get('transform_object_list', None)
            if fun:
                object_list = fun(object_list, param, mail)
                    
            if len(object_list) <= 0 and not report.json_send_always:
                continue
                
            doc_type = 'html'
            template_names = ['raporty/formsimplereport_' + report_name, 'raporty/formsimplereport',]
            if report_type == 'pdf' and destination!='2':
                doc_type = 'pdf'
            elif report_type == 'odf' and destination!='2':
                doc_type = 'ods'
            elif report_type == 'xlsx' and destination!='2':
                doc_type = 'xlsx'
            elif report_type == 'txt':
                doc_type = 'txt'

            if len(object_list)>0 and len(object_list[0])> len(columns):
                colors = True
                sli="0:"+str(len(columns))
            else:
                sli=":"
                colors = False
                
            rep_dict = {
                "object_list": object_list, 'doc_type': doc_type, 'report_type': report_type, 'date': date, 
                'columns': columns,  'time_str': datetime_gen_str, 'report': report, 'year': date_gen_year, 'month': date_gen_month, 
                'colors': colors, 'sli': sli,  'param': param, 'template_names': template_names, 'description': desc
            }
            
            fun = locals().get('transform_context', None)
            if fun:
                fun(rep_dict, param, mail)
                            
            attrs, content = render_doc(rep_dict)
            
            if 'attachment_name' in rep_dict:
                attachment_name = rep_dict['attachment_name']
        
        if len(mail_to)>0:
            #mail_to=['slawomir.cholaj@polbruk.pl',]
            if destination=='1': #Mail (attachement)                
                mail = EmailMessage(desc2, MAIL_CONTENT, to=mail_to)
                mail.attach(attachment_name if attachment_name else f"{report_name}_{date_gen_id}.{doc_type}", content, attrs['Content-Type'])
                mail.send()
            elif destination=='2': #Mail (content)
                mail = EmailMultiAlternatives(desc2, MAIL_CONTENT, to=mail_to)
                if type(content) == bytes:
                    content = content.decode('utf-8')
                mail.attach_alternative(content, "text/html")
                mail.send()
            elif destination=='3': #User storage
                pass
            elif destination=='4': #Group storage
                pass
            count += 1
            
        if destination.startswith('5'): #Download
            if mail_to:
                x = ';'.join(mail_to)
            else:
                x = date_gen_id
            ret_files.append((f"{report_name}_{x}.{doc_type}", content, attrs))            

    if ret_files:
        if len(ret_files) == 1:
            logger.info(f"End report: {report_name}, ret_files[0]")
            return ret_files[0]
        else:
            file_like_object = io.BytesIO()
            zipfileobj = zipfile.ZipFile(file_like_object, mode='w')
            for f in ret_files:
                zipfileobj.writestr(f[0], f[1])
            zipfileobj.close()
            file_like_object.seek(0)
            data = file_like_object.read()
            logger.info(f"End report: {report_name}, ret: data.zip")
            return ('data.zip', data, { 'Content-Type': 'application/zip', 'Content-Disposition': 'attachment; filename=data.zip;' } )
    else:
        logger.info(f"End report: {report_name}, ret: count")
        return count
