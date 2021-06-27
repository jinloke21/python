import os


def returndir():
    wenjian = ["c:\\recycler\\","c:\\recycled\\","c:\\$recycle.bin\\"]
    for i in wenjian:
        if os.path.isdir(i):
            print("存在："+i)
    return None

returndir()
