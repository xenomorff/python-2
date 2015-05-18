"""
hello
"""
import random
import colors as c


def rolldie(sides=6):
    return random.randint(1,sides)

def roll(number=1,sides=6):
    total = 0
    for count in range(number):
        total += rolldie(sides)
    return total
    

if __name__ =='__main__':
    for count in range(4):    
        hi = rolldie(6)
        print('roll die')
        print(hi)
        bye = roll(3,6)
        print('roll')
        print(bye)

    



