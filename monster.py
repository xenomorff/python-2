" hello "

from dice import roll

class Monster():
    health = 100
    def __init__(self):
        self.attack = roll('3,6')
        self.speed = roll('3,6')
    
    def show_stats(self):
        text = '''
        attack:     {s.attack}
        speed:      {s.speed}
        '''
        print(text.format(s=self))

if __name__ ==' __main__':    
    monster = Monster()
    monster.show_stats()
    
