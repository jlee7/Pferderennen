from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def hello_world():
    return """Hello World!
    <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/socket.io/1.3.6/socket.io.min.js"></script>
    <script type="text/javascript" charset="utf-8">
    var socket = io.connect('http://127.0.0.1:5000/);
    socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
</script>"""



@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))




if __name__ == '__main__':
    socketio.run(app)