""" Game Session """

import json
import player

class GameSession:
    """ GameSession holds all data regarding to one game with several
        players. """
    def __init__(self):
        self.players = list()

    def add_player(self, session_id):
        """ Adds a player by its session ID to the players list. """
        self.players.append(player.Player(session_id))

    def remove_player(self, session_id):
        """ Removes a player from the list. Since the list holds players
            instances, the session ID of each instance must be checked.
            If match, the index if the instance is used to delete it from
            the list. """
        for index_of_player_class, player in enumerate(self.players):
            if player.sid == session_id:
                break
            else:
                index_of_player_class = -1
        del self.players[index_of_player_class]

    def list_players(self):
        """ Can be removed after finishing. """
        print(self.players)

    def check_if_player_exists(self, session_id):
        """ Check if player has been added or not deleted before. """
        if session_id in [player.sid for player in self.players]:
            return True
        else:
            return False
