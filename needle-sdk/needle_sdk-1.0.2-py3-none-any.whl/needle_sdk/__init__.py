# Copyright (c) 2020, Varlogix Technologies
# All rights reserved.
# Our terms: https://needle.sh/terms

import requests
jk=None
jV=False
xY=print
xj=open
xc=enumerate
xC=True
xM=Exception
xu=str
xv=type
xW=len
xl=ImportError
xE=getattr
jp=requests.post
import json
jz=json.loads
jR=json.dumps
import time
jy=time.sleep
import threading
jd=threading.Thread
jX=threading.local
import platform
jO=platform.system
import re
jA=re.IGNORECASE
jK=re.compile
import importlib
jq=importlib.find_loader
class jJ:
 Y=[]
 j=''
 x=''
 c=''
 C=''
 M=''
 u=''
 v=''
class jg:
 W=''
 l=''
 E=jk
 e=jV
class jL:
 D='1.0.0'
 T=''
 n=''
 h=''
 H='python'
 b=''
 Q=''
 U={}
 N=jV
 B=[]
 P=0
 t=[]
 f=[]
 F=jV
 S=jV
 G=[]
 e=jV
 a=jk
 I=jk
 o=jk
 s=jk
 r=jV
 def __init__(m,J):
  if m.YA():
   m.debug_mode=J
  else:
   xY("Needle.sh error: Web framework not supported. Stopping agent.")
   return
  try:
   g=m.project_dir+'/needle_settings.ini'
   with xj(g)as fp:
    for L,YQ in xc(fp):
     if YQ[0]!='#':
      w,i=YQ.strip().split('=')
      if w=='app_id':m.app_id=i
      if w=='api_key':m.api_key=i
      if w=='server_url':m.server_url=i
      if w=='test_mode':
       if i=='0':
        m.test_mode=jV
       elif i=='1':
        m.test_mode=xC
        xY('Needle.sh: Agent in Test Mode...')
      if m.debug_mode:xY(w,'=',i)
  except xM as e:
   p=xu(e)
   m.Yq('Error opening settings INI file',p)
  if m.app_id=='' or m.api_key=='':
   xY("Needle.sh error: App ID or API key incorrect. Stopping agent.")
   return
 def YA(m):
  R=jV
  try:
   from django.conf import settings
   m.framework='django'
   m.project_dir=settings.BASE_DIR
   R=xC
  except xM as e:
   pass
  return R
 def Yq(m,error,p):
  if m.debug_mode:xY('Needle.sh: Error! ',error)
  m.errors.append({'platform':m.platform,'error':error,'error_data':p})
 def Yk(m,Yn,reason,YL,z,y,req_data):
  z,y=m.jN(z,y)
  X={}
  X['type']=Yn
  X['reason']=reason
  X['arg_type']=YL
  X['arg_name']=z
  X['arg_value']=y
  X['client_ip']=req_data.remote_addr
  X['http_method']=req_data.request_method
  X['server']=req_data.http_host
  X['path']=req_data.path_info
  X['user_agent']=req_data.http_user_agent
  if m.debug_mode:xY('Adding incident: ',X)
  m.mal_requests.append(X)
 def YV(m,xv,package,method):
  d={'type':xv,'package':package,'method':method}
  if not(d in m.modules_used):m.modules_used.append(d)
 def jY(m):
  O=0
  K=0
  A=0
  try:
   while xC:
    if O==0:
     m.jM()
    if m.app_active and(m.total_requests>0 or xW(m.mal_requests)>0):
     m.jC()
    if m.app_active and K==0 and(xW(m.errors)>0):
     m.jc('errors')
    if m.app_active and A==0 and(xW(m.modules_used)>0):
     m.jc('modules_used')
    O+=1
    K+=1
    A+=1
    if O==1:O=0
    if K==1:K=0
    if A==10:A=0
    jy(30)
  except xM as e:
   p=xu(e)
   m.Yq('Error while sending req data',p)
 def jx(m):
  F=0
  if m.test_mode:F=1
  a=0
  if m.jh():a=1
  q={'app_id':m.app_id,'api_key':m.api_key,'test_mode':F,'libinjec':a,'platform':m.platform,'framework':m.framework,'agent_version':m.agent_version}
  return q
 def jc(m,info):
  if m.debug_mode:xY('Needle.sh: Sending app info data')
  try:
   k=m.server_url+'/api/store_app_info'
   Y=m.jx()
   if info=='errors' and xW(m.errors)>0:
    Y['agent_errors']=m.errors
    m.errors=[]
   if info=='modules_used' and xW(m.modules_used)>0:
    Y['modules_used']=m.modules_used
    m.modules_used=[]
   V=jR(Y)
   x=jp(k,data=V)
  except xM as e:
   p=xu(e)
   m.Yq('Error while sending app info',p)
 def jC(m):
  if m.debug_mode:xY('Needle.sh: Sending requests data')
  try:
   k=m.server_url+'/api/store_requests'
   Y=m.jx()
   if m.total_requests>0:
    Y['total_requests']=m.total_requests
    m.total_requests=0
   if xW(m.mal_requests)>0:
    Y['mal_requests']=m.mal_requests
    m.mal_requests=[]
   V=jR(Y)
   Yj=jp(k,data=V)
  except xM as e:
   p=xu(e)
   m.Yq('Error while sending req data',p)
   m.total_requests+=Y['total_requests']
   if xW(Y['mal_requests'])>0:
    a=Y['mal_requests']
    b=m.mal_requests
    a.extend(b)
    m.mal_requests=a
 def jM(m):
  if m.debug_mode:xY('Needle.sh: Getting app settings')
  try:
   Yx=m.server_url+'/api/get_app_settings'
   Y=m.jx()
   V=jR(Y)
   Yj=jp(Yx,data=V)
   if m.debug_mode:xY("Needle.sh: Received app settings = ",Yj.text)
   Yc=jz(Yj.text)
   m.settings=Yc['settings']
  except xM as e:
   p=xu(e)
   m.Yq('Error while fetching settings',p)
  try:
   if m.settings['active']==1:
    m.app_active=xC
    m.jE('basic',xC)
    if 'sqli' in m.settings and m.settings['sqli']['active']==1:
     m.jE('sqli',xC)
    else:
     m.jE('sqli',jV)
    if 'xss' in m.settings and m.settings['xss']['active']==1:
     m.jE('xss',xC)
    else:
     m.jE('xss',jV)
    if 'cmdi' in m.settings and m.settings['cmdi']['active']==1:
     m.jE('cmdi',xC)
    else:
     m.jE('cmdi',jV)
   elif m.settings['active']==0:
    m.app_active=jV
    m.jE('basic',jV)
    m.jE('sqli',jV)
    m.jE('xss',jV)
  except xM as e:
   p=xu(e)
   m.Yq('Error while instrumenting',p)
 def ju(m,W,l,E,e):
  YC=jV
  for YM,Yv in xc(m.instr_list):
   if Yv.sec_module==W and Yv.py_module==l:
    YC=xC
    m.instr_list[YM].is_instr=e
    break
  if not YC:
   Yu=jg()
   Yu.sec_module=W
   Yu.py_module=l
   Yu.orig_method=E
   Yu.is_instr=e
   m.instr_list.append(Yu)
  return e
 def jv(m,l):
  e=jV
  for Yv in m.instr_list:
   if Yv.py_module==l and Yv.is_instr:
    e=xC
    break
  return e
 def jW(m,l):
  for Yv in m.instr_list:
   if Yv.py_module==l:
    return Yv.orig_method
 def jl(m,d):
  YW=jq('spam')
  Yl=YW is not jk
 def jE(m,W,e):
  YE=[{'sec_module':'basic','framework':'django','py_module':'django.core.handlers.base.BaseHandler.get_response'},{'sec_module':'xss','framework':'django','py_module':'django.template.loader.render_to_string'},{'sec_module':'sqli','framework':'','py_module':'mysql.connector.connect'},{'sec_module':'sqli','framework':'','py_module':'psycopg2.connect'},{'sec_module':'cmdi','framework':'','py_module':'os.system'},{'sec_module':'cmdi','framework':'','py_module':'os.popen'}]
  for Ye in YE:
   if Ye['sec_module']!=W:continue
   if Ye['framework']!='' and Ye['framework']!=m.framework:continue
   l=Ye['py_module']
   if e!=m.jv(l):
    if e:
     try:
      E=''
      if l=='django.core.handlers.base.BaseHandler.get_response':
       try:
        from django.core.handlers.base import BaseHandler
        E=BaseHandler.get_response
        BaseHandler.get_response=jP
       except xl:
        pass
      if l=='django.template.loader.render_to_string':
       try:
        import django.template.loader
        E=django.template.loader.render_to_string
        django.template.loader.render_to_string=jf
       except xl:
        pass
      if l=='mysql.connector.connect':
       try:
        import mysql.connector
        E=mysql.connector.connect
        mysql.connector.connect=jr
       except xl:
        pass
      if l=='psycopg2.connect':
       try:
        import psycopg2
        E=psycopg2.connect
        psycopg2.connect=jm
       except xl:
        pass
      if l=='os.system':
       try:
        import os
        E=os.system
        os.system=jG
       except xl:
        pass
      if l=='os.popen':
       try:
        import os
        E=os.popen
        os.popen=ja
       except xl:
        pass
      m.ju(W,l,E,xC)
     except xM as e:
      p=xu(e)
      m.Yq('Error while instrumenting module: '+l,p)
    else:
     try:
      E=''
      if l=='django.core.handlers.base.BaseHandler.get_response':
       try:
        from django.core.handlers.base import BaseHandler
        E=m.jW(l)
        BaseHandler.get_response=E
       except xl:
        pass
      if l=='django.template.loader.render_to_string':
       try:
        import django.template.loader
        E=m.jW(l)
        django.template.loader.render_to_string=E
       except xl:
        pass
      if l=='mysql.connector.connect':
       try:
        import mysql.connector
        E=m.jW(l)
        mysql.connector.connect=E
       except xl:
        pass
      if l=='psycopg2.connect':
       try:
        import psycopg2
        E=m.jW(l)
        psycopg2.connect=E
       except xl:
        pass
      if l=='os.system':
       try:
        import os
        E=m.jW(l)
        os.system=E
       except xl:
        pass
      if l=='os.popen':
       try:
        import os
        E=m.jW(l)
        os.popen=E
       except xl:
        pass
      m.ju(W,l,E,jV)
     except xM as e:
      p=xu(e)
      m.Yq('Error while un-instrumenting module: '+l,p)
 def je(m):
  YD={}
  try:
   if m.app_active:
    if 'h_cj' in m.settings:
     YD['X-Frame-Options']=m.settings['h_cj']
    if 'h_xss' in m.settings:
     YD['X-XSS-Protection']=m.settings['h_xss']
    if 'h_mime' in m.settings:
     YD['X-Content-Type-Options']=m.settings['h_mime']
    if 'h_ref' in m.settings:
     YD['Referrer-Policy']=m.settings['h_ref']
  except xM as e:
   p=xu(e)
   m.Yq('Error getting security headers: ',p)
  return YD
 def jD(m):
  YT=jV
  Yn=''
  try:
   if m.app_active and 'xss' in m.settings and m.settings['xss']['active']==1:
    YT=xC
    Yn=m.settings['xss']['action']
  except xM as e:
   p=xu(e)
   m.Yq('Error checking module active: xss: ',p)
  return YT,Yn
 def jT(m):
  YT=jV
  Yn=''
  try:
   if m.app_active and 'cmdi' in m.settings and m.settings['cmdi']['active']==1:
    YT=xC
    Yn=m.settings['cmdi']['action']
  except xM as e:
   p=xu(e)
   m.Yq('Error checking module active: cmdi: ',p)
  return YT,Yn
 def jn(m):
  YT=jV
  Yn=''
  try:
   if m.app_active and 'sqli' in m.settings and m.settings['sqli']['active']==1:
    YT=xC
    Yn=m.settings['sqli']['action']
  except xM as e:
   p=xu(e)
   m.Yq('Error checking module active: sqli: ',p)
  return YT,Yn
 def jh(m):
  try:
   if m.libinjec:
    return m.libinjec
   if not m.libinjec:
    a=jk
    Yh=jO()
    if Yh=='Darwin':
     from needle_sdk.libinjection2.mac_x86_64 import libinjection
     a=libinjection
    elif Yh=='Linux':
     from needle_sdk.libinjection2.linux import libinjection
     a=libinjection
    elif Yh=='':
     m.Yq('Error getting libinjec module for platform: ','Unrecognised platform')
    m.libinjec=a
    return m.libinjec
  except xM as e:
   p=xu(e)
   m.Yq('Error getting libinjec module for platform: ',p)
   return jk
 def jH(m):
  try:
   if m.xss_pattern:
    return m.xss_pattern
   else:
    import os,sys,inspect
    YH=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    g=YH+'/js_event_list'
    Yb=''
    with xj(g)as fp:
     for L,YQ in xc(fp):
      YQ=YQ.strip()
      if YQ=='' or YQ[0]=='#':continue
      Yb+=YQ+'|'
    Yb=Yb.rstrip('|')
    Yb=r'\b('+Yb+r')\b'
    Yb=r'(<[\\s]*script[\\s]*[>]*|javascript:|javascript&colon;|FSCommand)|'+Yb
    YU=jK(Yb,jA)
    m.xss_pattern=YU
    return m.xss_pattern
  except xM as e:
   p=xu(e)
   m.Yq('Error getting XSS pattern:',p)
   return jk
 def jb(m):
  try:
   if m.cmdi_pattern:
    return m.cmdi_pattern
   else:
    import os,sys,inspect
    YH=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    g=YH+'/unix_cmd_list'
    Yb=''
    with xj(g)as fp:
     for L,YQ in xc(fp):
      YQ=YQ.strip()
      if YQ=='' or YQ[0]=='#':continue
      Yb+=YQ.rstrip('+')+'|'
    Yb=Yb.rstrip('|')
    Yb=r'(^|\s|;|&&|\|\||&|\|)('+Yb+r')($|\s|;|&&|\|\||&|\||<)|(\*|\?)'
    YU=jK(Yb,jA)
    m.cmdi_pattern=YU
    return m.cmdi_pattern
  except xM as e:
   p=xu(e)
   m.Yq('Error getting cmdi pattern:',p)
   return jk
 def jQ(m):
  try:
   import sys
   YN=sys.modules.keys()
   YB=[]
   for m in YN:
    YP=m.split('.')
    if YP[0]not in YB:
     YB.append(YP[0])
  except xM as e:
   p=xu(e)
   m.Yq('Error getting module list',p)
 def jU(m,module_id=''):
  Yt=''
  if m.show_blocked_message:
   Yf=''
   if module_id=='sqli':Yf='SQL injection'
   if module_id=='xss':Yf='Cross-site Scripting(XSS)'
   if module_id=='cmdi':Yf='Command injection'
   Yt='Blocked by Needle.sh! Attack type: '+Yf
  return Yt
 def jN(m,z,y):
  try:
   import re
   YU=r'(\d[ -]*){13,16}'
      jA=re.IGNORECASE
      jK=re.compile
   YU=jK(YU,jA)
   YF=['password','passwd','api_key','apikey','access_token','secret','authorization']
   if xW(YU.findall(y))>0 or z in YF:
    y='[Sensitive data removed by Needle.sh]'
  except xM as e:
   p=xu(e)
   m.Yq('Error while checking sensitive data',p)
  return z,y
