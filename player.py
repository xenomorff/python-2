"""A simple player class with random stat gen"""

# player:
# Orc:


from interfaces import HasStats
import time 
import colors as c

class Player(HasStats):
    def __init__(self):
        self.set_stats()
        
            
if __name__ == '__main__':
   # for count in range(10):
    while True:
        time.sleep(.5)
        print(c.clear)
        player = Player()
        # player.save()
        player.load()
        player.show_stats()

