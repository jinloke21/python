import socket
import multiprocessing
import re

def service_client(new_socket):
    request = new_socket.recv(1024)
    print(request.decode("utf-8"))

    response = "HTTP/1.1 200 ok\r\n"
    response += "\r\n"
    response += "hahahha"
    new_socket.send(response.encode("utf-8"))
    new_socket.close()


def main():
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    tcp_server.bind(("",7890))
    tcp_server.listen(128)
    while True:
        new_socket,client_ip = tcp_server.accept()
        t1 = multiprocessing.Process(target=service_client,args=(new_socket,))
        t1.start()
        #因为是进程，所有都会被拷贝一份，如果父进程不关闭的话，进相当于多开了一个子套接字
        new_socket.close()
    tcp_server.close()

if __name__=="__main__":
    main()
