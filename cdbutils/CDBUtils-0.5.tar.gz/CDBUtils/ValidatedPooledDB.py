"""PooledDB - pooling for DB-API 2 connections.

Implements a pool of steady, thread-safe cached connections
to a database which are transparently reused,
using an arbitrary DB-API 2 compliant database interface module.

This should result in a speedup for persistent applications such as the
application server of "Webware for Python," without loss of robustness.

Robustness is provided by using "hardened" SteadyDB connections.
Even if the underlying database is restarted and all connections
are lost, they will be automatically and transparently reopened.
However, since you don't want this to happen in the middle of a database
transaction, you must explicitly start transactions with the begin()
method so that SteadyDB knows that the underlying connection shall not
be replaced and errors passed on until the transaction is completed.

Measures are taken to make the pool of connections thread-safe.
If the underlying DB-API module is thread-safe at the connection level,
the requested connections may be shared with other threads by default,
but you can also request dedicated connections in case you need them.

For the Python DB-API 2 specification, see:
    https://www.python.org/dev/peps/pep-0249/
For information on Webware for Python, see:
    https://cito.github.io/w4py/


Usage:

First you need to set up the database connection pool by creating
an instance of PooledDB, passing the following parameters:

    creator: either an arbitrary function returning new DB-API 2
        connection objects or a DB-API 2 compliant database module
    mincached: the initial number of idle connections in the pool
        (the default of 0 means no connections are made at startup)
    maxcached: the maximum number of idle connections in the pool
        (the default value of 0 or None means unlimited pool size)
    maxshared: maximum number of shared connections allowed
        (the default value of 0 or None means all connections are dedicated)
        When this maximum number is reached, connections are
        shared if they have been requested as shareable.
    maxconnections: maximum number of connections generally allowed
        (the default value of 0 or None means any number of connections)
    blocking: determines behavior when exceeding the maximum
        (if this is set to true, block and wait until the number of
        connections decreases, but by default an error will be reported)
    maxusage: maximum number of reuses of a single connection
        (the default of 0 or None means unlimited reuse)
        When this maximum usage number of the connection is reached,
        the connection is automatically reset (closed and reopened).
    setsession: an optional list of SQL commands that may serve to
        prepare the session, e.g. ["set datestyle to german", ...]
    reset: how connections should be reset when returned to the pool
        (False or None to rollback transcations started with begin(),
        the default value True always issues a rollback for safety's sake)
    failures: an optional exception class or a tuple of exception classes
        for which the connection failover mechanism shall be applied,
        if the default (OperationalError, InternalError) is not adequate
    ping: an optional flag controlling when connections are checked
        with the ping() method if such a method is available
        (0 = None = never, 1 = default = whenever fetched from the pool,
        2 = when a cursor is created, 4 = when a query is executed,
        7 = always, and all other bit combinations of these values)

    The creator function or the connect function of the DB-API 2 compliant
    database module specified as the creator will receive any additional
    parameters such as the host, database, user, password etc.  You may
    choose some or all of these parameters in your own creator function,
    allowing for sophisticated failover and load-balancing mechanisms.

For instance, if you are using pgdb as your DB-API 2 database module and
want a pool of at least five connections to your local database 'mydb':

    import pgdb  # import used DB-API 2 module
    from CDBUtils.ValidatedPooledDB import PooledDB
    pool = PooledDB(pgdb, 5, database='mydb')

Once you have set up the connection pool you can request
database connections from that pool:

    db = pool.connection()

You can use these connections just as if they were ordinary
DB-API 2 connections.  Actually what you get is the hardened
SteadyDB version of the underlying DB-API 2 connection.

Please note that the connection may be shared with other threads
by default if you set a non-zero maxshared parameter and the DB-API 2
module allows this.  If you want to have a dedicated connection, use:

    db = pool.connection(shareable=False)

You can also use this to get a dedicated connection:

    db = pool.dedicated_connection()

If you don't need it any more, you should immediately return it to the
pool with db.close().  You can get another connection in the same way.

Warning: In a threaded environment, never do the following:

    pool.connection().cursor().execute(...)

This would release the connection too early for reuse which may be
fatal if the connections are not thread-safe.  Make sure that the
connection object stays alive as long as you are using it, like that:

    db = pool.connection()
    cur = db.cursor()
    cur.execute(...)
    res = cur.fetchone()
    cur.close()  # or del cur
    db.close()  # or del db

Note that you need to explicitly start transactions by calling the
begin() method.  This ensures that the connection will not be shared
with other threads, that the transparent reopening will be suspended
until the end of the transaction, and that the connection will be rolled
back before being given back to the connection pool.


Ideas for improvement:

* Add a thread for monitoring, restarting (or closing) bad or expired
  connections (similar to DBConnectionPool/ResourcePool by Warren Smith).
* Optionally log usage, bad connections and exceeding of limits.


Copyright, credits and license:

* Contributed as supplement for Webware for Python and PyGreSQL
  by Christoph Zwerschke in September 2005
* Based on the code of DBPool, contributed to Webware for Python
  by Dan Green in December 2000

Licensed under the MIT license.

"""
import sys
import threading
from threading import Condition, Timer
import time
from DBUtils import PooledDB as Pool_db