YS=jk
YG=jX()
def jB(debug=jV,show_blocked_message=jV):
 xY("Starting Needle.sh agent")
 global YS
 YS=jL(debug)
 YS.show_blocked_message=show_blocked_message
 try:
  x=jd(target=YS.jY,args=(),daemon=xC)
  x.start()
 except xM as e:
  p=xu(e)
  YS.Yq('Error starting Wally thread to send data',p)
def jP(*Yr,**kwargs):
 l='django.core.handlers.base.BaseHandler.get_response'
 global YS
 try:
  YS.total_requests+=1
  Ya=jJ()
  YI=[]
  for Yo,Yw in Yr[1].GET.items():
   YI.append({'type':'get','name':Yo,'value':Yw})
  for Yo,Yw in Yr[1].POST.items():
   YI.append({'type':'post','name':Yo,'value':Yw})
  Ys=Yr[1].path.split('/')
  for p in Ys:
   YI.append({'type':'path','name':'path','value':p})
  Ya.data=YI
  Ya.remote_addr=Yr[1].META['REMOTE_ADDR']
  Ya.request_method=Yr[1].META['REQUEST_METHOD']
  Ya.http_host=Yr[1].META['HTTP_HOST']
  Ya.path_info=Yr[1].META['PATH_INFO']
  Ya.http_user_agent=Yr[1].META['HTTP_USER_AGENT']
  YG.req_data=Ya
  Ym=YS.jW(l)(*Yr,**kwargs)
  YJ=YS.je()
  for i,(Yo,Yw)in xc(YJ.items()):
   Ym[Yo]=Yw
  return Ym
 except xM as e:
  p=xu(e)
  YS.Yq('Error while adding request data to thread storage',p)
