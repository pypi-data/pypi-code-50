import pickle
import os
import shutil

ssql_name = 'default_sql'
slist_name = 'list0'
sposition_name = 'position0'
NSSea = 'nssea'
ADOea = 'adoea'
METea = 'metea'
cur = 0

try:
     os.mkdir('C:\\nssql')
except FileExistsError:
     pass

class _NanShanSQLOpenError(Exception):
     def __init__(self,value):
          self.value = value
     def __str__(self):
          return self.value

class _NanShanSQLChangeError(Exception):
     def __init__(self,value):
          self.value = value
     def __str__(self):
          return self.value

class _NanShanSQLEstablishError(Exception):
     def __init__(self,value):
          self.value = value
     def __str__(self):
          return self.value

class _NanShanSQLPasswordError(Exception):
     def __init__(self,value):
          self.value = value
     def __str__(self):
          return self.value

class _NanShanSQLExportError(Exception):
     def __init__(self,value):
          self.value = value
     def __str__(self):
          return self.value

class _NanShanSQLImportError(Exception):
     def __init__(self,value):
          self.value = value
     def __str__(self):
          return self.value

def cursor(name=1):
     global cur
     cur = name

def new_sql(sql_name='default_sql',password='None',existet=False):
     '''Make a new SQL'''
     global ssql_name
     ssql_name = sql_name
     try:
          os.mkdir('C:\\nssql\\'+ssql_name)
     except FileExistsError:
          if not existet:
               _NanShanSQLEstablishError('SQL \'%s\' already exist.' % sql_name)
     f = open('C:\\nssql\\%s_password.nssp' % sql_name,'w',encoding='utf-8')
     f.write(password)
     f.close()
     e = {}
     f = open('C:\\nssql\\%s_relation.nssrt' % sql_name,'wb')
     pickle.dump(obj=e,file=f)
     f.close()
     return ssql_name

def new_list(sql_name='default_sql',list_name='list0',existet=False,password='None'):
     '''Make a new list in a SQL'''
     global ssql_name
     global slist_name
     f = open('C:\\nssql\\%s_password.nssp' % sql_name)
     spassword = f.read()
     f.close()
     if spassword == 'None':
          ssql_name = sql_name
          slist_name = list_name
          try:
               os.mkdir('C:\\nssql\\'+ssql_name+'\\'+slist_name)
          except FileExistsError:
               if not existet:
                    _NanShanSQLEstablishError('SQL \'%s\' already exist.' % sql_name)
          return slist_name
     else:
          if password == spassword:
               ssql_name = sql_name
               slist_name = list_name
               try:
                    os.mkdir('C:\\nssql\\'+ssql_name+'\\'+slist_name)
               except FileExistsError:
                    if not existet:
                         _NanShanSQLEstablishError('SQL \'%s\' already exist.' % sql_name)
               return slist_name
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def new_position(sql_name='default_sql',list_name='list0',position_name='position0',data='NanShanSQL',password='None'):
     '''Add a position to a SQL list and add data to this position'''
     global sposition_name
     global ssql_name
     global slist_name
     f = open('C:\\nssql\\%s_password.nssp' % sql_name)
     spassword = f.read()
     f.close()
     if spassword == 'None':
          sposition_name = position_name
          ssql_name = sql_name
          slist_name = list_name
          f = open('C:\\nssql\\'+str(ssql_name)+'\\'+str(slist_name)+'\\'+str(sposition_name)+'.nsl','wb')
          pickle.dump(data,f)
          f.close()
     else:
          if password == spassword:               
               sposition_name = position_name
               ssql_name = sql_name
               slist_name = list_name
               f = open('C:\\nssql\\'+str(ssql_name)+'\\'+str(slist_name)+'\\'+str(sposition_name)+'.nsl','wb')
               pickle.dump(data,f)
               f.close()
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def close_sql(sql='default_sql'):
     '''Close the SQL and stop using it'''
     global ssql_name
     global slist_name
     global sposition_name
     global cur
     ssql_name = 'default_sql'
     slist_name = 'list0'
     sposition_name = 'position0'
     cur = 1

