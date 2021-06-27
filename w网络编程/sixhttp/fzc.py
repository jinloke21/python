import socket
import time

def main():
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.bind(("",7891))
    tcp_server.listen(128)
    clinet_list = list()
    while True:
        time.sleep(0.5)
        try:
            tcp_server.setblocking(False)
            clinet_socket,clinet_ip = tcp_server.accept()
        except Exception as ret:
            print("没有新的客户端连接")
        else:
            print("有一个客户端连接是%s" %(str(clinet_ip)))
            clinet_socket.setblocking(False)
            clinet_list.append(clinet_socket)

        for i in clinet_list:
            try:
                recv_datas = i.recv(1024)
            except Exception as ret:
                print("recv is not")
            else:
                if recv_datas:
                    print("recv is ok!")
                else:
                    i.close()
                    clinet_list.remove(i)
                    print("客户端关闭")


if __name__=="__main__":
    main()
