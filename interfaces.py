"""Interfaces"""
# TODO CHANGE SPEECH
# player:
# Orc:


import colors as c
from dice import roll
import random
import time
import json
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


#    def save(self):
 #       with open('player.json', 'w') as pfile:
  #          pfile.write(json.dumps({
   #         "strength": self.strength,
    #        "speed": self.speed,
     #       "speech"
      #      "wisdom"
       #     }))

#    def load(self):
 #       with open('player.json', 'r') as pfile:
  #          j = json.load(pfile)
   #         self.strength = j['strength']
    #        self.speed = j ['speed']
     #       self.speech = j ['speech']
      #      self.wisdom = j ['wisdom']

