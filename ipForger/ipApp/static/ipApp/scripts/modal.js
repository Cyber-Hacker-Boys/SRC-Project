let explanationE = [
    '<b>Explanation:</b><br><br>The ethernet header is the last header added to the data in the physical TCP/IP layer.',
    '<b>Explanation:</b><br><br>This field is 6 bytes long. It contains the MAC address of the destination device. MAC address is 6 bytes or 48 bits (1 byte = 8 bits, 6x8 = 48bits) long. <br><br>For convenience, usually, it is written as 12-digit hexadecimal numbers (such as 0000.0A12.1234).',
    '<b>Explanation:</b><br>This field is also 6 bytes long. It contains the MAC address of the source device. It helps the receiving device in identifying the source device.',
    '<b>Explanation:</b><br>This field is 2 bytes long. This field stores information about the protocol of the upper layer (network layer).<br><br>' +
    'The Data Link layer of the source computer prepares, packs and loads the Ethernet frame in the media. The Data link layer of the destination computer picks the Ethernet frame from the media. After picking the Ethernet frame, the Data link layer of the destination computer unpacks, processes, and hands over that Ethernet frame to the upper layer for further processing.<br<br>' +
    'If multiple protocols are running in the upper (network) layer of the destination computer, the data link layer will fail to hand over the received frame to the upper layer as it does not know to which protocol it should give the received frame.<br><br>' +
    'The type field solves this issue. This field allows the sender computer to insert the information of the upper layer protocol. Through this information, the data link layer of the destination computer can easily determine the upper layer protocol to which it should hand over the received frame.<br><br>' +
    'Modern LAN implementations mostly use the IP protocol in the network layer. There are two variants of the IP protocol; IPv4 and IPv6. If the type field has <b>0x800</b>, the frame is carrying the data of the IPv4 protocol. If the type field has value <b>0x86dd</b>, the frame is carrying the data of the IPv6 protocol.'
];

