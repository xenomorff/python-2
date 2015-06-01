"""A simple player class with random stat gen"""

# player:
# Orc:


import colors as c
from dice import roll
import random
import time

class HasStats():
    def set_stats(self):
        self.strength = roll('3,6')
        self.speed = roll('3,6')
        self.speech = roll('3,6')
        self.wisdom = roll('3,6')

    def show_stats(self):
        print(c.red)
        text = '''
        Strength: {s.strength:>2} 
        Speed: {s.speed:>2}
        Speech: {s.speech:>2}
        Wisdom: {s.wisdom:>2}
        '''
        print(text.format(s=self))

class Player(HasStats):
    def __init__(self):
        self.set_stats()
        
class Warrior(HasStats):
    def __init__(self):
        self.set_stats()
        self.strength += 5

class Archer():
    def __init__(self):
        self.set_stats()
        self.speed += 5

        
if __name__ == '__main__':
   # for count in range(10):
    while True:
        time.sleep(.5)
        print(c.clear)
        player = Player()
        player.show_stats()


