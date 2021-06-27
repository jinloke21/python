from scapy.all import *
import re

def dns_query(dns_name):
    dns_result = sr1(IP(dst="114.114.114.114")/UDP()/DNS(rd=1,qd=DNSQR(qname=dns_name)),verbose=False)
    print(dns_result.getlayer(DNS).fields['an'][1].fields['rdata'])

if __name__=="__main__":
    dns_query(sys.argv[1])
