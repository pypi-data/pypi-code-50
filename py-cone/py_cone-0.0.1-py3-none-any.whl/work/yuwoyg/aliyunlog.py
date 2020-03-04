import time
from aliyun.log import LogClient, PutLogsRequest, LogItem, GetLogsRequest


class AliyunLog():
    def __init__(self, endpoint, access_key_id, access_key, project=None, logstore=None, topic=None, source=None):
        self.logstore = logstore
        self.project = project
        self.topic = topic
        self.source = source
        assert isinstance(self.topic, str), 'topic must be string'
        # assert len(self.topic.split(':')) == 2, 'topic must format like xxx:xxx'
        self.client = LogClient(endpoint, access_key_id, access_key)

    # def add_log(self, item:dict):  # contents为[(name1, value1), (name2, value2), ...]
    #     log_item = LogItem(int(time.time()), list(item.items()))
    #     log_req = PutLogsRequest(self.project, self.logstore, topic=self.topic, source=self.source, logitems=[log_item])
    #     self.client.put_logs(log_req)

    def add_log(self, item:str):  # item为json.dumps(obj)
        log_item = LogItem(int(time.time()), [('content', item)])
        log_req = PutLogsRequest(self.project, self.logstore, topic=self.topic, source=self.source, logitems=[log_item])
        self.client.put_logs(log_req)


    def get_topics(self, fromTime=None, toTime=None):
        try:
            req = GetLogsRequest(self.project, self.logstore, fromTime=fromTime, toTime=toTime, topic=self.topic, query='*|select "__topic__" group by "__topic__"')
            res = self.client.get_logs(req)
            return [log.get_contents()['__topic__'] for log in res.get_logs()]
        except Exception as e:
            print("Get topic error: %s"%str(e))
            return []

    def get_logs(self, fromTime, toTime):
        try:
            req = GetLogsRequest(self.project, self.logstore, fromTime=fromTime, toTime=toTime, query='*')
            res = self.client.get_logs(req)
            return [log.get_contents() for log in res.get_logs()]
        except Exception as e:
            print("Get logs error: %s"%str(e))
            return []
        try:
            listShardRes = self.client.list_shards(self.project, self.logstore)
            log_list = []
            for shard in listShardRes.get_shards_info():
                shard_id = shard["shardID"]
                res = self.client.get_cursor(self.project, self.logstore, shard_id, fromTime)
                start_cursor = res.get_cursor()
                res = self.client.get_cursor(self.project, self.logstore, shard_id, toTime)
                end_cursor = res.get_cursor()
                while True:
                    loggroup_count = 100  # 每次读取100个包
                    res = self.client.pull_logs(self.project, self.logstore, shard_id, start_cursor, loggroup_count, end_cursor)
                    log_list += res.get_loggroup_json_list()
                    next_cursor = res.get_next_cursor()
                    if next_cursor == start_cursor:
                        break
                    start_cursor = next_cursor
            return log_list
        except Exception as e:
            print("Get topic error: %s"%str(e))
            return []
            # print(log['logs'][0]['@lh_time'])
            # ret_logs['topic']