__version__ = '1.0'


class PooledDB(Pool_db.PooledDB):
    """Pool for DB-API 2 connections.

    After you have created the connection pool, you can use
    connection() to get pooled, steady DB-API 2 connections.

    """

    version = __version__
    def_validate_sql = 'SELECT 1 FROM DUAL'
    def __init__(
            self, creator, mincached=0, maxcached=0,
            maxshared=0, maxconnections=0, blocking=False,
            maxusage=None, setsession=None, reset=True,
            failures=None, ping=1, test_on_borrow=False, test_idle=True,
            validation_sql=None, idle_check_time=60, validate_timeout=1, max_wait_time=5,
            *args, **kwargs):
        """Set up the DB-API 2 connection pool.

        creator: either an arbitrary function returning new DB-API 2
            connection objects or a DB-API 2 compliant database module
        mincached: initial number of idle connections in the pool
            (0 means no connections are made at startup)
        maxcached: maximum number of idle connections in the pool
            (0 or None means unlimited pool size)
        maxshared: maximum number of shared connections
            (0 or None means all connections are dedicated)
            When this maximum number is reached, connections are
            shared if they have been requested as shareable.
        maxconnections: maximum number of connections generally allowed
            (0 or None means an arbitrary number of connections)
        blocking: determines behavior when exceeding the maximum
            (if this is set to true, block and wait until the number of
            connections decreases, otherwise an error will be reported)
        maxusage: maximum number of reuses of a single connection
            (0 or None means unlimited reuse)
            When this maximum usage number of the connection is reached,
            the connection is automatically reset (closed and reopened).
        setsession: optional list of SQL commands that may serve to prepare
            the session, e.g. ["set datestyle to ...", "set time zone ..."]
        reset: how connections should be reset when returned to the pool
            (False or None to rollback transcations started with begin(),
            True to always issue a rollback for safety's sake)
        failures: an optional exception class or a tuple of exception classes
            for which the connection failover mechanism shall be applied,
            if the default (OperationalError, InternalError) is not adequate
        ping: determines when the connection should be checked with ping()
            (0 = None = never, 1 = default = whenever fetched from the pool,
            2 = when a cursor is created, 4 = when a query is executed,
            7 = always, and all other bit combinations of these values)
        test_on_borrow: check availability of the connection fetched from the pool
            (True = check，False = default = never check)
        test_idle: Check connection availability on idle(是否检查空闲连接)
                (True = default = check，False =  never check)
        validation_sql: the sql for validate the connection 测试连接的sql
                    (default is 'SELECT 1 FROM DUAL')
        idle_check_time: the seconds for Check and remove the idle connection interval,
                    it will be start one Thread to check the idle connection in the pool,
                     whenever 'idleCheckTime' greater than 0 and 'testIdle' is True,default is 60 seconds.
                    (检查并移除连接池中空闲连接的时间间隔 小于等于0时不检查,默认60s)
        validate_timeout: the max seconds to execute the validation Sql,default is 1.
                    if 'validateTimeOut' Less than 1, it will  Wait until to return the result
                    (执行校验sql语句的最大超时时间秒默认1s)
        max_wait_time: the max wait time for fetch one connection from the pool,
                    if ‘maxWaitTime’ greater than 0 ,it will be start a lock for the function
                    "connection " with in the time, and throw one exception when the timeout
                    在连接池中获取一个有效连接的最大超时时间 默认5s
        args, kwargs: the parameters that shall be passed to the creator
            function or the connection constructor of the DB-API 2 module

        """
        try:
            threadsafety = creator.threadsafety
        except AttributeError:
            try:
                if not callable(creator.connect):
                    raise AttributeError
            except AttributeError:
                threadsafety = 2
            else:
                threadsafety = 0
        if not threadsafety:
            raise Pool_db.NotSupportedError("Database module is not thread-safe.")
        self._creator = creator
        self._args, self._kwargs = args, kwargs
        self._blocking = blocking
        self._maxusage = maxusage
        self._setsession = setsession
        self._reset = reset
        self._failures = failures
        self._ping = ping
        # 新增项处理开始
        self.testOnBorrow = test_on_borrow
        self.testIdle = test_idle
        self.validationSql = self.def_validate_sql if not validation_sql else validation_sql
        self.idleCheckTime = 0 if not idle_check_time else idle_check_time
        self.validateTimeOut = 1 if not validate_timeout else validate_timeout
        self.maxWaitTime = max_wait_time
        # 新增项处理结束
        if mincached is None:
            mincached = 0
        self._mincached = mincached
        if maxcached is None:
            maxcached = 0
        if maxconnections is None:
            maxconnections = 0
        if maxcached:
            if maxcached < mincached:
                maxcached = mincached
            self._maxcached = maxcached
        else:
            self._maxcached = 0
        if threadsafety > 1 and maxshared:
            self._maxshared = maxshared
            self._shared_cache = []  # the cache for shared connections
        else:
            self._maxshared = 0
        if maxconnections:
            if maxconnections < maxcached:
                maxconnections = maxcached
            if maxconnections < maxshared:
                maxconnections = maxshared
            self._maxconnections = maxconnections
        else:
            self._maxconnections = 0
        self._idle_cache = []  # the actual pool of idle connections
        self._lock = Condition()
        self._conn_lock = Condition()
        self._connections = 0
        # Establish an initial number of idle database connections:
        idle = [self.dedicated_connection() for i in range(mincached)]
        while idle:
            idle.pop().close()
        if self.testIdle and self.idleCheckTime > 0:
            t = Timer(self.idleCheckTime, self.start_check_idle, [self.idleCheckTime])
            t.start()

    def start_check_idle(self, time_out):
        """
        开启检查并删除空闲连接
        :param time_out:
        :return:
        """
        if time_out:
            self._lock.acquire()
            try:
                while len(self._idle_cache) > self._mincached:
                    self._idle_cache.pop(0).close()
                    # self._connections -=1
                self._lock.notify()
            finally:
                self._lock.release()
            t = Timer(time_out, self.start_check_idle, [time_out])
            t.start()

    def connection(self, shareable=True):
        # self._lock.acquire()
        try:
            if self.testOnBorrow and self.maxWaitTime:
                start = time.time()
                t = ResultThread(self.get_validated_conn, [self, shareable])
                t.join(self.maxWaitTime)
                if t.result:
                    conn = t.result
                else:
                    t.stop()
                    error = "%s获取新连接失败，获取超时%s,thread=%s,flag is%s,error:%s" % (
                        threading.currentThread().getName(), time.time()-start, t.getName(), t.isAlive(), t.error)
                    raise Pool_db.PooledDBError(error)
            else:
                conn = super().connection(shareable)
            # self._lock.notify()
        except Exception as e:
            raise Pool_db.InvalidConnection(e)
        # finally:
        #     self._lock.release()
        return conn

    def get_validated_conn(self, shareable=True):
        # start = time.time()
        conn = None
        try:
            while True:
                conn = super().connection(shareable)
                if self._validate_connection(conn):
                    break
            return conn
        except Exception as e:
            self.close_conn(conn)
            raise Pool_db.PooledDBError("get_validated_conn error", e)

    def close_conn(self, conn):
        if not conn:
            return False
        self._lock.acquire()
        try:
            conn.cancel()
            try:
                conn._con.close()
            except:
                pass
            conn.close()
            if self._connections:
                self._connections -= 1
            self._lock.notify()
        finally:
            self._lock.release()
        return True

    def _validate_connection(self, conn, sql=None):
        """
        校验连接是否可用 不可用时移除连接池
        :param conn:
        :param sql:
        :return:
        """
        sql = self.def_validate_sql if not sql else sql

        try:
            if self.validateTimeOut > 0:
                c = ResultThread(exec_sql, conn=conn, sql=sql, params=[])
                c.join(self.validateTimeOut)
                if c.result:
                    return True
                c.stop()
                self.close_conn(conn)
            else:
                res = exec_sql(conn=conn, sql=sql, params=[])
                return True
        except Exception as e:
            print("_validate_connection-error:", e)

        return False


def exec_sql(conn, sql, params=()):
    try:
        cus = conn.cursor()
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
        if cus:
            cus.close()


class ResultThread(threading.Thread):
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
            self._stop()
        except Exception:
            pass

    def run(self):
        try:
            self.result = self.fun(*self.args, **self.kwargs)
        except:
            self.error = sys.exc_info()
