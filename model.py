""" This file contains all classes for the game. """

import json


class Player:
    def __init__(self, session_id, name):
        self.name = str(name)
        self.session_id = session_id


class EventManager:
    """ The EventManager receives all incoming messages
        and processes them."""
    def __init__(self):
        self.players = dict()

    def list_players(self):
        """Prints all players to console."""
        for player in self.players:
            print(player)

    def check_if_session_id_exists(self, session_id):
        """Returns True if SID already exists."""
        if session_id in self.players:
            print("Session ID exists:", session_id)
            return True

    def process_message(self, session_id, json_data):
        """Processes each message type defined in "type" in JSON."""
        print("MODEL: Event Type:", json.loads(json_data)["type"])

        if json.loads(json_data)["type"] == "echo":
            print("MODEL:", session_id, json_data)

        elif json.loads(json_data)["type"] == "connect":
            pass

        elif json.loads(json_data)["type"] == "disconnect":
            print("MODEL:", session_id, json_data)
            if session_id in self.players:
                del(self.players[session_id])

        elif json.loads(json_data)["type"] == "game_start":
            print("MODEL:", session_id, json_data)
            if self.check_if_session_id_exists(session_id):
                print("MODEL: Cannot add player because SID already exists.")
                self.list_players()
            else:
                self.players[session_id] = Player(session_id, json.loads(json_data)["data"]["name"])
                self.list_players()
                print(self.players)

        elif json.loads(json_data)["type"] == "":
            pass



        #emit_event("message_to_client", json_data)
        #emit_event_to_all_clients("message_to_client", json_data)
