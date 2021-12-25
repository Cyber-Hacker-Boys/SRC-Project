import ipaddress
from ipaddress import IPv4Network
from scapy.all import *
from scapy.layers.inet import IP, ICMP

def iprange(ip1,ip2):
    ip1_1 = ip1.split(".")
    ip2_2 = ip2.split(".")
    iparr=[]
    for i in range(0, len(ip1_1)):
        ip1_1[i] = int(ip1_1[i])

    for i in range(0, len(ip2_2)):
        ip2_2[i] = int(ip2_2[i])

    for i in range(ip1_1[0], ip2_2[0]+1):
        for j in range(ip1_1[1], ip2_2[1]+1):
            for k in range(ip1_1[2], ip2_2[2]+1):
                for z in range(ip1_1[3], ip2_2[3]+1):
                    temp=str(i)+'.'+str(j)+'.'+str(k)+'.'+str(z)
                    iparr.append(temp)
    return iparr

iparray = iprange("192.168.1.178", "192.168.1.179")
for x in iparray:
    print("->"+x)

live_count = 0

# Send ICMP ping request, wait for answer
for host in iparray:

    resp = sr1(IP(dst=str(host))/ICMP(),timeout=0.4,verbose=0)
    #print(resp)
    if resp is None:
        print(f"{host} is down or not responding.")
    elif (
        int(resp.getlayer(ICMP).type)==3 and
        int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
    ):
        print(f"{host} is blocking ICMP.")
    else:
        print(f"{host} is responding.")
        live_count += 1

print(f"{live_count}/{len(iparray)} hosts are online.")