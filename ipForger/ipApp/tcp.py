from scapy.all import *

from scapy.layers.inet import TCP, IP, Ether


class Packet:

    # Ethernet
    src_mac = ""
    dst_mac = ""
    type = 0

    # IP
    version_ip = ""
    ihl_ip = ""
    tos_ip = ""
    len_ip = ""
    ip_id = 0
    ip_flags = 0
    ip_frag = ""
    ip_ttl = ""
    ip_proto = ""
    ip_chksum = ""
    dst_ip = ""
    src_ip = ""
    ip_option = ""

    #TCP
    dst_port = 0
    src_port = 0
    seq_n = 0
    ack_n = 0
    dataO_tcp = ""
    reserved_tcp = ""
    flags_tcp = ""
    window_tcp = ""
    chksum_tcp = ""
    urgptr_tcp = ""
    options_tcp = ""

    content = ""

    def sendTCP(self):
        """"""
        print(sys.argv)

        # build packet
        eth = Ether(src=self.src_mac, dst=self.dst_mac, type=self.type)

        ip = IP(version=self.version_ip, ihl=self.ihl_ip, tos=self.tos_ip, len=self.len_ip, id=self.ip_id,
                flags=self.ip_flags, frag=self.ip_frag, ttl=self.ip_ttl, proto=self.ip_proto,
                chksum=self.ip_chksum, src=self.src_ip, dst=self.dst_ip, options=self.ip_option)
        
        tcp = ip / TCP(sport=self.src_port, dport=self.dst_port, flags='PA',
                       seq=self.seq_n, ack=self.ack_n) / self.content
        tcp.display()
        print("length of packet {}".format(len(tcp)))

        send(tcp)
