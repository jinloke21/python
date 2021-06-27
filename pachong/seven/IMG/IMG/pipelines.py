# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


from scrapy.pipelines.images import ImagesPipeline
import scrapy
import time
import re

class Img_piple(ImagesPipeline):
    date = time.time()

    def get_media_requests(self,item,info):


        yield scrapy.Request(item['img_src'])

    def file_path(self,request,response=None,info=None):
        #imgName = str(self.date) + '.jpg'
        imgNa = request.url.split('/')[-1]
        #print(imgNa)

        ret = re.search('(\w*)_s.jpg',imgNa)
        #print(ret.group(1))
        imgName = ret.group(1) + ".jpg"

        return imgName
    def item_completed(self,results,item,info):
        return item

