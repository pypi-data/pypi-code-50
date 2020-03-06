from .amqp_pipeline import AMQPPipeline
from .oss_pipeline import OSSPipeline
from .mongo_pipeline import MongoPipeline
from .item_check_pipeline import ItemCheckPipeline
from .filter_pipeline import FilterCheckPipeline, FilterSavePipeline
# from .redis_duplicate_pipeline import RedisDuplicatesPipeline

item_check_pipeline = 'scrapy_nc.pipelines.ItemCheckPipeline'
filter_check_pipeline = 'scrapy_nc.pipelines.FilterCheckPipeline'
amqp_pipeline = 'scrapy_nc.pipelines.AMQPPipeline'
mongo_pipeline = 'scrapy_nc.pipelines.MongoPipeline'
filter_save_pipeline = 'scrapy_nc.pipelines.FilterSavePipeline'

DEFAULT_ITEM_PIPELINES = {
    item_check_pipeline: 500,
    filter_check_pipeline: 550,
    amqp_pipeline: 600,
    mongo_pipeline: 650,
    filter_save_pipeline: 700,
}
