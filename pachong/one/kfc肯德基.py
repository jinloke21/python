import requests
import json

def main():
    location = input("请输入你要确定的地址：")
    url = "	http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    param = {
	"cname": "",
	"pid": "",
	"keyword": location,
	"pageIndex": "1",
	"pageSize": "10"
            }
    header = {
            "User-Agent":"12313"
        }
    res = requests.get(url=url,params=param,headers=header)
    list_data = res.json()
    f = open("./爬虫结果/"+location+"肯德基.html","w",encoding="utf-8")
    json.dump(list_data,fp=f,ensure_ascii=False)
    if res.status_code >= 200:
        print("Succesful!")
    else:
        print("bad!")





if __name__=="__main__":
    main()
