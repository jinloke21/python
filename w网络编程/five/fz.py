import re

def main():
    email= input("input your email:")
    #ijnwekgak@126/163.com 
    #ret = re.match(r"[a-zA-Z]{4,20}@(126|163).com$",email)
    ret = re.match(r"\w+@(126|163).com$",email)
    if ret:
        print("%s is right"%(ret.group()))
    else:
        print("is bad")
        

if __name__=="__main__":
    main()
