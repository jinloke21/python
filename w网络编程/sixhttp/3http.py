import socket
import re

def service_client(new_socket,request):
    #按hang分隔cheng yuanzu
    res = request.splitines()
    #GET / HTTP/1.1
    ret = re.match(r"[^/]+(/[^ ]*)",res[0])
    if ret.group(1) =="/":
        wj = "/index.html"
    else:
        wj = ret.group(1)
    try: 
        with open(wj,"rb") as f:
            content = f.read()
            f.close()
    except:
        response = "HTTP/1.1 404 NOT FOND\r\n"
        response +="\r\n"
        response +="----------file no find-------"
        new_socket.send(response.encode("utf-8"))

    else:
        response_header = "HTTP/1.1 200 ok\r\n"
        response_header += "Content-Length:%d\r\n" % len(content)
        response_header+= "\r\n"

        response = response_header.encode("utf-8") + content
        new_socket.send(response)


def main():
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #重复使用即使服务器先断开也不会等待2分钟
    tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


    tcp_server.bind(("",7890))
    tcp_server.listen(128)
    new_client_list = list()
    tcp_server.setblocking(False)
    while True:
        try: 
            new_socket,client_ip = tcp_server.accept()
        except Exception as ret:
            print(ret)
        else:
            new_client_list.append(new_socket)

        for i in new_client_list:
            try:
                i.setblocking(False)
                recv_datas = i.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_datas:
                    print("ok")
                    service_client(i,recv_datas)
                else:
                    i.close()
                    new_client_list.remove(i)


        tcp_server.close()



if __name__=="__main__":
    main()
