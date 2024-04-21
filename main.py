"""This is a digital implementation of an Asterix gamebook."""

from hero import Hero
import random
import tkinter as tk # Used to create a GUI

# Create Window
window = tk.Tk()
window.title("Create your stats")
window.geometry("400x300")

# Create a Frame
CharacterCreationFrame = tk.Frame(window)

# Labels for the character stats
hero_f_f_label = tk.Label(CharacterCreationFrame,
                       text=f"Hero FF:0",
                       font=10)
hero_f_f_label.pack(pady=20)

# Add a Generate Hero Button
CreateHeroBtn = tk.Button(CharacterCreationFrame,
                          text="Give me a name", font=10, width=7)
CreateHeroBtn.pack(pady=50)

# Draw the character creation frame
CharacterCreationFrame.pack()


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

########
# MAIN #
########
# Display the window
window.mainloop()
# Create Asterix with random properties
asterix = roll_hero()
print(f'Asterix stats are FF:{asterix.fighting_fitness} Skill:{asterix.skill} Charm:{asterix.charm}')