def jt(Yi):
 global YS
 Yg=jV
 YL=''
 z=''
 y=''
 try:
  a=YS.jh()
  for Yv in YG.req_data.data:
   Yw=Yv['value']
   if Yw=='':continue
   if a:
    Yc=a.xss(Yw)
    if Yc==1:
     if Yi.find(Yw)>-1:
      Yg=xC
      YL=Yv['type']
      z=Yv['name']
      y=Yv['value']
      return Yg,YL,z,y
   else:
    I=YS.jH()
    if I:
     if xW(I.findall(Yw))>0:
      if Yi.find(Yw)>-1:
       Yg=xC
       YL=Yv['type']
       z=Yv['name']
       y=Yv['value']
       return Yg,YL,z,y
    else:
     YS.Yq('Error checking XSS:','XSS pattern unavailable')
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking XSS:',p)
 return Yg,YL,z,y
def jf(*Yr,**kwargs):
 l='django.template.loader.render_to_string'
 global YS
 try:
  YS.YV('xss','django.template.loader','render_to_string')
  Yi=YS.jW(l)(*Yr,**kwargs)
  if YG.req_data.incident_action=='block':
   Yi=YS.jU(YG.req_data.incident_module)
  Yp,Yn=YS.jD()
  if Yp:
   xY('Checking XSS...')
   Yg,YL,z,y=jt(Yi)
   if Yg:
    if YS.debug_mode:xY('Needle.sh: New Incident of type: XSS')
    if Yn=='block':
     Yi=YS.jU('xss')
    YS.Yk(Yn,'xss',YL,z,y,YG.req_data)
  return Yi
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking reflected XSS',p)
def jF(Yz):
 global YS
 Yg=jV
 YL=''
 z=''
 y=''
 try:
  o=YS.jb()
  if o:
   for Yv in YG.req_data.data:
    Yw=Yv['value']
    if Yw=='':continue
    YR=['\'','"','\\','$@']
    for c in YR:
     Yw=Yw.replace(c,'')
     Yz=Yz.replace(c,'')
    if Yw=='':continue
    if xW(o.findall(Yw))>0:
     if Yz.find(Yw)>-1:
      Yg=xC
      YL=Yv['type']
      z=Yv['name']
      y=Yv['value']
      return Yg,YL,z,y
  else:
   YS.Yq('Error checking command injection:','Unavailable cmdi pattern')
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking command injection',p)
 return Yg,YL,z,y
