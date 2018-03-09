


class Session:
    def __init__(self):
        self.players = list()

    def check_if_sid_is_free(self, SID):
        if SID in [x[0] for x in self.players]:
            print("MODEL: Already taken.")
            return False
        else:
            print("MODEL: Can be added.")
            return True

    def add_player(self, SID, player_name):
        if self.check_if_sid_is_free(SID):
            self.players.append((SID, player_name))
            print("MODEL: Player added to Session.")
            print("MODEL:", self.players)



class Player:
    def __init__(self):
        self.name = str()
