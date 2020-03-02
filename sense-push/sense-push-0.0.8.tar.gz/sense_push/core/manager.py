from sense_push.util import *
from sense_push.common import *
import sense_core as sd
import pymysql
from sense_push.core.data import PushDataHandler


class SensePushManager(object):

    def push_table_all_data(self, queue_configs, db_config, table, build_sql, limit=1000):
        if limit < 10:
            limit = 10
        offset = 0
        handler = PushDataHandler(database=db_config['database'], table=table, queue_configs=queue_configs)
        while True:
            sql = build_sql(offset, limit)
            items = self.fetch_by_sql(db_config, sql)
            sd.log_info("size={0} for sql={1}".format(len(items), sql))
            for item in items:
                handler.insert_data(item)
            if len(items) < limit:
                break
            offset += limit
        sd.log_info("done push_table_all_data for {0}".format(table))

    def fetch_by_sql(self, config, sql):
        conn = pymysql.connect(host=config['host'], user=config['user'],
                               password=config['password'],
                               charset='utf8', database=config['database'],
                               port=int(config['port']))
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        items = cursor.fetchall()
        cursor.close()
        conn.close()
        return items
