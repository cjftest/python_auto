import scrapy
from jsonpath import jsonpath

class JdProductSpider(scrapy.Spider):
    name = 'jd_product'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
