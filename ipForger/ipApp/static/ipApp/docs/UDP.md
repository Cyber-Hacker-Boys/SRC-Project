#Packet Explanation

##UDP Packet
User datagram protocol (UDP) operates on top of the Internet Protocol (IP) to transmit datagrams over a network. UDP does not require the source and destination to establish a three-way handshake before transmission takes place. Additionally, there is no need for an end-to-end connection.

Since UDP avoids the overhead associated with connections, error checks and the retransmission of missing data, it’s suitable for real-time or high performance applications that don’t require data verification or correction. If verification is needed, it can be performed at the application layer.

###Source Port
The port of the device sending the data. This field can be set to zero if the destination computer doesn’t need to reply to the sender.

###Destination Port
The destination UDP port number is the communication endpoint for the receiving device.

###Length
Specifies the number of bytes comprising the UDP header and the UDP payload data. The limit for the UDP length field is determined by the underlying IP protocol used to transmit the data.

###Checksum
The checksum allows the receiving device to verify the integrity of the packet header and payload. It is optional in IPv4 but was made mandatory in IPv6.
