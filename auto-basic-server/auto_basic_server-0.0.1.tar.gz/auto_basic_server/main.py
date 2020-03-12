"""
文件名：main.py
Created on 2019年11月14日
@author: 梁彦鹏
"""
import sys
from flask import Flask
# from gevent.pywsgi import WSGIServer
from common.logger import log
from routes.autofile_blueprint import auto_file
from routes.autoproc_blueprint import auto_proc
from routes.autosys_blueprint import auto_sys
from routes.configuration_blueprint import configurate
from routes.timesync_blueprint import time_sync
from routes.sftputil_blueprint import sftp_util
app = Flask(__name__)
app.register_blueprint(auto_file)
app.register_blueprint(auto_proc)
app.register_blueprint(auto_sys)
app.register_blueprint(time_sync)
app.register_blueprint(configurate)
app.register_blueprint(sftp_util)

if sys.platform.startswith('win'):
    from routes.autogui_blueprint import auto_gui
    from routes.autoinput_blueprint import auto_input
    from routes.autoreg_blueprint import auto_reg
    from routes.autocfg_blueprint import auto_cfg
    app.register_blueprint(auto_gui)
    app.register_blueprint(auto_input)
    app.register_blueprint(auto_reg)
    app.register_blueprint(auto_cfg)


if __name__ == '__main__':
    log.info("开始运行BASIC_SERVER,端口:20000...")
    # http_server = WSGIServer(('0.0.0.0', 20000), app)
    # http_server.serve_forever()

    app.run(host='0.0.0.0', port=20000, debug=True)
