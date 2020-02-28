#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import time
from datetime import datetime
from py4j.java_gateway import JavaGateway
from py4j.java_gateway import GatewayParameters
from py4j.java_gateway import CallbackServerParameters
from py4j.java_gateway import launch_gateway
import socket
import os
from contextlib import closing

from .config import g_config

MIN_GATEWAY_PORT = 9500
MAX_GATEWAY_PORT = 9600

_gateway = None


def set_java_gateway(gateway):
    global _gateway
    _gateway = gateway


def get_java_gateway():
    global _gateway
    if _gateway is None:
        from pyalink.alink.py4j_util import LocalJvmBridge
        _gateway = LocalJvmBridge.inst().gateway
    return _gateway


def get_java_class(name):
    return _gateway.jvm.__getattr__(name)


def getAllJarFiles():
    global g_config
    alink_deps_dir = g_config["alink_deps_dir"]
    flink_home = g_config["flink_home"]

    ret = []
    ret += [os.path.join(alink_deps_dir, x) for x in
            os.listdir(alink_deps_dir) if x.endswith('.jar')]
    ret += [os.path.join(flink_home, 'lib', x) for x in
            os.listdir(os.path.join(flink_home, 'lib'))
            if x.endswith('.jar')]

    from pyalink.alink.utils import has_pyflink
    if has_pyflink():
        ret += [os.path.join(flink_home, 'opt', x) for x in
                os.listdir(os.path.join(flink_home, 'opt'))
                if x.endswith('.jar') and x.startswith("flink-python")]
    return ret


def stop_subprocess(process):
    process.terminate()
    st = datetime.now()
    while process.poll() is None:
        if (datetime.now() - st).total_seconds() > 3:
            process.kill()
            break
        time.sleep(50.0 / 1000.0)
    return process.poll()


def is_free(ip):
    pass


def is_available(ip, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        try:
            sock.bind((ip, port))
            return True
        except:
            return False


def is_available2(ip, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        try:
            res = sock.connect_ex((ip, port))
            return res != 0
        except:
            return True


def find_open_ports(ip, lo, hi):
    port = lo
    while port < hi:
        if is_available(ip, port):
            return port
        port += 1
    return None


class JavaDataSourceWrapper(object):
    def __init__(self, ds):
        self.ds = ds

    def check(self):
        return self.ds.check()

    def list_tables(self, name_prefix='', max_size=100):
        return self.ds.listTables(name_prefix, max_size)

    def get_table_data(self, table_name, max_size=100):
        data = self.ds.getTableData(table_name, max_size)
        import pandas
        return pandas.DataFrame.from_records(
            [tuple(x) for x in data.records],
            columns=tuple(data.colNames))

    def has_table(self, table_name):
        return self.ds.getDB().hasTable(table_name)

    def drop_table(self, table_name):
        return self.ds.getDB().dropTable(table_name)

    def get_column_names(self, table_name):
        return [x for x in self.ds.getDB().getColNames(table_name)]

    def get_table_schema(self, table_name):
        ts = self.ds.getDB().getTableSchema(table_name)
        return ([x for x in ts.getColNames()],
                [x.toString() for x in ts.getTypes()])

    def execute(self, sql):
        return self.ds.getDB().execute(sql)

    def name(self):
        return self.ds.getName()


class LocalJvmBridge(object):
    _bridge = None

    def __init__(self):
        self.process = None
        self.gateway = None
        self.app = None
        pass

    @classmethod
    def inst(cls):
        if cls._bridge is None:
            cls._bridge = LocalJvmBridge()
            cls._bridge.init()
        return cls._bridge

    def init(self):
        # port = find_open_ports('127.0.0.1', MIN_GATEWAY_PORT, MAX_GATEWAY_PORT)
        # import sys
        self._port = launch_gateway(
            port=0, javaopts=[], die_on_exit=True, daemonize_redirect=True,
            classpath=os.pathsep.join(getAllJarFiles())
        )
        print('JVM listening on 127.0.0.1:{}'.format(self._port))
        # self.process = subprocess.Popen([START_GATEWAY_CMD, '-P', str(port)])
        self.gateway = JavaGateway(
            gateway_parameters=GatewayParameters(port=self._port, auto_field=True),
            start_callback_server=False)
        # self._python_port = self.gateway.get_callback_server().get_listening_port()
        # print('Python listening on 127.0.0.1:{}'.format(self._python_port))
        # self.gateway.java_gateway_server.resetCallbackClient(
        #     self.gateway.java_gateway_server.getCallbackClient().getAddress(),
        #     self._python_port)
        self.app = self.gateway.jvm.com.alibaba.alink.python.AlinkDBMain()

    def close(self):
        # if self.app is None:
        #     return
        # self.gateway.detach(self.app)
        # self.app = None
        # self.gateway.close_callback_server()
        self.gateway.close()
        # self.gateway.shutdown_callback_server()
        self.gateway.shutdown()
        # stop_subprocess(self.process)

    def _make_db(self, db_type, db_config):
        ds = self.gateway.jvm.com.alibaba.alink.executor.datasource
        return ds.DataSourceFactory.MakeDataSource(db_type, db_config)

    def get_datasource(self, db_type, db_config):
        return JavaDataSourceWrapper(self._make_db(db_type, db_config))

    def validate_db(self, db_type, config):
        return self._make_db(db_type, config).check()

    def list_tables(self, db_type, db_config, name_prefix, max_size=100):
        assert isinstance(db_type, (str,))
        assert isinstance(db_config, (str,))
        assert isinstance(name_prefix, (str,))
        assert isinstance(max_size, (int,))
        return [x for x in self.app.listTables(db_type, db_config, name_prefix, max_size)]

    def has_table(self, db_type, db_config, table_name):
        return self._make_db(db_type, db_config).getDB().hasTable(table_name)

    def get_column_names(self, db_type, db_config, table_name):
        return [x for x in
                self._make_db(db_type, db_config).getDB().getColNames(table_name)]

    def get_column_types(self, db_type, db_config, table_name):
        return [x for x in self.app.getColTypes(db_type, db_config, table_name)]

    def execute(self, db_type, db_config, cmd):
        return self.app.execute(db_type, db_config, cmd)

    def get_table_data(self, db_type, db_config, table_name, max_size=100):
        data = self.app.getTableData(db_type, db_config, table_name, max_size)
        import pandas
        return pandas.DataFrame.from_records(
            [tuple(x) for x in data.records],
            columns=tuple(data.colNames))

    def submit_job(self, config_json, plan_json, cores=2, memory=4096, extra=None):
        return self.app.submitJob(config_json, plan_json, cores, memory, extra)

    def get_status(self, config_json, job_id):
        return self.app.getStatus(config_json, job_id)

    def get_logs(self, config_json, job_id, offset, limit=100):
        x = self.app.getLog(config_json, job_id, offset, limit)
        return [int(x.offset), [a for a in x.data]]

    pass
