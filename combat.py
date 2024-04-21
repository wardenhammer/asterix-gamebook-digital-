import random
# Import my own classes
from hero import Hero
from enemy import Enemy

asterix = Hero(fighting_fitness=15,charm=15,skill=15)
legionaire = Enemy(fighting_fitness=12)

# Start combat
while(asterix.fighting_fitness > 0 and legionaire.fighting_fitness > 0):
    print("Asterix hits the Legionire...")
    diceRoll = random.randint(1, 6)
    print(f"dice={diceRoll}")
    legionaire.fighting_fitness = legionaire.fighting_fitness - diceRoll
    print(vars(asterix))
    print(vars(legionaire))
    print("Legionire hits Asterix")
    diceRoll = random.randint(1, 6)
    print(f"dice={diceRoll}")
    asterix.fighting_fitness = asterix.fighting_fitness - diceRoll
    print(vars(asterix))
    print(vars(legionaire))