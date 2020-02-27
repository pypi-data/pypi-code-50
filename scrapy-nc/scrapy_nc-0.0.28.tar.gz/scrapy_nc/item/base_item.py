import scrapy
import json

class BaseItem(scrapy.Item):
    crawled_at = scrapy.Field()
    oss_filename = scrapy.Field()
    unique_id = scrapy.Field()

    def to_dict(self):
        dt = self.__dict__['_values']
        return dt

    def to_json_str(self):
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def queue_names(self):
        return []