let explanationI = [
    '<b>Explanation:</b><br>An IP header is bits of information attached to each data packet that is transported in the computer network. This information usually includes addressing and routing details which makes it possible to reassemble the packets and have the original data at the destination.<br><br>' +
    'The IPv4 header contains 13 fields. These fields are Version, Internet Header Length, Type of Service, Total Length, Identification, Flags, Fragment offset, Time-to-Live, Protocol, Header Checksum, Source address, Destination address, and Options.',
    '<b>Explanation:</b><br>This field sets the version of the IP protocol. As mentioned earlier, there are two versions of the IP protocol. If the value of this field is set to 4, then it indicates that the header belongs to the IPv4 protocol. The size of this field is 4 bits.',
    '<b>Explanation:</b><br>The size of this field is 4 bits. This field indicates the length of the IPv4 header. Not all IPv4 headers are equal in length. The length of the header depends on how many options are added. An option tells intermediate devices how packets should be forwarded or processed. Most IPv4 options are optional. Depending on the specific requirement, nodes can add options.<br><br>' +
    'The length of the header is calculated in the number of 4-byte blocks. To calculate the length, the number of bytes is divided by 4. For example, if the header contains 20 bytes, the header length in the 4-byte blocks will be 5 (20/4). Similarly, if the value in this field is 10, then the length of the header will be 10 x 4 = 40 bytes.<br><br>' +
    'If an IPv4 option is not an integral multiple of 4 bytes in length, the remaining bytes are filled through padding options. The minimum size of the IPv4 header is 20 bytes. The maximum size of the header including all options is 60 bytes.<br><br>' +
    '<b>Form Restriction: So the IHL can range from the value 5 to 15.</b>',
    '<b>Explanation:</b><br>This field is used to set the desired service expected by the packet for delivery through routers across the network. RFC 791 defines services for this field. The most common services are the precedence, delay, throughput, reliability, and cost characteristics. The size of this field is 8 bits.<br><br>' +
    'RFC 2474 updates the definition of this field. It renames the original field name as the Differentiated Services (DS) field and defines the bits of this field into two separate groups. In the first group, it defines the first (high-order) 6 bits. In the second group, it defines the last (low-order) 2 bits.<br><br>' +
    'The first 6 bits are used to mark, unmark, and classify packets for forwarding and routing. Nodes can prioritize packets based on the requirements of applications. For example, nodes may prioritize data packets of real-time applications (such as voice over IP and video) over other applications (such as email and file storage). Prioritized data packets take precedence over normal data packets in congested areas of the network. This feature is commonly known as QoS (Quality of Service).<br><br>' +
    'The last 2 bits are used for ECN (Explicit Congestion Notification). The ECN allows an intermediate device to send a notification to the sender device if it is not able to forward the packet due to congestion. ECN is defined in RFC 3168.<br><br>' + '' +
    '<b>Form Restriction: This field is now deprecated however routers still accept it and the value ranges from 0 to 7.</b>',
    '<b>Explanation:</b><br>This field specifies the total length of the packet. This length includes the length of the header and the length of the payload. By subtracting the header length from the total length, routers can calculate the length of the payload. The size of this field is 16 bits. Since a 16 bits field cannot store a value more than 65535, the maximum length of an IP packet can be 65535 bytes.<br><br>' +
    '<b>Form Restriction: This field accepts values from 0 to 65535.</b>',
    '<b>Explanation:</b><br>If the packet is large, the source node can fragment the packet. If the packet is fragmented all fragments retain the identification value. The destination node uses this value to reassemble the original packet from fragments. The size of this field is 16 bits.<br><br>' +
    '<b>Form Restriction: This field accepts values from 0 to 65535.</b>',
    '<b>Explanation:</b><br>This field is used to enable fragmentation. The size of this field is 3 bits. From these, only two bits are defined. The first bit indicates whether the packet can be fragmented or not. The second bit indicates whether more fragments follow the current fragment.<br><br>' +
    '<b>This field accepts the following options:</b> <ul><li><b>0</b>: Reserved</li> <li><b>DF</b>: Don\'t Fragment</li> <li><b>MF</b>: More Fragments</li></ul>',
    '<b>Explanation:</b><br>If the fragmentation is done, this field is used to indicate the position of the fragment relative to the beginning of the payload. The size of this field is 13 bits.<br><br>' +
    '<b>Form Restriction: This field accepts values from 0 to 65535.</b>',
    '<b>Explanation:</b><br>The size of this field is 8 bits. This field is used to discard the undeliverable packets. The original specification defines this field as a time counter. Intermediate routers determine the length of time required in seconds to forward the packet and decrement this time accordingly. This specification was updated later.<br><br>' +
    'In the modern specification, the sending node sets the maximum number of links on which the packet can travel before being discarded. When the packet crosses a router, the router decrements the TTL value by 1. If the TTL value equals 0 before reaching the destination, the packet is discarded and an ICMP Time Exceeded message is sent to the source of the packet.<br><br>' +
    '<b>Form Restriction: This field accepts values from 0 to 255.</b>',
    '<b>Explanation:</b><br>The size of this field is 8 bits. This field specifies the upper-layer protocol that will receive the payload of the packet on the destination node. For example, if this field contains a decimal value 17, then the Internet layer of the destination node will transfer the payload to the UDP protocol.<br><br>' +
    '<b>This field is based on the upper layer protocol and is set to:</b> <ul><li><b>6</b>: TCP</li> <li><b>17</b>: UDP</li> <li><b>1</b>: ICMP</li></ul>',
    '<b>Explanation:</b><br>The size of this field is 16 bits. This field provides a checksum on the header only. Since the payload contains its own checksum, the payload is not included in the checksum calculation. Intermediate routers that receive and forward the packet calculate and verify the checksum and discard the packet if checksum verification fails. Since a router decrements the TTL value by 1 before forwarding the packet, the header checksum value is recomputed at each hop between the source and destination nodes.<br><br>' +
    '<b>Form Restriction: This field accepts values from 0 to 65535.</b>',
    '<b>Explanation:</b><br>The size of this field is 32 bits. This field stores the IPv4 address of the sending device.<br><br>' +
    '<b>Form Restriction: This field is set with the IP address of the User.</b>',
    '<b>Explanation:</b><br>The size of this field is also 32 bits. This field stores the IPv4 address of the destination device.<br><br>' +
    '<b>Form Restriction: This field accepts values in format of an IPv4 Address.</b>',
    '<b>Explanation:</b><br>This field stores IPv4 options. The size of this field is a multiple of 32 bits. If an option is not 32 bits in the length, it uses padding options in the remaining bits to make the header an integral number of 4-byte blocks.<br><br>' +
    'The options field is not often used. Packets containing some options may be considered as dangerous by some routers and be blocked.<br><br>' +
    '<b>Form Restriction: The options need to have the type and length specified in hexadecimal for example \x44\x0A (Option 68- Timestamp, length 10).</b>'];

