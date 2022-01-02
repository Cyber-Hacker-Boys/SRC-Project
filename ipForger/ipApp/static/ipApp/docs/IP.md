#Header Explanation

##IPv4 Header

An IP header is bits of information attached to each data packet that is transported in the computer network. This information usually includes addressing and routing details which makes it possible to reassemble the packets and have the original data at the destination.

The IPv4 header contains 13 fields. These fields are Version, Internet Header Length, Type of Service, Total Length, Identification, Flags, Fragment offset, Time-to-Live, Protocol, Header Checksum, Source address, Destination address, and Options. The following image shows how these fields are arranged in the IP header.

###Version
This field sets the version of the IP protocol. As mentioned earlier, there are two versions of the IP protocol. If the value of this field is set to 4, then it indicates that the header belongs to the IPv4 protocol. The size of this field is 4 bits.

###IHL (Internet Header Length)
The size of this field is 4 bits. This field indicates the length of the IPv4 header. Not all IPv4 headers are equal in length. The length of the header depends on how many options are added. An option tells intermediate devices how packets should be forwarded or processed. Most IPv4 options are optional. Depending on the specific requirement, nodes can add options.

The length of the header is calculated in the number of 4-byte blocks. To calculate the length, the number of bytes is divided by 4. For example, if the header contains 20 bytes, the header length in the 4-byte blocks will be 5 (20/4). Similarly, if the value in this field is 10, then the length of the header will be 10 x 4 = 40 bytes.

If an IPv4 option is not an integral multiple of 4 bytes in length, the remaining bytes are filled through padding options. The minimum size of the IPv4 header is 20 bytes. The maximum size of the header including all options is 60 bytes.

So the IHL can range from the value 5 to 15.

###TOS
This field is used to set the desired service expected by the packet for delivery through routers across the network. RFC 791 defines services for this field. The most common services are the precedence, delay, throughput, reliability, and cost characteristics. The size of this field is 8 bits.

RFC 2474 updates the definition of this field. It renames the original field name as the Differentiated Services (DS) field and defines the bits of this field into two separate groups. In the first group, it defines the first (high-order) 6 bits. In the second group, it defines the last (low-order) 2 bits.

The first 6 bits are used to mark, unmark, and classify packets for forwarding and routing. Nodes can prioritize packets based on the requirements of applications. For example, nodes may prioritize data packets of real-time applications (such as voice over IP and video) over other applications (such as email and file storage). Prioritized data packets take precedence over normal data packets in congested areas of the network. This feature is commonly known as QoS (Quality of Service).

The last 2 bits are used for ECN (Explicit Congestion Notification). The ECN allows an intermediate device to send a notification to the sender device if it is not able to forward the packet due to congestion. ECN is defined in RFC 3168.

This field is now deprecated however routers still accept it and the value ranges from 0 to 7.

###Total Length
This field specifies the total length of the packet. This length includes the length of the header and the length of the payload. By subtracting the header length from the total length, routers can calculate the length of the payload. The size of this field is 16 bits. Since a 16 bits field cannot store a value more than 65535, the maximum length of an IP packet can be 65535 bytes.

This field accepts values from 0 to 65535.

###Identification
If the packet is large, the source node can fragment the packet. If the packet is fragmented all fragments retain the identification value. The destination node uses this value to reassemble the original packet from fragments. The size of this field is 16 bits.

This field accepts values from 0 to 65535.


###Flags
This field is used to enable fragmentation. The size of this field is 3 bits. From these, only two bits are defined. The first bit indicates whether the packet can be fragmented or not. The second bit indicates whether more fragments follow the current fragment.

This field accepts the following options:
- 0: Reserved;
- DF: Don't Fragment
- MF: More Fragments

###Fragment Offset
If the fragment is done, this field is used to indicate the position of the fragment relative to the beginning of the payload. The size of this field is 13 bits.

This field accepts values from 0 to 65535.

###TTL
The size of this field is 8 bits. This field is used to discard the undeliverable packets. The original specification defines this field as a time counter. Intermediate routers determine the length of time required in seconds to forward the packet and decrement this time accordingly. This specification was updated later.

In the modern specification, the sending node sets the maximum number of links on which the packet can travel before being discarded. When the packet crosses a router, the router decrements the TTL value by 1. If the TTL value equals 0 before reaching the destination, the packet is discarded and an ICMP Time Exceeded message is sent to the source of the packet.

This field accepts values from 0 to 255.

###Protocols
The size of this field is 8 bits. This field specifies the upper-layer protocol that will receive the payload of the packet on the destination node. For example, if this field contains a decimal value 17, then the Internet layer of the destination node will transfer the payload to the UDP protocol.

This field is based on the upper layer protocol and is set to:
- 6: TCP
- 17: UDP
- 1: ICMP

###Header Checksum
The size of this field is 16 bits. This field provides a checksum on the header only. Since the payload contains its own checksum, the payload is not included in the checksum calculation. Intermediate routers that receive and forward the packet calculate and verify the checksum and discard the packet if checksum verification fails. Since a router decrements the TTL value by 1 before forwarding the packet, the header checksum value is recomputed at each hop between the source and destination nodes.

This field accepts values from 0 to 65535.

###Source Address
The size of this field is 32 bits. This field stores the IPv4 address of the sending device.

This field is set with the IP address of the User

###Destination Address
The size of this field is also 32 bits. This field stores the IPv4 address of the destination device.

This field accepts values in format of an IPv4 Address

###Options
This field stores IPv4 options. The size of this field is a multiple of 32 bits. If an option is not 32 bits in the length, it uses padding options in the remaining bits to make the header an integral number of 4-byte blocks.

The options field is not often used. Packets containing some options may be considered as dangerous by some routers and be blocked.

The options need to have the type and length specified in hexadecimal for example \x44\x0A (Option 68- Timestamp, length 10)