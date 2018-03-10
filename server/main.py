
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room

import model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Create instances from classes in model.py
session_handler = model.SessionHandler()
message_handler = model.MessageHandler()

# Return index.html
@app.route("/")
def index():
    """Return HTML"""
    return render_template('index.html')

## Receivable event from client to server
# Reserved events
@socketio.on('connect')
def test_connect():
    """Gets fired on any client-server connection"""
    session_handler.add_client(request.sid)
    print("Connected:", request.sid)

@socketio.on('disconnect')
def test_disconnect():
    """Gets fired on any client-server disconnect"""
    session_handler.remove_client(request.sid)
    print('Disconnected:', request.sid)

# Custom events
@socketio.on('message_from_client') #  Event name is crucial.
def handle_my_custom_event(json_data):
    """Use this function to receive events from the client.
       A JSON is always sent along and it hold all necessary data."""
    message_handler.process_message(request.sid, json_data)
    print("MAIN: Received a message and forwarding to MessageHandler.")


## Emit events to one client as response
def emit_event(event_name, json_data):
    """Use this function to emit events to the client which sent data.
       A JSON is always sent along and it hold all necessary data.
       This is not a broadcasting to all clients!"""
    emit(event_name, json_data)
    print("MAIN: Sending to one client as response: ",event_name)


## Emit events to all clients as broadcast
def emit_event_to_all_clients(event_name, json_data):
    """Use this function to emit events to all clients as broadcast.
       A JSON is always sent along and it hold all necessary data."""
    print("MAIN: Sending to all clients: ",event_name)


# Boilerplate starts SocketIO instead of standard flask.
if __name__ == '__main__':
    socketio.run(app)


"""
Notes:
send() and emit() is used in client
context for answering.
socketio.send() and socketio.emit() is
used when server starts communication.

json.loads() --> string to json
json.dumps() --> json to string

request.sid --> unique session ID for each client connection
"""