def jS(l,*Yr,**kwargs):
 global YS
 YS.YV('cmdi','',l)
 try:
  Yy,Yn=YS.jT()
  if Yy:
   Yg,YL,z,y=jF(Yr[0])
   if Yg:
    if YS.debug_mode:xY('Needle.sh: New Incident of type: Command injection')
    if Yn=='block':
     Yr=('',)
     YG.req_data.incident_action='block'
     YG.req_data.incident_module='cmdi'
    YS.Yk(Yn,'cmdi',YL,z,y,YG.req_data)
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking command injection',p)
 return YS.jW(l)(*Yr,**kwargs)
def jG(*Yr,**kwargs):
 try:
  l='os.system'
  return jS(l,*Yr,**kwargs)
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking command injection',p)
def ja(*Yr,**kwargs):
 try:
  l='os.popen'
  return jS(l,*Yr,**kwargs)
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking command injection',p)
def jI(query):
 global YS
 Yg=jV
 YL=''
 z=''
 y=''
 xY('Checking SQL injection...')
 try:
  a=YS.jh()
  for Yv in YG.req_data.data:
   Yw=Yv['value']
   if Yw=='':continue
   if a:
    Yc=a.sqli(Yw,'')
    if Yc==1:
     if query.find(Yw)>-1:
      Yg=xC
      YL=Yv['type']
      z=Yv['name']
      y=Yv['value']
      YG.req_data.incident_action='block'
      YG.req_data.incident_module='sqli'
      return Yg,YL,z,y
   else:
    YU=jK(r'\b(select|update|insert|alter|create|drop|delete|merge|union|show|exec|or|and|order|sleep|having)\b|(&&|\|\|)',jA)
    if xW(Yw.split())>1 and xW(YU.findall(Yw))>0:
     Yg=xC
     YL=Yv['type']
     z=Yv['name']
     y=Yv['value']
     YG.req_data.incident_action='block'
     YG.req_data.incident_module='sqli'
     return Yg,YL,z,y
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking SQL injection:',p)
 return Yg,YL,z,y
