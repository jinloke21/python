import scrapy
from fristblood.items import FristbloodItem


class FristSpider(scrapy.Spider):
    name = 'frist'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.runoob.com/coder-learn-path']

#    def parse(self, response):
#        date = []
#        div_List = response.xpath('//div[@class="article"]')
#        #print(div_List)
#        #title = div_List.xpath('./div[2]/h2[3]/text()')
#        #title = div_List.xpath('./div[2]/h2[3]/text()')[0].extract()
#        for i in range(1,6):
#            title = div_List.xpath('./div[2]/h2['+str(i)+']/text()').extract_first()
#            #调用extract方法后可以将selector对象中存储的字符串提取出来
#            nei = div_List.xpath('./div[2]/ol['+str(i)+']//text()').extract()
#            nei = "".join(nei) #将列表转换成字符串
#            dic = {
#                "title":title,
#                "data":nei
#                    }
#            print(title,nei)
#            date.append(dic)
#        return date



    def parse(self, response):
        date = []
        div_List = response.xpath('//div[@class="article"]')
        #print(div_List)
        #title = div_List.xpath('./div[2]/h2[3]/text()')
        #title = div_List.xpath('./div[2]/h2[3]/text()')[0].extract()
        for i in range(1,6):
            title = div_List.xpath('./div[2]/h2['+str(i)+']/text()').extract_first()
            #调用extract方法后可以将selector对象中存储的字符串提取出来
            nei = div_List.xpath('./div[2]/ol['+str(i)+']//text()').extract()
            nei = "".join(nei) #将列表转换成字符串
            item = FristbloodItem()
            item['title'] = title
            item['date'] = nei
            yield item