def open_sql(sql='default_sql',password='None'):
     '''Open a SQL to get data from it'''
     l = open('C:\\nssql\\%s_password.nssp' % sql)
     spassword = l.read()
     l.close()
     nsql = 'C:\\nssql\\' + sql
     if spassword == 'None':
          me = os.listdir(nsql)
          apl = {}
          tpl = []
          for i in me:
               apl[i] = {}
               mt = os.listdir('C:\\nssql\\'+sql+'\\'+i)
               for v in mt:
                    if not '.nssrt' in v:
                         try:
                              f = open('C:\\nssql\\'+sql+'\\'+i+'\\'+v,'rb')
                         except:
                              raise _NanShanSQLOpenError('Can not open the file \'%s\'.' % (i+'\\'+v))
                         try:
                              pl = pickle.load(f)
                         except:
                              pl = 'None'
                              raise _NanShanSQLOpenError('Can not load the data \'%s\'.' % (i+'\\'+v))
                         apl[i][v.replace('.nsl','')] = pl
                         f.close()
                    f = open('C:\\nssql\\'+sql+'_relation.nssrt','rb')
          a = pickle.load(f)
          f.close()
          tpl = [apl,a]
          return tpl
     else:
          if password == spassword:
               me = os.listdir(nsql)
               apl = {}
               tpl = {}
               for i in me:
                    apl[i] = {}
                    mt = os.listdir('C:\\nssql\\'+sql+'\\'+i)
                    for v in mt:
                         if not '.nssrt' in v:
                              try:
                                   f = open('C:\\nssql\\'+sql+'\\'+i+'\\'+v,'rb')
                              except:
                                   raise _NanShanSQLOpenError('Can not open the file \'%s\'.' % (i+'\\'+v))
                              try:
                                   pl = pickle.load(f)
                              except:
                                   pl = 'None'
                                   raise _NanShanSQLOpenError('Can not load the data \'%s\'.' % (i+'\\'+v))
                              apl[i][v.replace('.nsl','')] = pl
                              f.close()
               f = open('C:\\nssql\\'+sql+'_relation.nssrt','rb')
               a = pickle.load(f)
               f.close()
               tpl = [apl,a]
               return tpl
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def change_sql(sql_name='default_sql',list_name='list0',position_name='position0',new_data='NanShanSQL',password='None'):
     '''Change the data stored in any position of any list in a SQL'''
     f = open('C:\\nssql\\%s_password.nssp' % sql_name)
     spassword = f.read()
     f.close()
     if spassword == 'None':
          try:
               f = open('C:\\nssql\\'+sql_name+'\\'+list_name+'\\'+position_name+'.nsl','wb')
          except:
               raise _NanShanSQLOpenError('Can not open the file \'%s\'.' % sql_name+'\\'+list_name+'\\'+position_name)
          try:
               pickle.dump(new_data,f)
          except:
               raise _NanShanSQLChangeError('Can not change the data \'%s\'.' % sql_name+'\\'+list_name+'\\'+position_name+'--'+new_data)
     else:
          if password == spassword:
               try:
                    f = open('C:\\nssql\\'+sql_name+'\\'+list_name+'\\'+position_name+'.nsl','wb')
               except:
                    raise _NanShanSQLOpenError('Can not open the file \'%s\'.' % sql_name+'\\'+list_name+'\\'+position_name)
               try:
                    pickle.dump(new_data,f)
               except:
                    raise _NanShanSQLChangeError('Can not change the data \'%s\'.' % sql_name+'\\'+list_name+'\\'+position_name+'--'+new_data)
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def change_password(sql='default_sql',new_password='None'):
     ''' Change password of SQL'''
     f = open('C:\\nssql\\%s_password.nssp' % sql,'w',encoding='utf-8')
     f.write(new_password)
     f.close()

def new_relation(sql='default_sql',obj1='default_sql\\list0\\position0',obj2='default_sql\\list1\\position1',password='None'):
     '''Associate any location in the SQL with another location'''
     f = open('C:\\nssql\\%s_password.nssp' % sql)
     spassword = f.read()
     f.close()
     if spassword == 'None':
          f = open('C:\\nssql\\%s_relation.nssrt' % sql,'rb')
          a = pickle.load(f)
          f.close()
          a[obj1] = obj2
          a[obj2] = obj1
          f = open('C:\\nssql\\%s_relation.nssrt' % sql,'wb')
          pickle.dump(a,f)
          f.close()
     else:
          if password == spassword:
               f = open('C:\\nssql\\%s_relation.nssrt' % sql,'rb')
               a = pickle.load(f)
               f.close()
               a[obj1] = obj2
               a[obj2] = obj1
               f = open('C:\\nssql\\%s_relation.nssrt' % sql,'wb')
               pickle.dump(a,f)
               f.close()
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def open_relation(sql='default_sql',obj='default_sql\\list0\\position0',password='None'):
     '''Open other position relation with this position'''
     f = open('C:\\nssql\\%s_password.nssp' % sql)
     spassword = f.read()
     f.close()
     if spassword == 'None':
          f = open('C:\\nssql\\%s_relation.nssrt' % sql,'rb')
          q = pickle.load(f)
          f.close()
          qm = q[obj]
          f = open('C:\\nssql\\%s.nsl' % qm,'rb')
          met = pickle.load(f)
          f.close()
          return met
     else:
          if password == spassword:
               f = open('C:\\nssql\\%s_relation.nssrt' % sql,'rb')
               q = pickle.load(f)
               f.close()
               qm = q[obj]
               f = open('C:\\nssql\\%s.nsl' % qm,'rb')
               met = pickle.load(f)
               f.close()
               return met
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def del_sql(sql_name='default_sql',password='None'):
     '''Delete a SQL'''
     #print(sql_name)
     f = open('C:\\nssql\\%s_password.nssp' % sql_name)
     spassword = f.read()
     f.close()
     if spassword == 'None':
          ssql_name = 'default_sql'
          slist_name = 'list0'
          sposition_name = 'position0'
          cur = 1
          #print(sql_name)
          shutil.rmtree('C:\\nssql\\'+sql_name)
     else:
          if password == spassword:
               ssql_name = 'default_sql'
               slist_name = 'list0'
               sposition_name = 'position0'
               cur = 1
               #print(sql_name)
               shutil.rmtree('C:\\nssql\\'+sql_name)
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def export_sql(ea='nssea',sql_name='default_sql',file_position='D:\\',password='None'):
     '''Export SQL to file'''
     f = open('C:\\nssql\\%s_password.nssp' % sql_name)
     spassword = f.read()
     f.close()
     if spassword == 'None':
          if ea == 'nssea':
               f = open(file_position+sql_name+'.nss','wb')
          elif ea == 'adoea':
               f = open(file_position+sql_name+'.ado','wb')
          elif ea == 'metea':
               f = open(file_position+sql_name+'.met','wb')
          else:
               raise _NanShanSQLExportError('Cannot find this export algorithm.')
          try:
               pickle.dump(open_sql(sql_name,password),f)
          except:
               raise _NanShanSQLOpenError('Cannot open the SQL: %s' % sql_name)
          f.close()
     else:
          if password == spassword:
               if ea == 'nssea':
                    f = open(file_position+sql_name+'.nss','wb')
               elif ea == 'adoea':
                    f = open(file_position+sql_name+'.ado','wb')
               elif ea == 'metea':
                    f = open(file_position+sql_name+'.met','wb')
               else:
                    raise _NanShanSQLExportError('Cannot find this export algorithm.')
               try:
                    pickle.dump(open_sql(sql_name,password),f)
               except:
                    raise _NanShanSQLOpenError('Cannot open the SQL: %s' % sql_name)
               f.close()
          else:
               raise _NanShanSQLPasswordError('Password Error!')