def jo(*Yr,**kwargs):
 global YS
 YS.YV('sqli','mysql.connection.cursor','execute')
 try:
  YX,Yn=YS.jn()
  if YX:
   Yg,YL,z,y=jI(Yr[0])
   if Yg:
    if YS.debug_mode:xY('Needle.sh: New Incident of type: SQL injection')
    if Yn=='block':
     Yr=('-- Query blocked by Needle.sh agent (Possible SQL injection)',)
    YS.Yk(Yn,'sqli',YL,z,y,YG.req_data)
 except xM as e:
  p=xu(e)
  YS.Yq('Error checking SQL injection',p)
 return YS.orig_sql_cursor_execute(*Yr,**kwargs)
class jw():
 def __init__(m,js):
  try:
   m.js=js
   YS.orig_sql_cursor_execute=m.js.execute
   m.execute=jo
  except xM as e:
   p=xu(e)
   YS.Yq('Error initialising cursor object:',p)
 def __getattr__(m,name):
  try:
   return xE(m.js,name)
  except xM as e:
   p=xu(e)
   YS.Yq('Error returning custom cursor method:',p)
class ji():
 def __init__(m,Yd):
  try:
   m.connection=Yd
  except xM as e:
   p=xu(e)
   YS.Yq('Error initialising custom SQL connection object:',p)
 def js(m,*Yr,**kwargs):
  try:
   YO=m.connection.cursor(*Yr,**kwargs)
   return jw(YO)
  except xM as e:
   p=xu(e)
   YS.Yq('Error getting cursor object from SQL connection:',p)
 def __getattr__(m,name):
  try:
   return xE(m.connection,name)
  except xM as e:
   p=xu(e)
   YS.Yq('Error returning custom connection method:',p)
def jr(*Yr,**kwargs):
 l='mysql.connector.connect'
 global YS
 try:
  YK=YS.jW(l)(*Yr,**kwargs)
  return ji(YK)
 except xM as e:
  p=xu(e)
  YS.Yq('Error in instrumented MySQL connect:',p)
def jm(*Yr,**kwargs):
 l='psycopg2.connect'
 global YS
 try:
  YK=YS.jW(l)(*Yr,**kwargs)
  return ji(YK)
 except xM as e:
  p=xu(e)
  YS.Yq('Error in instrumented psycopg2 connect:',p)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

