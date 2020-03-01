# -*- coding: utf-8 -*-
# Author: Orlando Chen
# Create: Sep 15, 2018
# Modifi: Mar 01, 2020

from siki.pysql import PySQLConnection as pys
from siki.basics import Logger as logger
from siki.basics.Logger import Priority as p
from siki.basics import Exceptions as excepts
from siki.dstruct.Queue import Queue

import threading
import time

class PySQLPool(threading.Thread):

    def __init__(self, size: int, params: dict):
        """
        setting up a process pool for sql handling
        
        Args:
        * [size] the number of sql connections to keep
        * [params] user, password, host, port, db, bstd, blog, dir, fname
        """
        self.pool = Queue()
        self.lock = threading.Lock()
        self.params = params

        # init self threading
        threading.Thread.__init__(self)

        # init with configure file
        if 'bstd' in params.keys() and 'blog' in params.keys() \
            and 'dir' in params.keys() and 'fname' in params.keys():
            logger.init(bool(params['bstd']), bool(params['blog']), params['dir'], params['fname'])
        else:
            logger.init(True, False)

        try:
            for i in range(size):
                # create a connection to sql server
                conn = pys.connect(user=params['user'], 
                    password=params['password'],
                    host=params['host'], 
                    port=params['port'])

                # add connection to queue
                self.pool.enqueue(conn)
            
            # print debug message
            logger.message(p.INFO, msg="creating connections pool finished")
        
        except excepts.SQLConnectionException as e:
            logger.message(p.ERROR, msg="creating connection failed", exception=e)





        def run(self):
            """
            running in backside
            """
            while True:
                # delay for 60 seconds
                time.sleep(60) 

                self.refresh()




    def get_connection(self):
        """
        Draw a connection from pool
        Returns:
        * [conn] pymysql.connect, the connection object from pool
        """
        conn = None
        try:
            self.lock.acquire()

            # returns a conn instance
            if len(self.pool) > 0:
                conn = self.pool.dequeue()

            # connection is empty
            if conn is None:
                logger.message(p.INFO, msg="connection is none, create a new one")
                conn = pys.connect(
                    user=self.params['user'],
                    password=self.params['password'],
                    host=self.params['host'],
                    port=self.params['port'])
            
            # if not connected
            if not pys.check_connection(conn):
                conn.connect()

        except Exception as e:
            logger.message(p.ERROR, msg="get connection failed, create a new one", exception=e)
        
        finally:
            self.lock.release()
            return conn




    def put_connection(self, conn):
        """
        Put a connection back to pool
        Args:
        * [conn] pymysql.connect
        """
        try:
            self.lock.acquire()

            # valid connection, put it back to pool
            if conn and pys.check_connection(conn):
                self.pool.enqueue(conn)
            
            # none connection, create a new one then re-enqueue
            else:
                conn = pys.connect(
                    user=self.params['user'],
                    password=self.params['password'],
                    host=self.params['host'],
                    port=self.params['port']) 
                logger.message(p.INFO, msg="create a new connection to pool")

                # enqueue
                self.put_connection(conn)

        finally:
            self.lock.release()




    def refresh(self):
        """
        Refresh the connection pool, this function will fix broken connections.
        """
        try:
            self.lock.acquire()

            backs = []
            for conn in self.pool:

                # an empty connection detected, reconnect to server
                if conn is None:
                    conn = pys.connect(
                        user=self.params['user'],
                        password=self.params['password'],
                        host=self.params['host'],
                        port=self.params['port']) 

                # reconnect if lost connection to server
                if not pys.check_connection(conn):
                    backs.append(conn)
                
            # after the loop, add new queue to original queue
            self.pool.merge(backs)

        finally:
            self.lock.release()
    



    def is_empty(self):
        """
        Whether the pool is empty
        Returns:
        * [res] bool
        """
        try:
            self.lock.acquire()

            return self.pool.is_empty()

        finally:
            self.lock.release()




    def close(self):
        """
        Close the connection pool, this function will release all resources
        """
        try:
            self.lock.acquire()

            logger.message(p.INFO, msg = "closing pool...")
            
            while not self.is_empty():
                pys.disconnect(self.pool.dequeue())
            
            logger.message(p.INFO, msg = "PySQLPool colsed")
        
        finally:
            self.lock.release()


    

    def size(self):
        """
        Returning the size of pool
        Returns:
        * [size] int, the size of contained connections
        """
        try:
            self.lock.acquire()
            return self.pool.size()
        finally:
            self.lock.release()
        