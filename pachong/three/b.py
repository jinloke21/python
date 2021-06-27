from lxml import etree
import requests

def main():
    url = "http://www.netbian.com/s/lol/"
    header = {"User-Agent":"haha"}
    res = requests.get(url=url,headers=header)
    res.encoding="GBK"
    print(res.status_code)
    tree = etree.HTML(res.text)
    r = tree.xpath('//div[@class="list"]//img/@src')[0]
    print(r)

if __name__ == "__main__":
    main()


