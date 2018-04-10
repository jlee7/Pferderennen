""" This file contains the player class """

class Player:
    def __init__(self, session_id, name):
        self.sid = session_id
        self.name = name
        self.wins = None
        self.highscore = None

        print("PLAYER:", self.name)
