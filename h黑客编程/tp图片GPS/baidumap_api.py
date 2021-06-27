#coding:utf8
import requests
import json

my_aky = "9Bu9sqOv9CNFbFaKFeuBzfRHrDaMUDnU"
url = "http://api.map.baidu.com/reverse_geocoding/v3/?ak="+my_aky+"&output=json&coordtype=wgs84ll&location=112.42543888888889,34.60506111111111"

header = "hahah"
res = requests.get(url=url)
gps_address = json.loads(res.text)
#print(res.text)
formatted_address = gps_address["result"]["formatted_address"]
#国家（若需访问境外POI，需申请逆地理编码境外POI服务权限）
country = gps_address["result"]["addressComponent"]["country"]
#省
province = gps_address["result"]["addressComponent"]["province"]
#城市
city = gps_address["result"]["addressComponent"]["city"]
#区
district = gps_address["result"]["addressComponent"]["district"]
#语义化地址描述
sematic_description = gps_address["result"]["sematic_description"]
#将转换后的信息写入文件
with open("gps_address.csv","a+") as csv:
        csv.write(formatted_address + "|" + country + "|" + province + "|" + city + "|" + district + "|" + sematic_description + "\n")