def import_sql(file='D:\\default_sql.nss',sql_name='default_sql',existet=False,password='None'):
     '''Import an SQL file into a SQL group and use it to change the data in it'''
     f = open(file,'rb')
     try:
          data = pickle.load(f)
     except:
          raise _NanShanSQLImportError('File %s is not a valid file' % file)
     try:
          os.mkdir('C:\\nssql\\'+sql_name)
     except FileExistsError:
          if not existet:
               raise _NanShanSQLImportError('SQL \'%s\' already exist.' % sql_name)
     for i in data[0]:
          try:
               os.mkdir('C:\\nssql\\'+sql_name+'\\'+i)
          except FileExistsError:
               if not existet:
                    raise _NanShanSQLImportError('List \'%s\' already exist.' % i_name)
          for k in data[0][i]:
               ff = open('C:\\nssql\\'+sql_name+'\\'+i+'\\'+k+'.nsl','wb')
               pickle.dump(data[0][i][k],ff)
               ff.close()
     for i in data[1]:
          fff = open('C:\\nssql\\'+i+'_relation.nssrt','w',encoding='utf-8')
          fff.write(data[1][i])
          fff.close()
          fff = open('C:\\nssql\\'+data[1][i]+'_relation.nssrt','w',encoding='utf-8')
          fff.write(i)
          fff.close()
     f.close()
     
def del_every_sql():
     '''Delete all SQL in SQL group'''
     shutil.rmtree('C:\\nssql')
     os.mkdir('C:\\nssql')

if __name__ == '__main__':
     data00 = {'Name':'NanShan SQL.',\
               'Type':'NSPR',\
               'How There':'DS_L0_P0',\
               'data':'NANSHAN_SQL>_THE_TYPE;NSPR1++'}
     data01 = {'Name':'NanShan SQL.',\
               'Type':'NSUT',\
               'How There':'DS_L0_P1',\
               'data':' 	  	 		  	 		 	 		 	  	 	 		 	 '}
     data10 = {'Name':'NanShan SQL.',\
               'Type':'NSTE',\
               'How There':'DS_L1_P0',\
               'data':'NanShan SQL. The Type:NSPR!'}
     data11 = {'Name':'NanShan SQL.',\
               'Type':'NSHM',\
               'How There':'DS_L1_P1',\
               'data':'NSHMNSHMNSHMNSHMNSHMNSHM'}
     new_sql(existet=True)
     cursor(8)
     new_list(existet=True)
     new_list(list_name='list1',existet=True)
     new_position(data=data00)
     new_position(position_name='position1',data=data01)
     new_position(list_name='list1',data=data10)
     new_position(list_name='list1',position_name='position1',data=data11)
     change_password()
     print('000:'+str(open_sql()))
     change_sql()
     print('001:'+str(open_sql()))
     change_sql(new_data=data00)
     print('010:'+str(open_sql()))
     new_relation()
     export_sql()
     del_sql()
     import_sql(existet=True)
     print('011:'+str(open_sql()))
     export_sql()
     import_sql(existet=True)
     print('100:'+str(open_sql()))
     #new_relation()
     print('101:'+str(open_relation()))
     
