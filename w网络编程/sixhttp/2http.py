import socket
import re

def service_client(new_socket):
    request = new_socket.recv(1024).decode("utf-8")
    print(request)
    #按hang分隔cheng yuanzu
    res = request.splitines()
    ret = re.match(r"[^/]")

    response = "HTTP/1.1 200 ok\r\n"
    response += "\r\n"
    new_socket.send(response.encode("utf-8"))
    new_socket.close()


def main():
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    tcp_server.bind(("",7890))
    tcp_server.listen(128)
    while True:
        new_socket,client_ip = tcp_server.accept()
        service_client(new_socket)
    tcp_server.close()

if __name__=="__main__":
    main()
