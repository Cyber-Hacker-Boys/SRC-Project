let explanationE = [
    '<b>Explanation:</b><br><br>The ethernet header is the last header added to the data in the physical TCP/IP layer.',
    '<b>Explanation:</b><br><br>This field is 6 bytes long. It contains the MAC address of the destination device. MAC address is 6 bytes or 48 bits (1 byte = 8 bits, 6x8 = 48bits) long. <br><br>For convenience, usually, it is written as 12-digit hexadecimal numbers (such as 0000.0A12.1234).',
    '<b>Explanation:</b><br>This field is also 6 bytes long. It contains the MAC address of the source device. It helps the receiving device in identifying the source device. The image above shows an example of both types of address in the frame.',
    '<b>Explanation:</b><br>This field is 2 bytes long. This field stores information about the protocol of the upper layer (network layer).<br><br>' +
    'The Data Link layer of the source computer prepares, packs and loads the Ethernet frame in the media. The Data link layer of the destination computer picks the Ethernet frame from the media. After picking the Ethernet frame, the Data link layer of the destination computer unpacks, processes, and hands over that Ethernet frame to the upper layer for further processing.<br<br>' +
    'If multiple protocols are running in the upper (network) layer of the destination computer, the data link layer will fail to hand over the received frame to the upper layer as it does not know to which protocol it should give the received frame.<br><br>' +
    'The type field solves this issue. This field allows the sender computer to insert the information of the upper layer protocol. Through this information, the data link layer of the destination computer can easily determine the upper layer protocol to which it should hand over the received frame.<br><br>' +
    'Modern LAN implementations mostly use the IP protocol in the network layer. There are two variants of the IP protocol; IPv4 and IPv6. If the type field has <b>0x800</b>, the frame is carrying the data of the IPv4 protocol. If the type field has value <b>0x86dd</b>, the frame is carrying the data of the IPv6 protocol.'
];

let explanationI = [
    '<b>Explanation:</b><br>An IP header is bits of information attached to each data packet that is transported in the computer network. This information usually includes addressing and routing details which makes it possible to reassemble the packets and have the original data at the destination.<br><br>' +
    'The IPv4 header contains 13 fields. These fields are Version, Internet Header Length, Type of Service, Total Length, Identification, Flags, Fragment offset, Time-to-Live, Protocol, Header Checksum, Source address, Destination address, and Options. The following image shows how these fields are arranged in the IP header',
    ''
]

let imageUrlE = [
    '../../static/ipApp/images/Ethernet.png',
    '../../static/ipApp/images/destEther.png',
    '../../static/ipApp/images/srcEther.png',
    '../../static/ipApp/images/typeEther.png'
]

let imageUrlI = [
    '../../static/ipApp/images/Packets-IPV4.png',
    '../../static/ipApp/images/Packets-IPV4-1.png',
    '../../static/ipApp/images/Packets-IPV4-2.png',
    '../../static/ipApp/images/Packets-IPV4-3.png',
    '../../static/ipApp/images/Packets-IPV4-4.png',
    '../../static/ipApp/images/Packets-IPV4-5.png',
    '../../static/ipApp/images/Packets-IPV4-6.png',
    '../../static/ipApp/images/Packets-IPV4-7.png',
    '../../static/ipApp/images/Packets-IPV4-8.png',
    '../../static/ipApp/images/Packets-IPV4-9.png',
    '../../static/ipApp/images/Packets-IPV4-10.png',
    '../../static/ipApp/images/Packets-IPV4-11.png',
    '../../static/ipApp/images/Packets-IPV4-12.png',
    '../../static/ipApp/images/Packets-IPV4-13.png'
]

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
            default:
                break;
        }
        document.getElementById("spinner").style.display = "none";
    })

    myModalEl.addEventListener('hidden.bs.modal', function (event) {
        document.getElementById("spinner").style.display = "revert";
    })
}

