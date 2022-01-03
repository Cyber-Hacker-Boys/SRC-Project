#Header Explanation

##Ethernet Header
The ethernet header is the last header added to the data in the physical TCP/IP layer.

###Destination Address
This field is 6 bytes long. It contains the MAC address of the destination device. MAC address is 6 bytes or 48 bits (1 byte = 8 bits, 6x8 = 48bits) long.

For convenience, usually, it is written as 12-digit hexadecimal numbers (such as 0000.0A12.1234).

This value is set to the broadcast mac address.

###Source Address
This field is also 6 bytes long. It contains the MAC address of the source device. It helps the receiving device in identifying the source device.

This value is set to the users mac address.


###Type
This field is 2 bytes long. This field stores information about the protocol of the upper layer (network layer).

The Data Link layer of the source computer prepares, packs and loads the Ethernet frame in the media. The Data link layer of the destination computer picks the Ethernet frame from the media. After picking the Ethernet frame, the Data link layer of the destination computer unpacks, processes, and hands over that Ethernet frame to the upper layer for further processing.

If multiple protocols are running in the upper (network) layer of the destination computer, the data link layer will fail to hand over the received frame to the upper layer as it does not know to which protocol it should give the received frame.

The type field solves this issue. This field allows the sender computer to insert the information of the upper layer protocol. Through this information, the data link layer of the destination computer can easily determine the upper layer protocol to which it should hand over the received frame.

Modern LAN implementations mostly use the IP protocol in the network layer. There are two variants of the IP protocol; IPv4 and IPv6. If the type field has value IP or ox800, the frame is carrying the data of the IPv4 protocol. If the type field has value IPv6 or 0x86dd, the frame is carrying the data of the IPv6 protocol.

This value is set to 4.
