from scapy.all import *

from scapy.layers.inet import TCP, IP


class IPPacket:
    dst_ip = ""
    dst_port = 0

    src_ip = ""
    src_port = 0

    ip_flags = 0
    ip_id = 0

    seq_n = 0
    ack_n = 0

    content = ""

    def sendTCP(self):
        """"""
        print(sys.argv)

        # build packet
        ip = IP(src=self.src_ip, dst=self.dst_ip, id=self.ip_id, flags=self.ip_flags)
        tcp = ip / TCP(sport=self.src_port, dport=self.dst_port, flags='PA',
                       seq=self.seq_n, ack=self.ack_n) / self.content
        tcp.display()
        print("length of packet {}".format(len(tcp)))

        send(tcp)
