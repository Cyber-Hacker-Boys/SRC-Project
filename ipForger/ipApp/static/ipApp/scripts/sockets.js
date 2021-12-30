var loc = window.location;

var socket = new WebSocket('ws://localhost:8000/ws/ip_forger/')

socket.onopen = function(e){
    console.log("open", e);
};
socket.onerror = function(e){
    console.log("error", e)
};
socket.onclose = function(e){
    console.log("close", e)
};
socket.onmessage = function (event) {
    var data = event.data;
    console.log(data);
/*
    let line = document.createElement("li");
    line.classList.add("new");
    let node = document.createTextNode(data);
    line.appendChild(node);

    let list = document.getElementById("table");
    list.insertBefore(line, list.firstChild);*/

    let row = document.createElement("tr");
    let line1 = document.createElement("td");
    let line2 = document.createElement("td");
    let line3 = document.createElement("td");
    let node = document.createTextNode("1");
    let node2 = document.createTextNode("55");
    let node3 = document.createTextNode("1");
    line1.appendChild(node);
    line2.appendChild(node2);
    line3.appendChild(node3);
    row.appendChild(line1);
    row.appendChild(line2);
    row.appendChild(line3);

    let list = document.getElementById("entrie");
    list.insertBefore(row, list.firstChild);
}