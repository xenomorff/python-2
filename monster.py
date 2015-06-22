" hello "

from interfaces import HasStats
import random
monsters = ['Shrek','Donkey']


class Shrek(HasStats):
    def __init__(self):
        self.set_stats()
        self.strength += 5
        self.title = self.__class__.__name__
class Donkey(HasStats):
    def __init__(self):
        self.set_stats()
        self.speed += 5
        self.title = self.__class__.__name__

monsters = ['Shrek','Donkey']


if __name__ ==' __main__':
    one_Shrek = Shrek()
    one_Shrek.show_stats