let explanationT = [
    '<b>Explanation:</b><br><br>Transmission Control Protocol is transport layer protocol that is widely used with Internet Protocol. A protocol is a set of procedures and rules that two computers follow to understand each other and exchange data.<br><br>' +
    'In overall TCP as the following features: <ul><li>Guarantees that data arrives as sent.</li> <li>Error-checks streams of data.</li> <li>A 20-byte header permits an optional 40 bytes of function data.</li> <li>Slower than UDP.</li> <li>Best for apps that require reliability.</li></ul>',
    '<b>Explanation:</b><br><br>The source TCP port number represents the sending device.<br><br>'+
    '<b>Form Restriction: This field accepts values from 0 to 65535.</b>',
    '<b>Explanation:</b><br><br>The destination TCP port number is the communication endpoint for the receiving device.<br><br>'+
    '<b>Form Restriction: This field accepts values from 0 to 65535.</b>',
    '<b>Explanation:</b><br><br>Message senders use sequence numbers to mark the ordering of a group of messages.<br><br>' +
    '<b>Form Restriction: This field accepts values from 0 to 4294967295.</b>',
    '<b>Explanation:</b><br><br>Both senders and receivers use the acknowledgment numbers field to communicate the sequence numbers of messages that are either recently received or expected to be sent.<br><br>' +
    '<b>Form Restriction: This field accepts values from 0 to 4294967295.</b>',
    '<b>Explanation:</b><br><br>The data offset field stores the total size of a TCP header in multiples of four bytes. A header not using the optional TCP field has a data offset of 5 (representing 20 bytes).<br><br>' +
    ' while a header using the maximum-sized optional field has a data offset of 15 (representing 60 bytes).<br><br>' +
    '<b>Form Restriction: So the Data Offset can range from the value 5 to 15.</b>',
    '<b>Explanation:</b><br><br>Reserved data in TCP headers always has a value of zero. This field aligns the total header size as a multiple of four bytes, which is important for the efficiency of computer data processing.<br><br>'+
    '<b>Form Restriction: This field is set to 0.</b>',
    '<b>Explanation:</b><br><br>TCP uses a set of six standard and three extended control flags—each an individual bit representing On or Off—to manage data flow in specific situations.',
    '<b>Explanation:</b><br><br>TCP senders use a number, called window size, to regulate how much data they send to a receiver before requiring an acknowledgment in return.<br><br>' +
    'If the window size is too small, network data transfer is unnecessarily slow. If the window size is too large, the network link may become saturated, or the receiver may not be able to process incoming data quickly enough, resulting in slow performance.<br><br>' +
    'Windowing algorithms built into the protocol dynamically calculate size values and use this field of TCP headers to coordinate changes between senders and receivers.',
    '<b>Explanation:</b><br><br>The checksum value inside a TCP header is generated by the protocol sender as a mathematical technique to help the receiver detect messages that are corrupted or tampered with.',
    '<b>Explanation:</b><br><br>The urgent pointer field is often set to zero and ignored, but in conjunction with one of the control flags, it can be used as a data offset to mark a subset of a message as requiring priority processing.',
    '<b>Explanation:</b><br><br>Usages of optional TCP data include support for special acknowledgment and window scaling algorithms.',
];

