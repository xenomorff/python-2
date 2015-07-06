""" Game Engine """

import colors as c
from player import Player 
import monster as m
import time
import random

class Game():
     
    def __init__(self):
        self.player = Player()
        self.player.load()

    def run(self):
        self.player.show_stats()
        while True:
           # self.player.show_stats()
            # TODO SHOW MONSTER STATS
            action = input(c.violet+'What do you want to do? '+c.base3+'>>> ')
            print(c.clear)
            print(c.reset)
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
            elif action in ['fight','battle']:
                self.handle_battle

    def pick(self):
        count = 1
        for monster in m.monsters:
            print((c.base3+ "{}. "+c.green+"{}" +c.reset).format(count, monster.title))
            count += 1
        print(c.red+'PICK: 1 , 2')
        print(c.reset)
        number = int(input().strip().lower())
        monster_class = m.monsters[number -1]
        monster = monster_class()
        print(c.red + "You picked {}:".format(monster.title))
        monster.show_stats()
    
        
    def handle_battle(self):
        # who goes first
        # attack defend pass

    def save(self):
        self.player.save()

            
    


if __name__ == '__main__':
    agame = Game()
    agame.run()


