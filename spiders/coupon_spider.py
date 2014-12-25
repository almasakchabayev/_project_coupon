import scrapy
from scrapy.selector import Selector
from scrapy.http import Request


class MySpider(scrapy.Spider):
    name = "coupon"
    allowed_domains = [
        'chocolife.me',
    ]
    start_urls = [
        'http://www.chocolife.me/',
    ]

    def parse(self, response):
        selector = Selector(response)
        category_urls = selector.xpath('//div[@id="b-deals__menunav__nav"]/ul[@class="b-deals__menunav__select"]/li/a/@href').extract()
        for url in category_urls:
            if 'chocolife' in url:
                yield Request(url, callback=self.parse_deal)
            else:
                yield Request('http://www.chocolife.me' + url, callback=self.parse_deal)

    def parse_deal(self, response):
        selector = Selector(response)
        print selector.xpath('//html').extract()



        
