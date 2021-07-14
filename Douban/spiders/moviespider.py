import scrapy
from scrapy import Request
from Douban.items import DoubanItem

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    # allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        all_msg=response.xpath("//div[@class='item']")
        movie=DoubanItem()
        for i in all_msg:
            movie['rank']=i.xpath("div[@class='pic']/em/text()").extract()[0]
            movie['title']=i.xpath("div[@class='info']/div[@class='hd']/a/span[1]/text()").extract()[0]
            movie['score']=i.xpath("div[@class='info']/div[@class='bd']/div/span[2]/text()").extract()[0]
            movie['comment_num']=i.xpath("div[@class='info']/div[@class='bd']/div/span[4]/text()").extract()[0]
            movie['quote']=i.xpath("div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()").extract()
            if len(movie['quote'])==0:
                movie['quote']='暂无评论'
            else:
                movie['quote']=movie['quote'][0]
            movie['img_path']=i.xpath("div[@class='pic']/a/img/@src").extract()[0]
            yield movie
        pass
        next_url = response.xpath('.//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250'+ next_url[0]
            yield Request(next_url)