import time
import aiohttp
import asyncio

#async def re(url):
#    print("正在下载：",url)
#    await asyncio.sleep(2)
#    print("下载成功：",url)
#
#
#urls = [
#    "www.baidu.com",
#    "www.xinlang.com",
#    "www.lol.com"
#        ]
#

#task_List = []
#
#start = time.time()
#async def main():
#    for url in urls:
#        c = re(url)
#        i = asyncio.create_task(c)
#        task_List.append(i)
#    await asyncio.wait(task_List)
#
#asyncio.run(main())
#print("总耗时：",time.time()-start)

#================================================================== 

   

async def re(url):
    print("正在下载：",url)
    async with aiohttp.ClientSession() as se:
        async with await se.get(url) as f:
            page_txt = await f.text()
            print(page_txt)
    print("下载成功：",url)


urls = [
    "https://www.winxuan.com/front/ranklist/category/1?type=default",
    "https://item.winxuan.com/1202266480",
    "https://www.bilibili.com/video/BV1Yh411o7Sz?p=48&spm_id_from=pageDriver"
        ]


task_List = []

start = time.time()
async def main():
    for url in urls:
        c = re(url)
        i = asyncio.create_task(c)
        task_List.append(i)
    await asyncio.wait(task_List)

asyncio.run(main())
print("总耗时：",time.time()-start)

 

   

