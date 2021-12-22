from django.shortcuts import render
from django.http import HttpResponseRedirect

from .clientInfo import ClientInfo
from .forms import IPCreatorForm
from .tcp import Packet

from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import Ether


# Create your views here.

def index(request):
    if request.method == 'GET':
        ip_create_form = IPCreatorForm()
        clientData = ClientInfo()

    else:
        ip_create_form = IPCreatorForm(request.POST)
        ip_packet = Packet()

        ip_packet.src_ip = ip_create_form['srcIP'].value()
        ip_packet.src_port = int(ip_create_form['srcPort'].value())
        ip_packet.dst_ip = ip_create_form['destIP'].value()
        ip_packet.dst_port = int(ip_create_form['destPort'].value())
        ip_packet.seq_n = int(ip_create_form['seqN'].value())
        ip_packet.ack_n = int(ip_create_form['ackN'].value())
        ip_packet.ip_id = int(ip_create_form['ip_id'].value())
        ip_packet.ip_flags = int(ip_create_form['ip_flags'].value())
        ip_packet.content = ip_create_form['content'].value()

        ip_packet.sendTCP()

    return render(request, 'ipApp/index.html', {'ipForm': ip_create_form, 'client': clientData})


def sendT(request):
    if request.method == "POST":

        dMac = request.POST['ethDesT']
        eMac = request.POST['ethSrcT']
        typeT = 0x800

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
        dataT = request.POST['dataT']

        eth = Ether(dst=dMac, src=eMac, type=typeT)

        ip = IP(version=version, ihl=ihl, tos=tos, len=lenT, id=ident, flags=flags, frag=fragment, ttl=ttl,
                proto=protocol,
                chksum=check, src=srcIP, dst=destIP, options=opt)

        tcp = TCP(sport=srcPort, dport=destPort, seq=seqNum, ack=ackNum, dataofs=dOff, reserved=rBits, flags=cFlags,
                  window=winSize, chksum=checkST, urgptr=uPont, options=[('NOP', 0), ('EOL', 0)])

        sendp(eth / ip / tcp)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
