from django.shortcuts import render

from .forms import IPCreatorForm
from .tcp import IPPacket


# Create your views here.

def index(request):
    if request.method == 'GET':
        ip_create_form = IPCreatorForm()
    else:
        ip_create_form = IPCreatorForm(request.POST)
        ip_packet = IPPacket()

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

    return render(request, 'ipApp/index.html', {'ipForm': ip_create_form})
