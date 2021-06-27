# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class FristbloodPipeline:
    fp =None
    def open_spider(self,spider):
        print("开始爬虫！")
        self.fp = open("./spi.txt","w",encoding="utf-8")

    def process_item(self, item, spider):
        title = item['title']
        date = item['date']
        self.fp.write(title+": "+date+"\n")
        return item #就会吧item传递给下一个要执行的对象
    def close_spider(self,spider):
        print("爬虫结束！")
        self.fp.close()




class Mysql_connt:
    con =None
    cour = None
    def open_spider(self,spider):
        self.con = pymysql.Connect(host="127.0.0.1",port = 3306,user = "root",password ="123.com",db = "IT",charset="utf8")
    def process_item(self, item, spider):
        self.cour = self.con.cursor()
        try:
            self.cour.execute("insert into one values('%s','%s')"%(item['title'],item['date']))
            self.con.commit()
        except Exception as e:
            print(e)
        return item #就会吧item传递给下一个要执行的对象
    def close_spider(self,spider):
        print("存取数据库结束！")
        self.cour.close()
        self.con.close()
