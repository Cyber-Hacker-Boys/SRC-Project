#Packet Explanation

##TCP Packet
Transmission Control Protocol is transport layer protocol that is widely used with Internet Protocol. A protocol is a set of procedures and rules that two computers follow to understand each other and exchange data.
In overall TCP as the following features:
- Guarantees that data arrives as sent.
- Error-checks streams of data.
- A 20-byte header permits an optional 40 bytes of function data.
- Slower than UDP.
- Best for apps that require reliability.

###Source Port
The source TCP port number represents the sending device.

###Destination Port
The destination TCP port number is the communication endpoint for the receiving device.

###Sequence Number
Message senders use sequence numbers to mark the ordering of a group of messages.

###Acknowledgment number
Both senders and receivers use the acknowledgment numbers field to communicate the sequence numbers of messages that are either recently received or expected to be sent.

###Data Offset
The data offset field stores the total size of a TCP header in multiples of four bytes. A header not using the optional TCP field has a data offset of 5 (representing 20 bytes), while a header using the maximum-sized optional field has a data offset of 15 (representing 60 bytes).

###Reserved Data
 Reserved data in TCP headers always has a value of zero. This field aligns the total header size as a multiple of four bytes, which is important for the efficiency of computer data processing.
 
###Control Flags
TCP uses a set of six standard and three extended control flags—each an individual bit representing On or Off—to manage data flow in specific situations.

###Windows Size
TCP senders use a number, called window size, to regulate how much data they send to a receiver before requiring an acknowledgment in return. 

If the window size is too small, network data transfer is unnecessarily slow. If the window size is too large, the network link may become saturated, or the receiver may not be able to process incoming data quickly enough, resulting in slow performance.

Windowing algorithms built into the protocol dynamically calculate size values and use this field of TCP headers to coordinate changes between senders and receivers.

###Checksum
The checksum value inside a TCP header is generated by the protocol sender as a mathematical technique to help the receiver detect messages that are corrupted or tampered with.
 
###Urgent Pointer
The urgent pointer field is often set to zero and ignored, but in conjunction with one of the control flags, it can be used as a data offset to mark a subset of a message as requiring priority processing.

###Optional Data
Usages of optional TCP data include support for special acknowledgment and window scaling algorithms.