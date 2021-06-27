from bs4 import BeautifulSoup
import requests

def main():
    url = "http://www.netbian.com/s/lol/"
    header = {"User-Agent":"haha"}
    res = requests.get(url=url,headers=header)
    res.encoding="GBK"
    print(res.status_code)
    soup = BeautifulSoup(res.text,"lxml")
    tr = soup.select(".list > ul   img")[5]["src"]
    print(tr)

if __name__ == "__main__":
    main()