let explanationU = [
    '<b>Explanation:</b><br><br>User datagram protocol (UDP) operates on top of the Internet Protocol (IP) to transmit datagrams over a network. UDP does not require the source and destination to establish a three-way handshake before transmission takes place. Additionally, there is no need for an end-to-end connection.<br><br>' +
    'Since UDP avoids the overhead associated with connections, error checks and the retransmission of missing data, it’s suitable for real-time or high performance applications that don’t require data verification or correction. If verification is needed, it can be performed at the application layer.',
    '<b>Explanation:</b><br><br>The port of the device sending the data. This field can be set to zero if the destination computer doesn’t need to reply to the sender.',
    '<b>Explanation:</b><br><br>The destination UDP port number is the communication endpoint for the receiving device.',
    '<b>Explanation:</b><br><br>Specifies the number of bytes comprising the UDP header and the UDP payload data. The limit for the UDP length field is determined by the underlying IP protocol used to transmit the data.',
    '<b>Explanation:</b><br><br>The checksum allows the receiving device to verify the integrity of the packet header and payload. It is optional in IPv4 but was made mandatory in IPv6.'
];

let explanationIC = [
    '<b>Explanation:</b><br><br>ICMP (Internet Control Message Protocol) is an error-reporting protocol that network devices such as routers use to generate error messages to the source IP address when network problems prevent delivery of IP packets. ICMP creates and sends messages to the source IP address indicating that a gateway to the internet, such as a router, service or host, cannot be reached for packet delivery. Any IP network device has the capability to send, receive or process ICMP messages.<br><br>' +
    'ICMP is not a transport protocol that sends data between systems.<br><br>' +
    'While ICMP is not used regularly in end-user applications, it is used by network administrators to troubleshoot internet connections in diagnostic utilities including ping and traceroute.',
    '<b>Explanation:</b><br><br>The first 8 bits are the message types. Some common message types include the following:<ul><li>Type 0: Echo reply</li> <li>Type 3: Destination unreachable</li> <li>Type 5: Redirect</li> <li>Type 8: Echo</li></ul><br><br>' +
    'The type provides a brief explanation of what the message is for so the receiving network device knows why it is getting the message and how to treat it.',
    '<b>Explanation:</b><br><br>This field has 8 bits represent the message type code, which provides additional information about the error type.',
    '<b>Explanation:</b><br><br>The last 16 bits provide a message integrity check. The checksum shows the number of bits in the entire message and enables the ICMP tool to check for consistency with the ICMP message header to make sure the full range of data was delivered.'
];

let scanExplanation = '<b>Explanation:</b><br><br>The Internet Control Message Protocol (ICMP) is like the TCP protocol; both support protocols in the internet protocol suite. ICMP is used for checking live systems; ping is the most well-known utility that uses ICMP requests. Its principle is very simple—ICMP scanning sends requests to hosts and waits for an echo request to check whether the system is alive.';

let imageUrlE = [
    '../../static/ipApp/images/Ethernet/Ethernet.png',
    '../../static/ipApp/images/Ethernet/destEther.png',
    '../../static/ipApp/images/Ethernet/srcEther.png',
    '../../static/ipApp/images/Ethernet/typeEther.png'
]

let imageUrlI = [
    '../../static/ipApp/images/IP/Packets-IPV4.png',
    '../../static/ipApp/images/IP/Packets-IPV4-1.png',
    '../../static/ipApp/images/IP/Packets-IPV4-2.png',
    '../../static/ipApp/images/IP/Packets-IPV4-3.png',
    '../../static/ipApp/images/IP/Packets-IPV4-4.png',
    '../../static/ipApp/images/IP/Packets-IPV4-5.png',
    '../../static/ipApp/images/IP/Packets-IPV4-6.png',
    '../../static/ipApp/images/IP/Packets-IPV4-7.png',
    '../../static/ipApp/images/IP/Packets-IPV4-8.png',
    '../../static/ipApp/images/IP/Packets-IPV4-9.png',
    '../../static/ipApp/images/IP/Packets-IPV4-10.png',
    '../../static/ipApp/images/IP/Packets-IPV4-11.png',
    '../../static/ipApp/images/IP/Packets-IPV4-12.png',
    '../../static/ipApp/images/IP/Packets-IPV4-13.png'
];

