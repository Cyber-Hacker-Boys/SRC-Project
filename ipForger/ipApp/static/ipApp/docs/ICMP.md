#Packet Explanation

##ICMP Packet
ICMP (Internet Control Message Protocol) is an error-reporting protocol that network devices such as routers use to generate error messages to the source IP address when network problems prevent delivery of IP packets. ICMP creates and sends messages to the source IP address indicating that a gateway to the internet, such as a router, service or host, cannot be reached for packet delivery. Any IP network device has the capability to send, receive or process ICMP messages.

ICMP is not a transport protocol that sends data between systems.

While ICMP is not used regularly in end-user applications, it is used by network administrators to troubleshoot internet connections in diagnostic utilities including ping and traceroute.

###Type
The first 8 bits are the message types. Some common message types include the following:
- Type 0: Echo reply
- Type 3: Destination unreachable
- Type 5: Redirect
- Type 8: Echo

The type provides a brief explanation of what the message is for so the receiving network device knows why it is getting the message and how to treat it.

###Code
This field has 8 bits represent the message type code, which provides additional information about the error type.

###Checksum
The last 16 bits provide a message integrity check. The checksum shows the number of bits in the entire message and enables the ICMP tool to check for consistency with the ICMP message header to make sure the full range of data was delivered.
