""" This file contains all classes for the game. """

import json

class Player:
    def __init__(self, session_id, name):
        self.name = str(name)
        self.session_id = session_id



class MessageHandler:
    """ The MessageHandler receives all incoming messages
        and processes them."""
    def __init__(self):
        pass

    def process_message(self, session_id, json_data):
        #print("Got RAW message from client:",json_data)
        #print("Got message from client:", json.loads(json_data))
        print("MAIN: Request.SID:", session_id)
        if json.loads(json_data)["type"] == "echo":
            print("MAIN: Event Type:", json_loads(json_data)["type"])
        #elif json.loads(json_data)["type"] == "game_start":
            #game_session.add_player(session_id, json_data)

        #emit_event("message_to_client", json_data)
        #emit_event_to_all_clients("message_to_client", json_data)


class SessionHandler:
    """ The SessionHandler receives all Session IDs (request.sid)
        and knows about all connected and disconnected clients."""
    def __init__(self):
        self.players = list()

    def check_if_already_exists(self, session_id):
        print([x for x in self.players])
        if session_id in [x for x in self.players]:
            print("MODEL: Already taken.")
            return False
        else:
            print("MODEL: Can be added.")
            return True

    def add_client(self, session_id):
        if self.check_if_already_exists(session_id):
            self.players.append(session_id)
            print("MODEL: Player added to Session.")
            print("MODEL:", self.players)

    def remove_client(self, session_id):
        self.players.remove(session_id)
        print("MODEL: Player removed from Session.")
        print("MODEL:", self.players)
