import random
# Import my own classes
from hero import Hero
from enemy import Enemy

asterix = Hero(15,15,15)
legionaire = Enemy(12)

# Start combat
while(asterix.fightingfitness > 0 and legionaire.fightingfitness > 0):
    print("Asterix hits the Legionire...")
    diceRoll = random.randint(1, 6)
    print(f"dice={diceRoll}")
    legionaire.fightingfitness = legionaire.fightingfitness - diceRoll
    print(vars(asterix))
    print(vars(legionaire))
    print("Legionire hits Asterix")
    diceRoll = random.randint(1, 6)
    print(f"dice={diceRoll}")
    asterix.fightingfitness = asterix.fightingfitness - diceRoll
    print(vars(asterix))
    print(vars(legionaire))