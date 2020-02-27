from scrapy_nc.crawlab import get_task_id
from scrapy_nc.db import mongo_db

class MongoPipeline(object):

    def process_item(self, item, spider):
        if not self.spider_collection:
            pass
        ensure_unique_index = spider.settings.get('ENSURE_UNIQUE_INDEX')
        item_dict = dict(item)
        item_dict['task_id'] = get_task_id()
        if ensure_unique_index:
            self.spider_collection.update_one({
                'unique_id':   item.get('unique_id')
            }, {"$set": item_dict}, upsert=True)
        else:
            self.spider_collection.update_one({
                'unique_id':   item.get('unique_id'),
                'task_id':   item.get('task_id')
            }, {"$set": item_dict}, upsert=True)
        return item

    def open_spider(self, spider):
        # spider.logger.error('open_spider')
        if not mongo_db:
            self.spider_collection = None
            spider.logger.error('mongodb not configed')
            return

        # self.spider_collection = mongo_db.get_collection(spider.name)

        # ensure_unique_index = spider.settings.get('ENSURE_UNIQUE_INDEX')
        # unique_key = ('unique_id')
        # spider.logger.info("self.spider_collection.index_information()",
        #                    self.spider_collection.index_information())
    
        # spider.logger.info("self.spider_collection.list_indexes()",
        #                        self.spider_collection.list_indexes())
        # if not ensure_unique_index:
        #     unique_key = ('unique_id','task_id')
        # try:
        #     index_keys = [index_spec['key'] for index_spec in
        #                     self.spider_collection.list_indexes()]

        # except:
        #     index_keys = []
        # spider.logger.info(f'unique_key {unique_key}')
        # if unique_key not in index_keys:
        #     self.spider_collection.create_index(unique_key, unique=True)
