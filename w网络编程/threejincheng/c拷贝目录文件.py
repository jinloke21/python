import multiprocessing
import os,time

def copy(old_filename,new_filename,file_name):
    print("从%s拷贝文件到%s,文件名%s"%(old_filename,new_filename,file_name))
    old_f = open(old_filename+"/"+file_name,"rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_filename+"/"+file_name,"wb")
    new_f.write(content)
    new_f.close()


def main():
    old_filename = input("请输入要copy的文件:")

    try:
        new_filename = old_filename+"[复件]"
        os.mkdir(new_filename)
    except:
        pass
    file_names = os.listdir(old_filename)
    pool = multiprocessing.Pool(5)
    for file_name in file_names:        
        pool.apply_async(copy,args=(old_filename,new_filename,file_name))
    print("--------start-------------")
    pool.close()
    pool.join()
    print("----------end-------------")


if __name__ =="__main__":
    main()
