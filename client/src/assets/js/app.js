import $ from 'jquery';
import whatInput from 'what-input';
import io from 'socket.io-client'

window.$ = $;

import Foundation from 'foundation-sites';
// If you want to pick and choose which modules to include, comment out the above and uncomment
// the line below
//import './lib/foundation-explicit-pieces';


$(document).foundation();

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function(data) {
    console.log("Socket connection to server established.")
});

socket.on('message_to_client', function(data) {
    // convert data
    var msg = JSON.stringify(data);

    // print msg
    $('#from-server').html(msg);
    console.log(msg);

    var data = {"type": "echo", "data": msg}
    socket.emit("message_from_client", JSON.stringify(data));
});

// Hier kommen alle Events rein, die vom Server empfangen werden koennen. Einfach wie die Beispiele oben.

$('#player').submit(function(e){
  e.preventDefault();

  var name = $(this).serializeArray(),
      myJSON = {};

  myJSON.type = "game_start"
  myJSON.data = {"name": name[0].value};


  console.log('this was sent to the server:', JSON.stringify(myJSON));
  socket.emit('message_from_client', JSON.stringify(myJSON));

});
