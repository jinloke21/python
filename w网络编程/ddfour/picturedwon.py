import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open ("../1.jpg","wb") as f:
        f.write(img_content)



def main():
    gevent.joinall([
            gevent.spawn(downloader,"http://www.baidu.com")
            gevent.spawn(downloader,"http://www.itcast.com")
            gevent.spawn(downloader,"http://www.itheima.com")

        ])




if __name__=="__main__":
    main()
