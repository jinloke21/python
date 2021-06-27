from scapy.all import *


lis = ["172.21.204.107","172.21.22.2"]

request_data = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op=1,hwdst="00:00:00:00:00:00",pdst=lis,psrc="172.21.230.72"),iface="eth0",verbose = False)

datas = request_data[0].res[0][1].getlayer(ARP).fields["hwsrc"]
print(datas)
print(request_data[0].res[0][1][1].fields)
print(request_data[0].res[1][1].getlayer(ARP).fields)
