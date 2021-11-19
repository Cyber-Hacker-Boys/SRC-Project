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
    var data = JSON.parse(event.data);
    console.log(data);
/*
    let line = document.createElement("li");
    line.classList.add("new");
    let node = document.createTextNode(data);
    line.appendChild(node);

    let list = document.getElementById("table");
    list.insertBefore(line, list.firstChild);*/

    let row = document.createElement("tr");
    let line = document.createElement("td");
    let node = document.createTextNode(data);
    line.appendChild(node);
    row.appendChild(line)

    let list = document.getElementById("entrie");
    list.insertBefore(row, list.firstChild);
}