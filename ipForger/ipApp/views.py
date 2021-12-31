from django.http import HttpResponseRedirect
from django.shortcuts import render
from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.layers.inet import TCP, UDP
from scapy.layers.l2 import Ether

import socket
from getmac import get_mac_address as gma


# Create your views here.

def index(request):
    if request.method == 'GET':
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        local_mac = gma()
        return render(request, 'ipApp/index.html', {'clientIP': local_ip, 'clientMac': local_mac})


def sendT(request):
    if request.method == "POST":

        version = 4
        ihl = int(request.POST['ihlT'])
        tos = int(request.POST['tosT'])
        lenT = int(request.POST['lenT'])
        ident = int(request.POST['identT'])
        flags = request.POST['flagsT']

        if flags == '0':
            flags = 0

        fragment = int(request.POST['fragmentT'])
        ttl = int(request.POST['ttlT'])
        protocol = int(request.POST['protocolsT'])
        check = int(request.POST['headerCT'])
        srcIP = request.POST['srcIPT']
        destIP = request.POST['destIPT']
        opt = request.POST['optIPT']

        srcPort = int(request.POST['srcPort'])
        destPort = int(request.POST['destPort'])
        seqNum = int(request.POST['seqNum'])
        ackNum = int(request.POST['ackNum'])
        dOff = int(request.POST['dOff'])
        rBits = int(request.POST['rBits'])
        cFlags = request.POST['cFlags']
        winSize = int(request.POST['winSize'])
        checkST = int(request.POST['checkST'])
        uPont = int(request.POST['uPont'])
        dataT = request.POST['optionsTCP']

        dataTT = request.POST['dataTC']

        dataTS = dataT.split(",")
        dataTS.pop()
        dataO = []
        for i in dataTS:
            if i == "1":
                dataO.append(('NOP', ''))
            elif i == "2":
                dataO.append(('MSS', 4))
            elif i == "3":
                dataO.append(('SAckOK', ''))
            elif i == "4":
                dataO.append(('Timestamp', (1098453, 0)))

        ip = IP(version=version, ihl=ihl, tos=tos, len=lenT, id=ident, flags=flags, frag=fragment, ttl=ttl,
                proto=protocol,
                chksum=check, src=srcIP, dst=destIP, options=opt)

        tcp = TCP(sport=srcPort, dport=destPort, seq=seqNum, ack=ackNum, dataofs=dOff, reserved=rBits, flags=cFlags,
                  window=winSize, chksum=checkST, urgptr=uPont, options=dataO)

        send(ip / tcp / Raw(dataTT))

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def sendU(request):
    if request.method == "POST":

        dMac = request.POST['ethDesU']
        eMac = request.POST['ethSrcU']
        typeT = 0x800

        version = 4
        ihl = int(request.POST['ihlU'])
        tos = int(request.POST['tosU'])
        lenI = int(request.POST['lenUI'])
        ident = int(request.POST['identU'])
        flags = request.POST['flagsU']

        if flags == '0':
            flags = 0

        fragment = int(request.POST['fragmentU'])
        ttl = int(request.POST['ttlU'])
        protocol = int(request.POST['protocolsU'])
        check = int(request.POST['headerCU'])
        srcIP = request.POST['srcIPU']
        destIP = request.POST['destIPU']
        opt = request.POST['optIPU']

        srcPort = int(request.POST['srcPortU'])
        destPort = int(request.POST['destPortU'])
        lenU = int(request.POST['lenU'])
        checkSU = int(request.POST['checkSU'])

        dataUD = request.POST['dataU']

        eth = Ether(dst=dMac, src=eMac, type=typeT)

        ip = IP(version=version, ihl=ihl, tos=tos, len=lenI, id=ident, flags=flags, frag=fragment, ttl=ttl,
                proto=protocol,
                chksum=check, src=srcIP, dst=destIP, options=opt)

        udp = UDP(sport=srcPort, dport=destPort, len=lenU, chksum=checkSU)

        send(ip / udp / Raw(dataUD))

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def sendI(request):
    if request.method == "POST":

        version = 4
        ihl = int(request.POST['ihlI'])
        tos = int(request.POST['tosI'])
        lenI = int(request.POST['lenII'])
        ident = int(request.POST['identI'])
        flags = request.POST['flagsI']

        if flags == '0':
            flags = 0

        fragment = int(request.POST['fragmentI'])
        ttl = int(request.POST['ttlI'])
        protocol = int(request.POST['protocolsI'])
        check = int(request.POST['headerCI'])
        srcIP = request.POST['srcIPI']
        destIP = request.POST['destIPI']
        opt = request.POST['optIPI']

        typeI = int(request.POST['typeI'])
        codeI = int(request.POST['codeI'])
        checkI = int(request.POST['checkS'])

        dataIC = request.POST['dataAI']

        ip = IP(version=version, ihl=ihl, tos=tos, len=lenI, id=ident, flags=flags, frag=fragment, ttl=ttl,
                proto=protocol,
                chksum=check, src=srcIP, dst=destIP, options=opt)

        icmp = ICMP(type=typeI, code=codeI, chksum=checkI)

        send(ip / icmp / Raw(dataIC))

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def ICMP_sweep(request):
    if request.method == "POST":
        startIPScan = request.POST['startIPScan']
        endIPScan = request.POST['endIPScan']
        # thr = threading.Thread(target=icmpSweep, args=(startIPScan, endIPScan), daemon=True)
        # thr.start()
        scanData = icmpSweep(startIPScan, endIPScan)

        return render(request, 'ipApp/report.html', {'scanD': scanData[:-1], 'result': scanData[-1]})
    else:
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


