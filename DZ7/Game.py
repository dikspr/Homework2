from player import Player
from hamsters import Hamster

hamsters_count = 4


class Game:
    map = '****\n****\n****\n****'
    gameon = True
    happy_message = 'WOW!!!! You won!'
    hamsters_count_now = hamsters_count

    def __init__(self):
        self.player = Player()
        self.hamsters = []
        for i in range(hamsters_count):
            self.hamsters.append(Hamster(i+1, self.get_full_map()))


    def add_point(self, position, name, s):
        li = s.split('\n')
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0] + 1:]
        li[position[1]] = row
        return '\n'.join(li)

    def render_map(self):
        s = self.map
        s = self.add_point(self.player.position, 'x', s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)

        print(s)


    def move_player(self, destination):
        """ destination = w,a,s,d """
        if destination == 's':
            if self.player.position[1] == len(self.map.split('\n')) - 1:
                return False
            self.player.position[1] += 1  # bottom
        if destination == 'w':
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1  # top
        if destination == 'a':
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1  # left
        if destination == 'd':
            if self.player.position[0] == len(self.map.split('\n')[0]) - 1:
                return False
            self.player.position[0] += 1  # right
        self.on_move(destination)

    def get_full_map(self):
        s = self.map
        for h in self.hamsters:
            s = self.add_point(h.position, str(h.id), s)
        return s

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()

        return s.split('\n')[coords[1]][coords[0]]

    directions = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}
    def on_move(self, direction):
        hamster = self.get_hamster_on_position(self.player.position)
        if not hamster == '*':
            self.player.was_hit(int(hamster))
            if self.player.health <= 0:
                self.gameon = False
                print('Game over... Sorry!')
                return False
            print("Player's health: ", self.player.health)
            killed = self.hamsters[int(hamster) - 1].on_shot()
            if not killed:
                print('wasnt killed')
                self.move_player(self.directions[direction])
            else:
                print(self.hamsters[int(hamster) - 1].id, 'was killed')
                self.hamsters_count_now -= 1

    def start(self):
        game.render_map()
        while self.gameon:
            # print(self.hamsters_count_now)
            if self.hamsters_count_now == 0:
                print(self.happy_message)
                self.gameon = False
            command = input('Insert command: ')
            if command in ['a', 's', 'd', 'w']:
                self.move_player(command)
                self.render_map()
            if command == 'e':
                self.player.wait()
            if command == 'q':
                self.gameon = False


game = Game()
game.start()

# 2. Нормальную обработку границ карты мы сделали, когда делали метод перемещения по карте. Ошибки нет.
# 3. Для исправления ошибки с концовкой в классе Game ввел свойство hamsters_count_now,
# которое показывает текущее количество хомяков.
# В методе on_move, когда хомяк умирает, это свойство уменьшается на 1.
# В методе start в начале цикла проверяем не количество хомяков в списке hamsters, которое у нас в игре не меняется,
# а свойство hamsters_count_now.