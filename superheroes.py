#!/usr/bin/env python3
# superheroes program for CS-1-1

# SPAGHETTI CODE TO THE MAXXXXXX

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
        # It should also call add_kill on each hero with the number of
        # opponents killed
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
            ratio = "N/A"
            if hero.deaths > 0:
                ratio = str(hero.kills / hero.deaths)
            print(hero.name + " - Kills: " + str(hero.kills) +
                  "\t Deaths: " + str(hero.deaths) + "\t Ratio: " + ratio)

    def update_kills(self):
        # This method should update each hero when there is a team kill.
        return


class Arena:

    def __init__(self):
        # declare variables
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        # call the method
        self.build_a_team("One")

    def build_team_two(self):
        # call the method
        self.build_a_team("Two")

    def build_a_team(self, selector):
        # ask the questions
        print("What would you like to name Team " + selector + "?")
        team_name = input()
        constructed_team = Team(team_name)
        print("How many heroes are on Team " + selector + "?")
        cardinal = int(input())
        for index in range(1, cardinal + 1):
            print("What is the name of hero #" + str(index) + "?")
            hero_name = input()
            new_hero = Hero(hero_name)
            print("Great. How many abilities does " + new_hero.name + " have?")
            num_abilities = int(input())
            for subindex1 in range(1, num_abilities + 1):
                print("Ok. What is the name of ability #" + str(subindex1) + "?")
                ability_name = input()
                print("And how much power does it have?")
                ability_power = int(input())
                new_ability = Ability(ability_name, ability_power)
                new_hero.add_ability(new_ability)
                print("Got it. Added " + new_ability.name + " with a power of " +
                      str(new_ability.attack_strength) + " to " + new_hero.name + ".")
            print("Now, how many weapons does " + new_hero.name + " have?")
            num_weapons = int(input())
            for subindex2 in range(1, num_weapons + 1):
                print("Ok. What is the name of weapon #" + str(subindex2) + "?")
                weapon_name = input()
                print("And how much power does this weapon have?")
                weapon_power = int(input())
                new_ability = Ability(weapon_name, weapon_power)
                new_hero.add_ability(new_ability)
                print("Got it. Added a " + new_ability.name + " with a power of " +
                      str(new_ability.attack_strength) + " to " + new_hero.name + ".")
            print("And defense - how many armor pieces does " +
                  new_hero.name + " have?")
            num_armors = int(input())
            for subindex3 in range(1, num_armors + 1):
                print("Ok. What is the name of armor piece #" +
                      str(subindex3) + "?")
                armor_name = input()
                print("And how much defense does this armor have?")
                armor_defense = int(input())
                new_armor = Armor(armor_name, armor_defense)
                new_hero.add_armor(new_armor)
                print("Got it. Added a " + new_armor.name + " with a defense of " +
                      str(new_armor.defense) + " to " + new_hero.name + ".")
            constructed_team.add_hero(new_hero)
        print()

        # save the team
        if selector == "One":
            self.team_one = constructed_team
        elif selector == "Two":
            self.team_two = constructed_team

        # print the pretty table
        team_name_padding_len = 72 - len(constructed_team.name)
        team_name_padding = ""
        for h in range(0, team_name_padding_len):
            team_name_padding += " "
        summary_name_spaces = 25
        summary_power_spaces = 39
        summary_value_spaces = 25
        print("|-------------------------------------------------------------------------------------------|")
        print("| Team " + selector + " Summary: " +
              constructed_team.name + team_name_padding + "|")
        print("| Name                      Powers & Equipment                      Attack or Defense Value |")
        print("|-------------------------|---------------------------------------|-------------------------|")
        for hero in constructed_team.heroes:
            hero_name_line = True
            for ability in hero.abilities:
                ability_name = ability.name
                ability_power = str(ability.attack_strength)
                name_padding = ""
                name_padding_len = summary_name_spaces
                power_padding = ""
                power_padding_len = summary_power_spaces - \
                    len(ability_name) - 1
                value_padding = ""
                value_padding_len = summary_value_spaces - \
                    len(ability_power) - 1
                for i in range(0, name_padding_len):
                    name_padding += " "
                for j in range(0, power_padding_len):
                    power_padding += " "
                for k in range(0, value_padding_len):
                    value_padding += " "
                if hero_name_line:
                    name_padding = ""
                    name_padding_len = summary_name_spaces - len(hero.name) - 1
                    for i in range(0, name_padding_len):
                        name_padding += " "
                    print("| " + hero.name + name_padding + "| " + ability_name +
                          power_padding + "| " + ability_power + value_padding + "|")
                    hero_name_line = False
                else:
                    print("|" + name_padding + "| " + ability_name + power_padding +
                          "| " + ability_power + value_padding + "|")
            for armor in hero.armors:
                armor_name = armor.name
                armor_defense = str(armor.defense)
                name_padding = ""
                name_padding_len = summary_name_spaces
                power_padding = ""
                power_padding_len = summary_power_spaces - \
                    len(armor_name) - 1
                value_padding = ""
                value_padding_len = summary_value_spaces - \
                    len(armor_defense) - 1
                for i in range(0, name_padding_len):
                    name_padding += " "
                for j in range(0, power_padding_len):
                    power_padding += " "
                for k in range(0, value_padding_len):
                    value_padding += " "
                if hero_name_line:
                    print("| " + hero.name + name_padding + "| " + armor_name +
                          power_padding + "| " + armor_defense + value_padding + "|")
                    hero_name_line = False
                else:
                    print("|" + name_padding + "| " + armor_name + power_padding +
                          "| " + armor_defense + value_padding + "|")
            print(
                "|-------------------------|---------------------------------------|-------------------------|")
        print()

    def team_battle(self):
        if self.team_one == None or self.team_two == None:
            print("You need two teams to battle, ya ding dong!")
            return
        else:
            still_alive = True
            battle_round_cardinal_number = 1
            while still_alive:
                still_alive = False
                print("Round " + str(battle_round_cardinal_number) + ". Fight!")
                self.team_one.attack(self.team_two)
                self.team_two.attack(self.team_one)
                for hero in self.team_one.heroes:
                    if hero.health > 0:
                        still_alive = True
                if still_alive:
                    still_alive = False
                    for hero in self.team_two.heroes:
                        if hero.health > 0:
                            still_alive = True
                battle_round_cardinal_number += 1
            print("The match is over!")
            print()

    def show_stats(self):
        print("Team One:")
        self.team_one.stats()
        print("Team Two:")
        self.team_two.stats()

if __name__ == "__main__":

    # If you run this file from the terminal this block is executed.
    # for x in xrange(1,10):
    # 	hero = Hero("Diana")
    # 	pass

    # Basic testing
    # hero = Hero("Wonder Woman")
    # print(hero.attack())
    # ability = Ability("Divine Speed", 300)
    # hero.add_ability(ability)
    # print(hero.attack())
    # new_ability = Ability("Super Human Strength", 800)
    # hero.add_ability(new_ability)
    # print(hero.attack())

    # Arena testing
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
