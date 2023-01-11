#!/usr/bin/python3
monster_life = 10
Hero_life = 10
Hero_STR = 0
#Importing Random Number for Hero STR
import random
monstera = random.randrange(5)
#Start Loop for Game
print('hi')
while monster_life > 0 | Hero_life > 0:
    print("You are Fighting the Dragon" , monster_life,"You are the Hero",Hero_life)
    Hero_STR=random.randrange(5)
    monster_life=monster_life-Hero_STR
    print("Moster Life Left",monster_life)
    Hero_life=Hero_life-monstera
    print("Hero Life left :", Hero_life)
