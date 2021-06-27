import scrapy


class OneSpider(scrapy.Spider):
    name = 'one'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kyouxi/']
    urls = "https://pic.netbian.com/4kyouxi/index_%d.html"
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('//div[@class="slist"]/ul/li')
        #print(li_list)
        for li in li_list:
        #    print("fjkaf")
            src = li.xpath('./a/img/@src')[0].extract()
            img_src = "https://pic.netbian.com" + str(src)
            print(img_src)
        if self.page_num <= 5:
            new_url = format(self.urls%self.page_num)
    #        print(new_url)
            self.page_num = self.page_num + 1
            yield scrapy.Request(url=new_url,callback=self.parse)

