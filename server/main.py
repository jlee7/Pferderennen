import json
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room

import model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Create Session instance from model.py
game_session = model.Session()

# Return index.html----------------------
@app.route("/")
def index():
    return render_template('index.html')
# ---------------------------------------

# Receivable event from client to server
@socketio.on('message_from_client') #  Event name is crucial.
def handle_my_custom_event(json_data):
    """Use this function to receive events from the client.
       A JSON is always sent along and it hold all necessary data."""
    #print("Got RAW message from client:",json_data)
    #print("Got message from client:", json.loads(json_data))
    print("MAIN: Request.SID:", request.sid)
    if json.loads(json_data)["type"] == "echo":
        print("MAIN: Event Type:", json_loads(json_data)["type"])
    elif json.loads(json_data)["type"] == "game_start":
        game_session.add_player(request.sid, json_data)

    #emit_event("message_to_client", json_data)
    #emit_event_to_all_clients("message_to_client", json_data)
# ----------------------------------------

# Emit events to one client as response
def emit_event(event_name, json_data):
    """Use this function to emit events to the client which sent data.
       A JSON is always sent along and it hold all necessary data.
       This is not a broadcasting to all clients!"""
    emit(event_name, json_data)
    print("MAIN: Sending to one client as response: ",event_name)
# ----------------------

# Emit events to all clients as broadcast
def emit_event_to_all_clients(event_name, json_data):
    """Use this function to emit events to all clients as broadcast.
       A JSON is always sent along and it hold all necessary data."""
    socketio.emit(event_name, json_data)
    print("MAIN: Sending to all clients: ",event_name)
# ---------------------------------------

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
"""
