" hello "

from interfaces import HasStats
import random


class Shrek(HasStats):
    title = "The God Of All Gods"
    def __init__(self):
        self.set_stats()
        self.strength += 5
       

class Donkey(HasStats):
    title = "The Prince Of All Princes"
    def __init__(self):
        self.set_stats()
        self.speed += 5
        

monsters = [Shrek,
            Donkey
]

if __name__ ==' __main__': 
    one_Shrek = Shrek()
    one_Shrek.show_stats
    one_Shrek.title

