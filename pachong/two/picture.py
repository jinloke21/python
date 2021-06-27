import requests
import time
from multiprocessing import Pool
import multiprocessing
import re
from bs4 import BeautifulSoup

def main(q,header,s):
    urls = "https://pic.netbian.com/"+q
    #print(urls)
    dm = requests.get(url=urls,headers=header).content
    with open("./pic2/"+str(s)+".jpg","wb") as f:
        f.write(dm)
        s +=1
    print("is over! s = "+str(s))
    f.close()


def main2(q,header):
    for a in range(2,30):
        #url = "https://pic.netbian.com/s/lol/index_"+str(a)+".html"
        url = "https://pic.netbian.com/4kdongman/index_"+str(a)+".html"
        page_txt = requests.get(url=url,headers=header)
        page_txt.encoding = "GBK"
        soup = BeautifulSoup(page_txt.text,"lxml")
        for a in range(0,40):
            try:
                src = soup.select(".slist > ul img")[a]["src"]
                #data.append(src)
                #q.put(src)
                q.append(src)
            except:
                pass
     #   print(q)
     #print(len(q))

if __name__=="__main__":
    po = Pool(10)
    header = {"User-Agent":"afjakfa"}
    #q = multiprocessing.Queue()
    q = []
    #t1 = multiprocessing.Process(target=main2,args=(q,header,))
    #t1.start()
    main2(q,header)
    #print("大小："+str(q.qsize()))
    s = 0
    for data in q:
        #print("data=="+data)
        po.apply_async(main,args=(data,header,s))
        s += 1

    
    print("--start--")
    po.close()
    po.join()
    print("--end--")

