import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from CRAWL.items import CrawlItem
from CRAWL.items import Detail_CrawlItem


class OneSpider(CrawlSpider):
    name = 'one'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']
    link = LinkExtractor(allow=r'id=\d+&page=\d+') 
    link2 = LinkExtractor(allow=r'index\?id=\d+') 
    rules = (
        Rule(link , callback='parse_item', follow=True),
        Rule(link2 , callback='parse_detail_url')
    )


    def parse_item(self, response):

        li_list = response.xpath('//div[@class="width-12"]/ul[@class="title-state-ul"]/li')
        #print(li_list)
        for li in li_list:
            tip = li.xpath('./span[@class="state1"]/text()')[0].extract()
            title = li.xpath('./span[@class="state3"]//text()')[0].extract()
            item = CrawlItem()
            item['tip'] = tip
            item['title'] = title
            yield item




    def parse_detail_url(self,response):
        detail_tip = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()')[0].extract()
        detail_text = response.xpath('//div[@class="width-12 mr-three"]/div[2]/div[@class="details-box"]/pre/text()')[0].extract()
        #print(detail_tip +" : " +detail_text)
        item = Detail_CrawlItem()
        item['detail_tip'] = detail_tip
        item['detail_text'] = detail_text
        yield item
    



