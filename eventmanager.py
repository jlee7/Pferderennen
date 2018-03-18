""" This file contains the event manager for this application. """
import json
import game_session

class EventManager:
    """ The EventManager receives all incoming messages
        and processes them."""
    def __init__(self):
        self.game = game_session.GameSession()

    def process_message(self, session_id, json_data):
        """Processes each message type defined in "type" in JSON."""
        print("MODEL: Event Type:", json.loads(json_data)["type"])

        if json.loads(json_data)["type"] == "echo":
            print("MODEL:", session_id, json_data)

        elif json.loads(json_data)["type"] == "connect":
            pass

        elif json.loads(json_data)["type"] == "disconnect":
            self.game.remove_player(session_id)
            #print("MODEL:", session_id, json_data)

        elif json.loads(json_data)["type"] == "game_start":
            print("MODEL:", session_id, json_data)
            if self.game.check_if_player_exists(session_id):
                print("Player already exists.")

            else:
                self.game.add_player(session_id)
                self.game.list_players()

        elif json.loads(json_data)["type"] == "":
            pass



        #emit_event("message_to_client", json_data)
        #emit_event_to_all_clients("message_to_client", json_data)
