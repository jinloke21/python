import scrapy
from IMG.items import ImgItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']


    def parse(self, response):
        #div_list = response.xpath('//div[class="index_only"]/div[class="left"]//div[id="container"]/div')
        div_list = response.xpath('//*[@id="container"]/div')
        img_list = []
        #print(div_list)
        for div in div_list:
          src2 = div.xpath('./div//a/img/@src2')[0].extract()
          img_src = "https:" + str(src2)
          item = ImgItem()
          item['img_src'] = img_src
          yield item
          

