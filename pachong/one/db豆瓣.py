import requests
import json

def main():
    sta = input("请输入你想从第几部开始请求：")
    lim = input("请输入一次要请求的个数：")
    url = "	https://movie.douban.com/j/chart/top_list?"
    param = {
            "type":"24",
            "interval_id":"100:90",
            "action":"",
            "start":sta, #表示从庫中的第几部电影去取
            "limit":lim  #表示一次取出多少部
        }
    header = {
            "User-Agent":"12313"
        }
    res = requests.get(url=url,params=param,headers=header)
    list_data = res.json()
    f = open("./爬虫结果/豆瓣.html","w",encoding="utf-8")
    json.dump(list_data,fp=f,ensure_ascii=False)
    if res.status_code >= 200:
        print("Succesful!")
    else:
        print("bad!")





if __name__=="__main__":
    main()
