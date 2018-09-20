import random

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Return attack value
        attackValue = random.randint(attack_strength // 2, attack_strength)
        return attackValue

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength


class Hero:
    def __init__(self, name):
        # Initialize starting values
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        


if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
