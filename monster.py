" hello "

from interfaces import HasStats

monsters = ['Shrek','Donkey']


class Shrek(HasStats):
    def __init__(self):
        self.set_stats()
        self.strength += 5

class Donkey(HasStats):
    def __init__(self):
        self.set_stats()
        self.speed += 5



if __name__ ==' __main__':
    while True:
        monster = Monster()
        monster.show_stats()
    
