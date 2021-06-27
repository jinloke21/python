import scrapy
import time

class IpSpider(scrapy.Spider):
    name = 'ip'
#    allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):
        time.sleep(0.5)
        page_source = response.text
        with open('./ip.html','w',encoding="utf-8") as f:
            f.write(page_source)

