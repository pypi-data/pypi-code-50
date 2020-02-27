import os
from scrapy.exceptions import DropItem

class ItemCheckPipeline(object):

    def process_item(self, item, spider):
        unique_id = item.get('unique_id')
        if not unique_id:
            spider.logger.error(f'unique_id is None')
            raise DropItem('unique_id is None')
        
        queues = item.queue_names()
        if len(queues) == 0:
            spider.logger.warn(f'queue_names length is 0')
        return item