# -----ICMPsweeper----
def iprange(ip1, ip2):
    ip1_1 = ip1.split(".")
    ip2_2 = ip2.split(".")
    iparr = []
    for i in range(0, len(ip1_1)):
        ip1_1[i] = int(ip1_1[i])

    for i in range(0, len(ip2_2)):
        ip2_2[i] = int(ip2_2[i])

    for i in range(ip1_1[0], ip2_2[0] + 1):
        for j in range(ip1_1[1], ip2_2[1] + 1):
            for k in range(ip1_1[2], ip2_2[2] + 1):
                for z in range(ip1_1[3], ip2_2[3] + 1):
                    temp = str(i) + '.' + str(j) + '.' + str(k) + '.' + str(z)
                    iparr.append(temp)
    return iparr


def icmpSweep(startIPScan, endIPScan):
    # iparray = iprange("192.168.1.178", "192.168.1.179")
    ip1_1 = startIPScan.split(".")
    ip2_2 = endIPScan.split(".")
    iparr = []
    for i in range(0, len(ip1_1)):
        ip1_1[i] = int(ip1_1[i])

    for i in range(0, len(ip2_2)):
        ip2_2[i] = int(ip2_2[i])

    for i in range(ip1_1[0], ip2_2[0] + 1):
        for j in range(ip1_1[1], ip2_2[1] + 1):
            for k in range(ip1_1[2], ip2_2[2] + 1):
                for z in range(ip1_1[3], ip2_2[3] + 1):
                    temp = str(i) + '.' + str(j) + '.' + str(k) + '.' + str(z)
                    iparr.append(temp)

    live_count = 0
    ress_Array = []

    # Send ICMP ping request, wait for answer
    for host in iparr:

        resp = sr1(IP(dst=str(host)) / ICMP(), timeout=0.4, verbose=0)
        # print(resp)
        if resp is None:
            print(f"{host} is down or not responding.")
            ress_Array.append(host + " is down or not responding.")
        elif (
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]
        ):
            print(f"{host} is blocking ICMP.")
            ress_Array.append(host + " is blocking ICMP.")
        else:
            print(f"{host} is responding.")
            ress_Array.append(host + " is responding.")
            live_count += 1

    print(f"{live_count}/{len(iparr)} hosts are online.")

    ress_Array.append(str(live_count) + "/" + str(len(iparr)) + "hosts are online.")

    return ress_Array

# -----ICMPsweeper----
