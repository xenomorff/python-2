"""A simple player class with random stat gen"""

import colors as c
from dice import roll
import random
import time

class Player():
    def __init__(self):
        self.strength = roll('3,6')
        self.vitality = roll('3,6')
        self.speed = roll('3,6')
        self.speech = roll('3,6')
        self.wisdom = roll('3,6')
    
    def show_stats(self):
        text = '''
        Strength: {s.strength:>2}
        Vitality: {s.vitality:>2}
        Speed: {s.speed:>2}
        Speech: {s.speech:>2}
        Wisdom: {s.wisdom:>2}
        '''
        print(text.format(s=self))
        
        
if __name__ == '__main__':
    for count in range(5):
        time.sleep(1)
        print(c.clear)
        player = Player()
        player.show_stats()



