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

    let line = document.createElement("li");
    line.classList.add("list-group-item");
    let node = document.createTextNode(data);
    line.appendChild(node);

    let list = document.getElementById("table");
    list.appendChild(line);
}