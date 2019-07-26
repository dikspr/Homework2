from random import randint, choice

class Hamster:
    def __init__(self, hid, map):
        self.id = hid
        self.health = 2 # randint(1, 4)
        self.position = self.get_clear_position(map)

    def get_clear_position(self, map):
        map_width = len(map.split('\n')[0])
        map_heigth = len(map.split('\n'))
        while True:
            coords = [randint(0, map_width-1), randint(0, map_heigth - 1)]
            if map.split('\n')[coords[1]] [coords[0]] == '*':
                return coords

    def on_shot(self):
        self.health -=1
        return self.health == 0

