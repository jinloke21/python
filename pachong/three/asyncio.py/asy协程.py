import asyncio

async def req(url):
    print("真正求情url是：",url)
    print("请求成功！")

#async修饰的函数，调用后返回i一个携程对象
c = req("www.baidu.com")


#创建一个事件循环对象
#loop = asyncio.get_event_loop()

#将携程对象注册到loop 中，然后启动loop
#loop.run_until_complete(c)

#或者直接调用次函数，python>=3.7
#asyncio.run(c)

#==================================================
#task的使用
#loop = asyncio.get_event_loop()
##基于loop创建了一个task对象
#task = loop.create_task(c)
#print(task)
#
#loop.run_until_complete(task)
#print(task)
#===================================================




#=========================await
#async def main():
#    print("我来了！")
#    res = await asyncio.sleep(2)
#    print("结束：",res)
#
#
#asyncio.run(main())
#===================================


#========================await2

#async def main():
#    print("======start====")
#    await asyncio.sleep(2)
#    print("===end===")
#    return "sucessfully"
#    
#
#async def main2():
#    print("one")
#    response  = await main() #阻塞等待main()函数执行完
#    print("return:",response)
#
#asyncio.run(main2())

#============================


#=========================task1
#在事件循环中添加多个任务


#async def main():
#    print(1)
#    print("哼！，我可不等你")
#    await asyncio.sleep(2)
#    print(2)
#    return "返回值"
#
#
#async def main2():
#    print("----start----")
#    #创建task任务，将当前的main函数加入到事件循环
#    test1 = asyncio.create_task(main())
#    test2 = asyncio.create_task(main())
#    print("我要执行了")
#    #当执行到IO时，会自动切换到其他任务，这里的await是等待相应的程序获取结果
#    res = await test1
#    res2 = await test2
#    print(res,res2)
#
#asyncio.run(main2())

#=============================endtask1



#==============================task2

#async def main():
#    print(1)
#    print("哼！，我可不等你")
#    await asyncio.sleep(2)
#    print(2)
#    return "返回值"
#
#
#async def main2():
#    print("----start----")
#    #创建task任务列表，将当前的main函数加入到事件循环
#    test_list = [
#            asyncio.create_task(main(),name="n1"),
#            asyncio.create_task(main(),name="n2")
#            ]
#    print("我要执行了")
#    #当执行到IO时，会自动切换到其他任务，这里的await是等待相应的程序获取结果
#    done,pending = await asyncio.wait(test_list,timeout=3) #由于await后不能加列表形式，所以用asyncio.wait函数读取列表中的任务
#    print(done,pending)
#
#asyncio.run(main2())
#                                                 
##================================endtask2


#=================================future

#async def main():
#    #获取当前的事件循环
#    loop = asyncio.get_running_loop()
#
#    #创建一个futher对象，这个对象什么也不干
#    fu = loop.create_future()
#
#    #等待最终结果(Futher),没有结果就一直等下去
#    await fu
#
#asyncio.run(main())

#===============================future1




#=============================future2

#async def main2(fu):
#    print(1)
#    await asyncio.sleep(2)
#    #等待2秒，设置fu的结果值为7777
#    fu.set_result("7777")
#
#
#async def main():
#    #获取当前的事件循环
#    loop = asyncio.get_running_loop()
#
#    #创建一个futher对象，这个对象什么也不干
#    fu = loop.create_future()
#    #等待拿到一个携程对象
#    await loop.create_task(main2(fu))
#
#    #这里由于等待，去执行main(fu),执行完fu=7777,不再等待
#    data = await fu
#    print(data)
#
#
#asyncio.run(main())


#===============================endfuture2



#================================concurrent.futures
import time
from concurrent.futures import Future
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor


def main(i):
    print("start---")
    time.sleep(i)
    return 123


def main2():
    pool = ProcessPoolExecutor(max_workers=5)
    for i in range(1,10):
        fur = pool.submit(main,i)
        print(fur)

start = time.time()
main2()
end = time.time()
print("总耗时：",end-start)



  





















