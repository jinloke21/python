import socket


def main():
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_socket.bind(("",8080))

    tcp_socket.listen(128)
    while True:
        print("wait a newclinet come to...")
        new_client,ipaddr = tcp_socket.accept()
        print("a new clinet come here!....")

        print(str(ipaddr))
        while 1:

            recv_data = new_client.recv(1024)
            if recv_data.decode("utf-8")=="break":
                break;
            else:
                print("data from clinet:%s"%recv_data.decode("utf-8"))

                new_client.send("-------ok---------".encode("utf-8"))

        new_client.close()
        print("had to close")
        tcp_socket.close()


if __name__ =="__main__":
    main()


