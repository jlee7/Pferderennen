""" This file contains the player class """

class Player:
    def __init__(self, session_id, is_host, name):
        self.sid = session_id
        self.name = name
        self.is_host = is_host
        self.wins = None
        self.highscore = None

        if self.is_host == True:
            print(self.name, "is the host.")
