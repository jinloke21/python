import socket
import threading


def send_msg(up_socket,dest_ip,dest_ports):

    while 1:
        dats = input("input the datas:")
        if dats == "break":
            break
        else:
            up_socket.sendto(dats.encode("utf-8"),(dest_ip,dest_ports))



def recv_msg(up_socket):

    while 1:
        recv_data = up_socket.recvfrom(1024)
        if str(recv_data)=="break":
            break
        else:
            print(recv_data.decode("utf-8"))






def main():
    up_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    up_socket.bind(("",8080))

    dest_ip = input("input the ip:")
    dest_ports  = int(input("input the port:"))
    
    data = input("please input datas:")

    t_recv = threading.Thread(target=recv_msg,args=(up_socket))
    t_send = threading.Thread(target=send_msg,args=(up_socket,dest_ip,dest_ports))
    t_recv.start()
    t_send.start()



if __name__=="__main__":
    main()


