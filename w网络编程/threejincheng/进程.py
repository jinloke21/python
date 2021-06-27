import threading
import time
import multiprocessing

def test1():
    count = 0
    while 1:
        count+=1
        if count ==3:
            break
        print("test1----------------")
        time.sleep(1)

def test2():

    while 1:
        print("test2----------------")
        time.sleep(1)





def main():
    t1 = multiprocessing.Process(target=test1)
    t2 = multiprocessing.Process(target=test2)
    t1.start()
    t2.start()

if __name__=="__main__":
    main()
