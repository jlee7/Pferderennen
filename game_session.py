""" Game Session """

import json
import player

class GameSession:
    """ GameSession holds all data regarding to one game with several
        players. """
    def __init__(self):
        #self.players = list()
        self.players = dict()
        self.host = None

    # ABOUT THE PLAYERS
    def add_player(self, session_id, is_host, json_data):
        """ Adds a player by its session ID to the players list. """
        print(session_id, is_host)
        self.players[session_id] = player.Player(session_id, is_host, json.loads(json_data)["data"]["name"])

    def remove_player(self, session_id):
        """ Removes a player from the list. Since the list holds players
            instances, the session ID of each instance must be checked.
            If match, the index if the instance is used to delete it from
            the list. """
        if len(self.players) > 0:
            del self.players[session_id]
        else:
            print("List of players is empty.")

    def list_players(self):
        """ Can be removed after finishing. """
        print(self.players)

    def check_if_player_exists(self, session_id):
        """ Check if player has been added or not deleted before. """
        if session_id in self.players:
            return True
        else:
            return False
    # --------------------------------------------------------------------------

    # ABOUT THE GAME
    def start_game(self):
        pass

    def end_game(self):
        pass

    def send_quizzes_to_players(self):
        pass


    # --------------------------------------------------------------------------
