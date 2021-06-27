from multiprocessing import Pool
import time,os,random


def test(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))



def main(po):
    for i in range(0,10):
        po.apply_async(test,(i,))

if __name__=="__main__":
    po = Pool(3)
    main(po)
    print("------start-----")
    po.close()

    po.join()
    print("------end-------")
        
