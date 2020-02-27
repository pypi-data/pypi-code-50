import os
import jaydebeapi
import jpype

jdbc_driver_name = "com.qubole.jdbc.jdbc41.core.QDriver"
jdbc_jar_path = os.environ.get('QUBOLE_JDBC_JAR_PATH')


def return_dbapi():
    if jpype.isJVMStarted() and not jpype.isThreadAttachedToJVM():
        jpype.attachThreadToJVM()
        jpype.java.lang.Thread.currentThread().setContextClassLoader(
            jpype.java.lang.ClassLoader.getSystemClassLoader())
    return jaydebeapi


def check_env():
    if jdbc_jar_path is None:
        raise Exception('Please set the QUBOLE_JDBC_JAR_PATH environment variable pointing to JDBC Jar location with absolute path')


def create_conn(url, dsi):
    if url is not None:
        driver = jdbc_jar_path
        driver_args = []
        cargs = (jdbc_driver_name, create_jdbc_url(url, dsi), driver_args, driver)
        cparams = {}
        return [cargs, cparams]


def create_jdbc_url(url, dsi):
    url_str = url.__to_string__().split('?')
    params = str(url_str[1]).replace('&', ';')
    if str(dsi) == 'presto':
        jdbc_url = "jdbc:qubole://presto/" + url.database + "?" + params
    elif str(dsi) == 'hive':
        jdbc_url = "jdbc:qubole://hive/" + url.database + "?" + params
    else:
        raise Exception('Invalid DSI. Only Presto and Hive supported')
    return jdbc_url
