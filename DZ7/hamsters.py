from random import randint

class Hamster:
    def __init__(self, hid, map_width, map_heigth):
       self.id = hid
       self.health = randint(1, 4)
       self.position = [randint(0, map_width - 1), randint(0, map_heigth - 1)]