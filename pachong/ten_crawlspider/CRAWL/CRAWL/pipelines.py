# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlPipeline:
    con =None
    cour = None
    title = None
    tip = None
    detail_tip = None
    detail_text = None

    def open_spider(self,spider):
        self.con = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123.com',db='tab',charset='utf8')
        print('开始存储')


    def process_item(self, item, spider):
        self.cour = self.con.cursor()
        if item.__class__.__name__=='CrawlItem':
            self.tip = item['tip']
            self.title = item['title']
        else:
            self.detail_tip = item['detail_tip']
            self.detail_text = item['detail_text']
            self.cour.execute("insert into news(detail_text) values('%s') where %s = news.tip"%(self.detail_text,self.tip))
            self.con.commit()
        #self.cour.execute("insert into news(tip,titile) values('%s','%s')"%(self.tip,self.title))
        #self.con.commit()

    def cloes_spider(self,spider):
        print("爬虫结束！")
        self.con.close()
        self.cour.close()


        return item
