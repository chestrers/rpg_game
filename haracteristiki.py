



strength = 0
agility = 0
intelligence = 0
attack = 5+strength
defence = 0+agility
hp = 0 + strength*4
mana = 0*intelligence*4
lvl = 1
experience = 0
exp2 = 50

if experience >= exp2:
    lvl += 1
    experience *= 1.7
    strength += 4
    agility += 4
    intelligence += 4



