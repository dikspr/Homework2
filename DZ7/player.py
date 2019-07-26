import random
class Player:
    health = 10
    position = [0,0]
    def was_hit(self, hid):
        self.health -= random.choice(range(hid+1))