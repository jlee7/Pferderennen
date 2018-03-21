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

        # Check if self.player is empty already
        if len(self.players) > 0:
            # Get index to remove by index from list
            for index_of_player_class, player in enumerate(self.players):
                print("SESSION: remove_player: IF", index_of_player_class, player)
                # Match session_id with the session ID from each player in list
                if player.sid == session_id:
                    index_of_player_class = self.players.index(player)
                    print(index_of_player_class)
                    #del self.players[index_of_player_class]
                else:
                    print("SESSION: remove_player: ELSE", index_of_player_class)
                    index_of_player_class = -1
                    print(index_of_player_class)

                # Delete the player by index
                del self.players[index_of_player_class]
        else:
            print("List of players is empty.")

    def list_players(self):
        """ Can be removed after finishing. """
        print(self.players)

    def check_if_player_exists(self, session_id):
        """ Check if player has been added or not deleted before. """
        if session_id in [player.sid for player in self.players]:
            return True
        else:
            return False
