import socket
import sys


def mian(argv):
    up_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while 1:
        send_data=input("input your speak:")
        
        if send_data=="break":
            break
        
       # up_socket.sendto(b"hahhahah",("172.21.204.107",8080))
        up_socket.sendto(send_data.encode("utf-8"),(argv,8080))
    up_socket.close()

if __name__=="__main__":
    mian(sys.argv[1])
