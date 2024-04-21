"""This is a digital implementation of an Asterix gamebook."""

from hero import Hero
import random
import tkinter as tk # Used to create a GUI

# Create Window
window = tk.Tk()
window.geometry("400x300")
window.title("Give me a name!")


def roll_hero():
    """Rolls the stats for a hero. Each stat has a base of 10. 
    There are then 15 points to distribute between the stats"""
    fighting_fitness = random.randint(0, 15)
    skill = random.randint(0, (15 - fighting_fitness))
    charm = (15 - fighting_fitness - skill)
    return Hero(
        fighting_fitness=fighting_fitness+10,
        skill=skill+10,
        charm=charm+10)

# Create Asterix with random properties
asterix = roll_hero()
print(f'Asterix stats are FF:{asterix.fighting_fitness} Skill:{asterix.skill} Charm:{asterix.charm}')