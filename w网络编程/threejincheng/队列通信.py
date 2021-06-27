import multiprocessing
import time


def test1(q):
    data = [1,2,3,4,5,6]
    for i in data:
        q.put(i)
       # print(i)
    print("数据已经存到队列中....")

def test2(q):
    waiting_data = list()
    while True:
            if q.empty():
                break
            else:
                p = q.get()
                waiting_data.append(p)
    print(waiting_data)
    print("完成......")


def main():
    q = multiprocessing.Queue()
    t1 = multiprocessing.Process(target=test1,args=(q,))
    t2 = multiprocessing.Process(target=test2,args=(q,))
    t1.start()
    time.sleep(1)
    t2.start()


if __name__=="__main__":
    main()
