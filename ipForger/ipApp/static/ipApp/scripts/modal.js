let explanationE = [
    'The ethernet header is the first piece added to the data in the second layer.',
    'The Mac Address of the destination.',
    'The Mac Address of the source.',
    'Defines the type of protocol inside the frame, for example IPv4 or IPv6.'
];

let imageUrlE = [
    '../../static/ipApp/images/Ethernet.png',
    '../../static/ipApp/images/destEther.png',
    '../../static/ipApp/images/srcEther.png',
    '../../static/ipApp/images/typeEther.png'
]

function helpUser(title, text, url, packet) {
    var myModalEl = document.getElementById('helpModal');
    console.log(title)
    myModalEl.addEventListener('shown.bs.modal', function (e) {
        document.getElementById('helpModalLabel').innerHTML = title;
        switch (packet) {
            case 0:
                document.getElementById('helpModalText').innerHTML = explanationE[text];
                document.getElementById('helpModelImage').src = imageUrlE[url];
                break;
            default:
                break;
        }

    })
}

