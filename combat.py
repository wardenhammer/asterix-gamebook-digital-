import random


class Hero:
    def __init__(self, fightingfitness, charm, skill):
        self.fightingfitness = fightingfitness
        self.charm = charm
        self.skill = skill

class Enemy:
    def __init__(self, fightingfitness):
        self.fightingfitness = fightingfitness

asterix = Hero(15,15,15)
legionaire = Enemy(12)

# Start combat
diceRoll = random.randint(1, 6)
print(f"dice={diceRoll}")
legionaire.fightingfitness = legionaire.fightingfitness - diceRoll
print(vars(asterix))
print(vars(legionaire))