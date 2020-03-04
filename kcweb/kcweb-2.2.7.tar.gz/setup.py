
# python setup.py sdist upload
############################################# 
from setuptools import setup, find_packages,Extension
import os
confkcw={}
confkcw['name']='kcweb'								#项目的名称
confkcw['version']='2.2.7'							#项目版本
confkcw['description']='增加windos自定义python解释器'        #项目的简单描述
confkcw['author']='禄可集团-坤坤'  					 #名字
confkcw['author_email']='fk1402936534@qq.com' 	    #邮件地址
confkcw['maintainer']='坤坤' 						 #维护人员的名字
confkcw['maintainer_email']='fk1402936534@qq.com'    #维护人员的邮件地址
confkcw['url']=''
def get_file(folder='./',lists=[]):
    lis=os.listdir(folder)
    for files in lis:
        if not os.path.isfile(folder+"/"+files):
            if files!='__pycache__':
                lists.append(folder+"/"+files)
            get_file(folder+"/"+files,lists)
        else:
            pass
    return lists
b=get_file("kcweb",['kcweb'])
setup(
    name = confkcw["name"],
    version = confkcw["version"],
    description = confkcw["description"],
    author = confkcw["author"],
    author_email = confkcw["author_email"],
    maintainer = confkcw["maintainer"],
    maintainer_email = confkcw["maintainer_email"],
    url=confkcw['url'],
    packages =  b,
    # install_requires = ['pymongo==3.10.0','six==1.12.0','requests==2.22.0','watchdog==0.9.0','Mako==1.1.0','paramiko==2.6.0','webssh==1.4.5'], #第三方包
    install_requires = ['pymongo','Mako','requests','six','watchdog'], #第三方包
    package_data = {
        '': ['*.html', '*.js','*.css','*.jpg','*.png','*.gif'],
        'kcweb/utill/db/sqlitedata': ['*'],
        'kcweb/application/api/tpl': ['*']
    }
)