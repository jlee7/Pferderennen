from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import json

import game_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # super secret
socketio = SocketIO(app)

# Import game components
lobby = list()
game_session = game_session.GameSession()

# Return index.html
@app.route("/")
def index():
    """Return HTML"""
    return render_template('index.html')

# Reserved event: Connect
@socketio.on('connect')
def test_connect():
    """Gets fired on any client-server connection"""
    print("SocketIO: Connected:", request.sid)
    lobby.append(request.sid)
    process_message(request.sid, """{"type": "connect"}""")
    print("LOBBY:", lobby)

# Reserved event: Disconnect
@socketio.on('disconnect')
def test_disconnect():
    """Gets fired on any client-server disconnect"""
    print('SocketIO: Disconnected:', request.sid)
    lobby.remove(request.sid)
    process_message(request.sid, """{"type": "disconnect"}""")
    print("LOBBY:", lobby)

# Custom event: Any message from client
@socketio.on('message_from_client') #  Event name is crucial.
def handle_my_custom_event(json_data):
    """Use this function to receive events from the client.
       A JSON is always sent along and it hold all necessary data."""
    print("SocketIO: Received a message and forwarding to MessageHandler.")
    process_message(request.sid, json_data)

# Emit events to one client as response
def emit_event(event_name, json_data):
    """Use this function to emit events to the client which sent data.
       A JSON is always sent along and it hold all necessary data.
       This is not a broadcasting to all clients!"""
    print("SocketIO: Sending to one client as response: ",event_name)
    emit(event_name, json_data)

# Emit events to all clients as broadcast
def emit_event_to_all_clients(event_name, json_data):
    """Use this function to emit events to all clients as broadcast.
       A JSON is always sent along and it hold all necessary data."""
    print("SocketIO: Sending to all clients: ",event_name)
    socketio.emit(event_name, json_data)

# ALL EVENTS ARE PROCESSED HERE --------------------------------
def process_message(session_id, json_data):
    """Processes each message type defined in "type" in JSON."""
    print("PROCESSING: Event Type:", json.loads(json_data)["type"])

    data = json.loads(json_data)

    if data["type"] == "echo":
        pass
        #print("PROCESSING:", session_id, json_data)

    elif data["type"] == "connect":
        print("PROCESSING: Someone has connected to the Server: ", session_id)
        print("PROCESSING: Sending a few JSON examples to clients.")

        test_json_1 = """{"type": "test_json_1", "data": {"name": "Manuel","real age": "over 30","menthal age": "9"}}"""
        test_json_2 = """{'type': 'test_json_2', 'data': {'name': 'Manuel','real age': 'over 30','menthal age': '9'}}"""
        test_json_3 = """{type: test_json_3, data: {name: Manuel,real age: over 30,menthal age: 9}}"""

        #emit_event_to_all_clients("message_to_client", test_json_1)
        #emit_event_to_all_clients("message_to_client", """{"type": "to_all_clients"}""")
        # emit_event("message_to_client", test_json_1)
        # emit_event("message_to_client", test_json_2)
        # emit_event("message_to_client", test_json_3)

    elif data["type"] == "disconnect":
        print("PROCESSING: Someone disconnected: ", session_id)
        game_session.remove_player(session_id)

    elif data["type"] == "game_start":
        print("PROCESSING:", session_id, json_data)
        if game_session.check_if_player_exists(session_id):
            print("PROCESSING: Player already exists.")
        else:
            if session_id == lobby[0]:
                is_host = True
                emit_event("message_to_client", """{"type": "is_host", "data": "You are host"}""")
            else:
                is_host = False
                emit_event("message_to_client", """{"type": "is_host", "data": "You are not host"}""")

            game_session.add_player(session_id, is_host, json_data)
            game_session.list_players()
            print("PROCESSING: Player has been added to session:", session_id)

        check_players_in_session()

    elif data["type"] == "":
        pass
#----------------------------------------------------------------

## GAME MODEL
def check_players_in_session():
    print("Current players:", len(game_session.players))




# Boilerplate starts SocketIO instead of standard flask.
if __name__ == '__main__':
    socketio.run(app)
    # socketio.run(app, host="192.168.178.23", port="5001")


"""
Notes:
send() and emit() is used in client context for answering.
socketio.send() and socketio.emit() is used when server starts communication.

json.loads() --> string to json
json.dumps() --> json to string

request.sid --> unique session ID for each client connection
"""
