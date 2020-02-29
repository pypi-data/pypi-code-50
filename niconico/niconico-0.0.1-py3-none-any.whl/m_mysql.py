#coding=utf-8


import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine


rootPath=r'./'


class MySql():
    def __init__(self):
        #15162q1k54.imwork.net:58744#mt29353962.wicp.vip:43541#127.0.0.1:3306
        self.sqlUrl = 'mysql+pymysql://peppa:111111@127.0.0.1:3306/bilibili'
        self.engine = create_engine(self.sqlUrl, encoding='utf-8', echo=True)


    def getdbmysql(self, table):
        try:
            conn = self.engine.connect()
            sql_cmd ='select * from {}'.format(table)
            df = pd.read_sql(sql=sql_cmd, con=conn)
            return df
        except Exception  as e:
            print(e)
        finally:
            conn.close()

    def save2mysqldb(self, table, df):
        try:
            conn = self.engine.connect()
            # 将新建的DataFrame储存为MySQL中的数据表，不储存index列 , con=con, if_exists='append',
            df.to_sql(table, con=conn, if_exists='append', index=False)
            print('Read from and write to Mysql table successfully!')
        except Exception  as e:
            print(e)
        finally:
            conn.close()

    #从服务器查询个股url
    def getMidfromDB(self, table, left, right, type='mid'):
        sqlStr = "SELECT * FROM {} WHERE {} BETWEEN \"{}\" AND \"{}\"".format(table, type, left, right)
        with self.engine.raw_connection().cursor() as raw_cursor:
            query_count = raw_cursor.execute(sqlStr)
            query=raw_cursor.fetchall()
            result=[]
            for row in query:
                result.append(row[0])
            return result



# 主程序入口
if __name__ == '__main__':
    print('TS:'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


