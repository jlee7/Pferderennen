""" This file contains the player class """

class Player:
    def __init__(self, session_id):
        self.sid = session_id
        self.name = None
        self.wins = None
        self.highscore = None
