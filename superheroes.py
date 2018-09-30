#!/usr/bin/env python3
# superheroes program for CS-1-1
# just testing if wakatime works for sublime text
import random


class Ability:

    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Return attack value
        attackValue = random.randint(
            self.attack_strength // 2, self.attack_strength)
        if attackValue == None:
            attackValue = 0
        return attackValue

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength


class Weapon(Ability):

    def attack(self):
            # Return a weapon attack value, between 0 and full attack.
        attackValue = random.randint(0, self.attack_strength)
        if attackValue == None:
            attackValue = 0
        return attackValue


class Armor:

    def __init__(self, name, defense):
        # Initialize starting values
        self.name = name
        self.defense = defense

    def defend(self):
        # Return a random value between 0 and the initialized defense strength.
        defenseValue = random.randint(0, self.defense)
        if defenseValue == None:
            defenseValue = 0
        return defenseValue


class Hero:

    def __init__(self, name, health=100):
        # Initialize starting values
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        # Run attack() on every ability hero has
        if len(self.abilities) > 0:
            for ability in self.abilities:
                return ability.attack()
        else:
            return 0

    def defend(self):
        # Run defend on each piece of armor and calculate total defense
        # If the hero's health is 0, the hero is out of play and this method
        # should return 0 defense points.
        if self.health == 0:
            return 0
        defense = 0
        for armor in self.armors:
            defense += armor.defend()
        return defense

    def take_damage(self, damage_amt):
        # This method should subtract the damage amount from the hero's health.
        # If the hero dies, update the number of deaths.
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills
        self.kills += num_kills


class Team:

    def __init__(self, team_name):
        # Initialize starting values
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        # Add a Hero to the heroes list
        self.heroes.append(Hero)

    def remove_hero(self, name):
        # Remove hero from the heroes list.
        # If the hero isn't found, return 0.
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        return 0

    def find_hero(self, name):
        # Find and return hero from heroes list.
        # If Hero is not found, return 0
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        # Print out all heroes to the console
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        # This method should calculate our team's total attack strength and call the defend() method on the opposing team
        # It should also call add_kill on each hero with the number of kills
        # made
        totalAttack = 0
        for hero in self.heroes:
            totalAttack += hero.attack()
        opponentsKilled = other_team.defend(totalAttack)
        for hero in self.heroes:
            hero.add_kill(opponentsKilled)

    def defend(self, damage_amt):
        # This method should calculate our team's total defense.
        # Any damage in excess of our team's total defense should be distributed evenly among our heroes using deal_damage().
        # Return number of heroes killed in the attack.
        totalDefense = 0
        for hero in self.heroes:
            totalDefense += hero.defend()
        damage = damage_amt - totalDefense
        heroesKilled = self.deal_damage(damage)
        return heroesKilled

    def deal_damage(self, damage):
        # Divide the total damage among all heroes. Return number of heroes
        # that died during the attack.
        deadHeroes = 0
        individualDamage = damage / len(self.heroes)
        for hero in self.heroes:
            hero.take_damage(individualDamage)
            deadHeroes += hero.deaths
        return deadHeroes

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        # This method should print a K/D ratio for each hero
        for hero in self.heroes:
            ratio = hero.kills / hero.deaths
            print("K/D ratio for " + hero.name + ": " + ratio)

    def update_kills(self):
        # This method should update each hero when there is a team kill.
        return


if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
    # for x in xrange(1,10):
    # 	hero = Hero("Diana")
    # 	pass
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
