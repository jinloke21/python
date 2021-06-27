import scrapy


class OneSpider(scrapy.Spider):
    name = 'one'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c100010000-p100310/?ka=search_100310']
    def start_requests(self):
        cookies = {
	"__a": "20409203.1624438501..1624438501.20.1.20.20",
	"__c": "1624438501",
	"__g": "-",
	"__l": "l=/www.zhipin.com/web/geek/recommend?random=1624441458345&r=https://www.baidu.com/link?url=xqxZrLDSJBnx5I38uYzdKKMNibLbGKv83MLAvM58GU0PvYeXpYcCBEUrMIb0HwHZ&wd=&eqid=be351f720000dd6d0000000360d30237&g=&s=3&friend_source=0&s=3&friend_source=0",
	"__zp_sname__": "5a4d3896",
	"__zp_sseed__": "LkndE6+/ka9qGQDbBktYIVoPcl1Kf4MEypEmbWgvsUg=",
	"__zp_stoken__": "93b4cOHwzOAM8UXg3N3hHVU0UKVVCLEB8Y3EaeRdjGh0Ie2ZBfC56EBNFEFQWH3MJfiAHWQkwIld0NQMUAT9/NXlSWxEvMSRbVihHbCtPcgUTM0lcXSEuBB0sAAdJBRE6TgMXZH0/VnwDeEc0",
	"__zp_sts__": "1624442509161",
	"_bl_uid": "s9k8zqyj924aFji2y4jt7edfd8m7",
	"lastCity": "100010000",
	"wt2": "DDJqTfsPS7tz8JYmF54seRHLW_5lfRis9m5SC7ddESXlNAAuChk4x_J2y2BsTqOVk7pszwhG6wuZZQ0x99AD_4Q~~"
}
        yield scrapy.Request(self.start_urls[0],callback=self.parse,cookies=cookies)

        

    def parse(self, response):
        li_list = response.xpath('//div[@class="job-list"]//li')
        #print(response.text)
       # li_list = response.xpath('/html/body/div[1]/div[3]/div/div[3]/ul/li[1]')
        print(li_list)
        #for li in li_list:
            #title = li.xpath('./div[@class="job-primary"]//div[@class="job-title"]//a/text()')
            #print(title)

