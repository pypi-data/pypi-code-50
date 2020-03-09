# encoding: utf-8
"""
##基于redis的AES加解密工具包

2/4/2020   Bruce  0.8.2   初始版本<br/>
2/5/2020   Bruce  0.8.3   补充调用及配置说明，更新引用方式<br/>
2/5/2020   Bruce  0.9.1   新增鉴权模块<br/>
3/9/2020   Bruce  0.9.8   bugfix<br/>

###使用方法：<br/>
####1、配置全局变量<br/>
变量名|类型|用途|示例
REDIS_ADDRESS|字符串|redis服务器地址,需要带上ip、端口、库号|127.0.0.1:6379/1
COMMON_SALT|字符串|解密密钥|0648ea5562efffee
APPLICATION_NAME|字符串|cad应用名|mms
APP_CONFIG_PREFIX|字符串|cad配置前缀|app-config

####2、引入模块<br/>
from cad.cad_util import CadUtil  # 数据获取模块
from cad.app_config_util import AppConfigUtil  # 用户鉴权模块

####3、使用<br/>
`cad_util = CadUtil()`<br/>
`res = util.get(ak)`<br/>

ak为应用对应的ak键<br/>
res 即得到的解析结果<br/>
结果格式如下<br/>
`{
    "ak": "0648ea5562efffee",
    "sk": "1e058d312eb61448",
    "permissions": {
        "app_1": ["auth_1", "auth_2"],
        "app_2': ["auth_3", "auth_4"]
    }
}`
格式说明:<br/>
- ak: 字符串,应用的ak
- sk: 字符串,应用的sk
- permissions: 字典,应用的权限清单
  - permissions的每个键为该ak所拥有的其他应用的权限的应用名称
  - permissions每个键的值为该ak所拥有的对应应用的权限列表


`app_config_util = AppConfigUtil()pp_id`<br/>
校验ak是否有某应用的某个权限权限
app_config_util.check(ak, sk, auth_code)
校验ak是否有某应用的任意权限
app_config_util.check(ak,sk)

参数说明：<br/>
- ak: 传入的ak
- sk: 传入的sk
- app_id: 判断ak是否有该应用的权限
- auth_code: 判断ak是否有app下auth_code的权限，如果不传则判断ak是否有app的任意权限

结果说明：<br/>
True: 校验成功
False: 校验失败，原因如下：
- aksk不匹配
- ak没有对应app的权限
- ak没有对应app的auth_code权限
抛出异常CadException：<br/>
- ak不存在
"""
import sys
from setuptools import setup, find_packages
import cad

SHORT = 'cache aes decrypter'

if sys.platform == 'win32':
    setup(
        name='cad',
        version=cad.__version__,
        packages=find_packages(),
        install_requires=[
            'requests', 'redis', 'dynaconf', 'pycryptodome'
        ],
        long_description_content_type="text/markdown",
        url='',
        author=cad.__author__,
        author_email=cad.__email__,
        classifiers=[
            'Programming Language :: Python :: 3',
        ],
        include_package_data=True,
        package_data={'': ['*.py', '*.pyc']},
        zip_safe=False,
        platforms='any',

        description=SHORT,
        long_description=__doc__,
    )
else:
    setup(
        name='cad',
        version=cad.__version__,
        packages=find_packages(),
        install_requires=[
            'requests', 'redis', 'dynaconf', 'pycrypto'
        ],
        long_description_content_type="text/markdown",
        url='',
        author=cad.__author__,
        author_email=cad.__email__,
        classifiers=[
            'Programming Language :: Python :: 3',
        ],
        include_package_data=True,
        package_data={'': ['*.py', '*.pyc']},
        zip_safe=False,
        platforms='any',

        description=SHORT,
        long_description=__doc__,
    )
