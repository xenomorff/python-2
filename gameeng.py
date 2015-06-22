""" Game Engine """

import colors as c
from player import Player 
import monster as m
import time
import random

class Game():
     
    def __init__(self):
        self.player = Player()
        #TODO MONSTER

    def run(self):
        while True:
           # self.player.show_stats()
            # TODO SHOW MONSTER STATS
            action = input('What do you want to do? >>> ')
            print(c.clear)
            if action == 'stats':
                self.player.show_stats()
            elif action == 'save':
                self.save()
            elif action == 'exit':
                print(c.orange+'Bye')
                time.sleep(.5)
                exit()
            elif action in ['pick','choose']:
                self.pick()

    def pick(self):
        count = 1
        for monster in m.monsters:
            print((c.base3+ "{}. "+c.green+"{}" +c.reset).format(count, monster))
            count += 1
        print('1,2')
        number = int(input().strip().lower())
        monster_name = m.monsters[number -1]
        print("You have chosen", monster_name)

    def save(self):
        print('Did not save')

    


if __name__ == '__main__':
    agame = Game()
    agame.run()