let imageUrlT = [
       '../../static/ipApp/images/TCP/Packets-TCP.png',
       '../../static/ipApp/images/TCP/Packets-TCP-1.png',
       '../../static/ipApp/images/TCP/Packets-TCP-2.png',
       '../../static/ipApp/images/TCP/Packets-TCP-3.png',
       '../../static/ipApp/images/TCP/Packets-TCP-4.png',
       '../../static/ipApp/images/TCP/Packets-TCP-5.png',
       '../../static/ipApp/images/TCP/Packets-TCP-6.png',
       '../../static/ipApp/images/TCP/Packets-TCP-7.png',
       '../../static/ipApp/images/TCP/Packets-TCP-8.png',
       '../../static/ipApp/images/TCP/Packets-TCP-9.png',
       '../../static/ipApp/images/TCP/Packets-TCP-10.png',
       '../../static/ipApp/images/TCP/Packets-TCP-11.png'
];

let imageUrlU = [
       '../../static/ipApp/images/UDP/Packets-UDP.png',
       '../../static/ipApp/images/UDP/Packets-UDP-1.png',
       '../../static/ipApp/images/UDP/Packets-UDP-2.png',
       '../../static/ipApp/images/UDP/Packets-UDP-3.png',
       '../../static/ipApp/images/UDP/Packets-UDP-4.png'
];

let imageUrlIC = [
       '../../static/ipApp/images/ICMP/Packets-ICMP.png',
       '../../static/ipApp/images/ICMP/Packets-ICMP-1.png',
       '../../static/ipApp/images/ICMP/Packets-ICMP-2.png',
       '../../static/ipApp/images/ICMP/Packets-ICMP-3.png',
       '../../static/ipApp/images/ICMP/Packets-ICMP-4.png'
];

let imageScan = '../../static/ipApp/images/icmpScan.png';

function helpUser(title, text, url, packet) {
    let myModalEl = document.getElementById('helpModal');

    console.log(title)
    myModalEl.addEventListener('shown.bs.modal', function (e) {
        document.getElementById('helpModalLabel').innerHTML = title;
        switch (packet) {
            case 0:
                document.getElementById('helpModalText').innerHTML = explanationE[text];
                document.getElementById('helpModelImage').src = imageUrlE[url];
                break;
            case 1:
                document.getElementById('helpModalText').innerHTML = explanationI[text];
                document.getElementById('helpModelImage').src = imageUrlI[url];
                break;
            case 2:
                document.getElementById('helpModalText').innerHTML = explanationT[text];
                document.getElementById('helpModelImage').src = imageUrlT[url];
                break;
            case 3:
                document.getElementById('helpModalText').innerHTML = explanationU[text];
                document.getElementById('helpModelImage').src = imageUrlU[url];
                break;
            case 4:
                document.getElementById('helpModalText').innerHTML = explanationIC[text];
                document.getElementById('helpModelImage').src = imageUrlIC[url];
                break;
            case 5:
                document.getElementById('helpModalText').innerHTML = scanExplanation;
                document.getElementById('helpModelImage').src = imageScan;
                break;
            default:
                break;
        }
        document.getElementById("spinner").style.display = "none";
    })

    myModalEl.addEventListener('hidden.bs.modal', function (event) {
        document.getElementById("spinner").style.display = "revert";
    })
}

function addOption() {

     document.getElementById("dataT").value = "";

    for (let i = 1; i <= 4; i++) {
        let opt = document.getElementById("opt1-"+i);
        if (opt.checked){
            document.getElementById("dataT").value += opt.name +",";
            document.getElementById("optionsTCP").value += opt.value + ",";
        }
    }
    $('#optionsModal').modal('toggle');
}

function addFlag() {

     document.getElementById("cFlags").value = "";

    for (let i = 1; i <= 9; i++) {
        let opt = document.getElementById("flag"+i);
        if (opt.checked){
            document.getElementById("cFlags").value += opt.value;
        }
    }

    $('#flagModal').modal('toggle');
}


function addOptionI() {
    let opt = document.getElementById("optI").value;

    document.getElementById("optIPT").value = "["+opt+"],";
    $('#optionsTModal').modal('toggle');
}

$('form').submit(function(){
    $("form :disabled").removeAttr('disabled');
});

function scan() {
    Swal.fire({
      title: 'Scan in progress!',
        html:'<div id="basicUsage">00:00:00</div>',
      allowOutsideClick: false,
      didOpen: () => {
        Swal.showLoading();
      var timer = new Timer();
        timer.start();

        timer.addEventListener('secondsUpdated', function (e) {
            $('#basicUsage').html(timer.getTimeValues().toString());
        });
      }
    });
}