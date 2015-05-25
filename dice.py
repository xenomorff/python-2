"""
rolling
"""
import random
import colors as c


def rolldie(sides=6):
    return random.randint(1,sides)

def roll(number=1,sides=6):
    total = 0
    for count in range(sides):
        total += rolldie(sides)
    return total

def parse(text):
    (howmany, sides) = text.split('d')
    return (int(howmany), int(sides)) 

def parse_roll(text):
    (howmany, sides) = parse(text)
    return roll(howmany, sides)

if __name__ =='__main__':
   # print(parse_roll('2d6'))
   # exit()
    for count in range(2):  
        hi = rolldie(6)
        print(c.red +'++roll die++')
        print(hi)
        print(c.orange+'------')
        bye = roll(3,6)
        print(c.blue+'<<roll>>')
        print(bye)
        print(c.orange+'------')

