from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)




# Index HTML
@app.route("/")
def index():
    return render_template('index.html')

# Receiving messages
@socketio.on('message_from_client')
def handle_my_custom_event(json):
    #print('received json: ' + str(json))
    print('Message from client: ' + json["data"])
    emit('message_to_client', {'data': 'SOME_OTHER_EVENT'})

@socketio.on('another_message_from_client')
def handle_my_custom_event(json):
    #print('received json: ' + str(json))
    print('Another message from client: ' + json["data"])


# Boilerplate starts SocketIO instead of standard flask.
if __name__ == '__main__':
    socketio.run(app)