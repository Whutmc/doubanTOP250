# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank=scrapy.Field()#排名
    title=scrapy.Field()#电影名称
    score=scrapy.Field()#评分
    comment_num=scrapy.Field()#评分人数
    quote=scrapy.Field()#最新评论
    img_path=scrapy.Field()#海报路径
    pass
