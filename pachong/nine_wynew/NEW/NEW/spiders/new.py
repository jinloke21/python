import scrapy
from NEW.items import NewItem
from selenium import webdriver

class NewSpider(scrapy.Spider):
    name = 'new'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    ul_sort = [3,4,6,7]
    modol_urls = []
    def __init__(self):
        self.web = webdriver.Chrome(executable_path="./chromedriver.exe")

    def parse(self, response):
        li_list = response.xpath('//div[@class="ns_area list"]/ul/li')
        for i in self.ul_sort:
            li = li_list[i].xpath('./a/@href')[0].extract()
            self.modol_urls.append(li)

        for url in self.modol_urls:
            yield scrapy.Request(url=url,callback=self.parse_model)

    def parse_model(self,response):
        div_list = response.xpath('//div[@class="data_row news_article clearfix "]')
        for div in div_list:
            title = div.xpath('./div[@calss="news_title"]/h3/a/text()')[0].extract()
            detail_url = div.xpath('./div[@calss="news_title"]/h3/a/@href')[0].extract()
            item = NewItem()
            item['title'] = title

            yield scrapy.Request(url=detail_url,callback=self.parse_datail_url,meta={"item":item})

    def parse_datail_url(self,response):
        div_text = response.xpath('//div[@class="post_body"]//text()').extract()
        div_text = "".join(div_text)
        item =response.meta['item']
        item['text'] = div_text
        yield item
        


