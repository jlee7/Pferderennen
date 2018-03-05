from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

<<<<<<< HEAD
# import game_model
>>>>>>> 3005e3217fff5a72fb4293ff4606eb66a1c09da6

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# Index HTML
@app.route("/")
def index():
    return render_template('index.html')

# Receiving events
# Test events ---------------------------
@socketio.on('message_from_client')
def handle_my_custom_event(json):
    #print('received json: ' + str(json))
    print('Message from client: ' + json["data"])
    emit('message_to_client', {'data': 'SOME_OTHER_EVENT'})

@socketio.on('another_message_from_client')
def handle_my_custom_event(json):
    #print('received json: ' + str(json))
    print('Another message from client: ' + json["data"])
# ---------------------------------------

# Receivable events from client to server
@socketio.on('name_of_client')
def handle_my_custom_event(json):
    pass

@socketio.on('')
def handle_my_custom_event(json):
    pass

@socketio.on('')
def handle_my_custom_event(json):
    pass
# ----------------------------------------

# Emit events to clients
def emit_event(event_name, json):
    emit(event_name, json)
    print("Sending to clients",
event_name)
# ----------------------



# Boilerplate starts SocketIO instead of standard flask.
if __name__ == '__main__':
    socketio.run(app)


"""
Notes:
send() and emit() is used in client
context for answering.
socketio.send() and socketio.emit() is
used when server starts communication.
"""
