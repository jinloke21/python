import requests

url = "https://www.baidu.com/s"
#处理url携带的参数
key = input('请输入参数：')
param = {
	"wd":key
}
header = {
        "User-Agent":"2324"
    }
res = requests.get(url=url,params=param,headers=header)
print("状态码："+str(res.status_code))
page_text = res.text 

with open("./爬虫结果/"+key+".html","w",encoding="utf-8") as f:
	f.write(page_text)
	print(" 爬取成功！")
