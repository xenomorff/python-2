""" Game Engine """
import colors as c
from player import Player 
import player

class Game():
     
    def __init__(self):
        self.player = Player()
        #TODO MONSTER
        print('Your stats are')

    def run(self):

       while True:
            self.player.show_stats()
            # TODO SHOW MONSTER STATS
            action = input('What do you want to do? ')
            
if __name__ == '__main__':
    agame = Game()
    agame.run()
