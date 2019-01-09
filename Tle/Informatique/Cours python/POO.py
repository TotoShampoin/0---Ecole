class Player:
    def __init__(self):
        self.name = ""
        self.HP = 20
        self.MP = 0
        self.health = "Good"
    def _get_health(self):
        return self.health
    def _set_health(self, newVal):
        self.health = newVal
    
class Witch(Player):
    def __init__(self):
        self.MP = 20
    
