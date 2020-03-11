from ddcmaker.maker.spider.actions import normal
from ddcmaker.maker.spider.spider import Spider


def init():
    normal_spider = Spider()
    normal_spider.run_action(normal.init_body)
