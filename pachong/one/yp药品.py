import requests
import json
def main():
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    header = {"User-Agent":"hahha"}
    param = {
            "on": "true",
            "page": "1",
            "pageSize": "15",
            "productName": "",
            "conditionType": "1",
            "applyname": "",
            "applysn": ""
        }
    res = requests.post(url=url,headers=header,data=param)
    print("状态码："+str(res.status_code))
    air = res.json()
    id_list = []
    #print(air['list'])
    for A in air['list']:
        id_list.append(A['ID'])
    #print(id_list)
    url2 = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    f = open("./爬虫结果/yp.html","w",encoding="utf-8")
    for B in id_list:
        datas = {
           "id":B
            }
        res2 = requests.post(url=url2,data=datas,headers=header)
        bir = res2.json()
        json.dump(bir,fp=f,ensure_ascii=False)
    print("成功！")







if __name__=="__main__":
    main()
