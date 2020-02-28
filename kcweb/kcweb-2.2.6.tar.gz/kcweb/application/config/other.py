# -*- coding: utf-8 -*-
from kcweb.config import *
#路由配置
route['default']=True #是否开启默认路由  默认路由开启后面不影响以下配置的路由，模块名/版本名/控制器文件名/方法名 作为路由地址   如：http://www.kcw.com/api/v1/index/index/
route['modular']=[{"www":"${modular}"},{"127":"${modular}"},{"192":"${modular}"}] #配置域名模块 配置后地址为：http://www.kcw.com/v1/index/index/  注意:如果使用的是代理服务器需要把代理名称设置为当前配置的域名，否则不生效
route['edition']='v1' #默认路由版本，配置后地址为 http://www.kcw.com/index/index/
route['files']='index' #默认路由文件 
route['funct']='index'  #默认路由函数
route['methods']=['POST','GET'] #默认请求方式
#sqlite配置
sqlite['db']='kcwlicuxweb' #sqlite数据库文件
