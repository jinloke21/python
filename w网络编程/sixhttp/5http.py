import socket
import threading
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
        t1 = threading.Thread(target=service_client,args=(new_socket,))
        t1.start()
    tcp_server.close()

if __name__=="__main__":
    main()
