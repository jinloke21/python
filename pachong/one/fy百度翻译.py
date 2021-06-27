import requests
import json
def main():
    string = input("请输入要翻译的英文：")
    url = "https://fanyi.baidu.com/sug"
    header = {"User-Agent":"hahha"}
    param = {
            "kw":string
        }
    res = requests.post(url=url,headers=header,data=param)
    page_txt = string+".html"
    f = open("./爬虫结果/"+page_txt,"w",encoding="utf-8")
    json.dump(res.json(),fp=f,ensure_ascii=False)
    print("状态码："+str(res.status_code))
    print("保存成功！")

if __name__=="__main__":
    main()
