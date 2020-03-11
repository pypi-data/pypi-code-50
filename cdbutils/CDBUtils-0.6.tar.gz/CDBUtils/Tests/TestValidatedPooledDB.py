import threading
import sys
import time
from CDBUtils.ValidatedPooledDB import PooledDB
from threading import Thread, Timer
import cx_Oracle


# TNS = cx_Oracle.makedsn("127.0.0.1", '1521',"orcl")
# TNS = 127.0.0.1:1521/orcl
TNS = "LOCALORCL"


pool = PooledDB(cx_Oracle,
                user="zhangzx",
                password="Pwdasc123",
                dsn=TNS,
                mincached=3,
                maxcached=20,
                blocking=True,
                test_on_borrow=True,
                test_idle = True,
                maxconnections=50,
                max_wait_time=10
                )


class Dispacher(threading.Thread):
    def __init__(self, fun, *args, **kwargs):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.result = None
        self.error = None
        self.fun = fun
        self.args = args
        self.kwargs = kwargs

        self.start()

    def stop(self):
        try:
            print("testTimeout-into stop")
            self._stop()
        except Exception as e:
            print(e)

    def run(self):
        try:
            self.result = self.fun(*self.args, **self.kwargs)
        except Exception as e:
            print(e)
            self.error = sys.exc_info()


def test_fun(conn, sql, params=[]):
    try:
        cus = conn.cursor()
        print("testTimeout-sql"+sql)
        print("testTimeout222-params" + str(params), "现在的连接数", pool._connections)
        result_db = cus.execute(sql, params)
        result = result_db.fetchall()
        return_result = list()
        if len(result) > 0:
            key_list = [key[0] for key in result_db.description]
            for value in result:
                return_result.append(dict(zip(key_list, value)))
        return return_result
    except Exception as e:
        raise e
    finally:
        cus.close()


sql = "select username,count(username) as u_size from v$session where PROGRAM='python.exe' and username is not null  group by username"
params = []


def main_fun(time_out=1, connection=None):
    c = Dispacher(test_fun, conn=connection, sql=sql, params=params)
    c.join(time_out)
    if c.isAlive():
        c.stop()
        print("testTimeout-%s 现在的连接数%s" % (threading.currentThread().getName(),  pool._connections))
        connection.cancel()
        time.sleep(1)
        return "TimeOutError"
    elif c.error:
        return c.error[1]
    t = c.result
    return t


def start_check():
    connection = pool.connection()
    fun = main_fun(1, connection)
    print("testTimeout-返回结果%s" % str(fun))
    r = test_fun(conn=connection, sql=sql, params=params)
    connection.close()
    print("testTimeout-%s-试一下连接还能用吧-返回%s现在的连接数%s缓存连接%s" %
          (threading.currentThread().getName(), r, pool._connections, len(pool._idle_cache)))


def start_time():
    for i in range(100):
        Thread(target=start_check).start()
    time.sleep(20)
    print("testTimeout-%s现在的连接数%s_现在缓存的连接数%s" %
          (threading.currentThread().getName(), pool._connections, len(pool._idle_cache)))
    Timer(10, start_time).start()


if __name__ == '__main__':
    for i in range(3):
        threading.Thread(target=start_time()).start()
