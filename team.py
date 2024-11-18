from hero import Hero
from ability import Ability
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        '''Add a hero to the team.'''
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill/Deaths: {kd}')

    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # create lists of living heroes from both teams
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        # Fight loop until one of the teams has no living heroes
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # Randomly select a living hero from each team
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            # Have the heroes fight each other
            hero.fight(opponent)

            # Update the lists of living heroes and opponents
            if not hero.is_alive():
                living_heroes.remove(hero)
                
            if not opponent.is_alive():
                living_opponents.remove(opponent)

        # Annouce the winner
        if living_heroes:
            print(f'{self.name} wins the battle!')
        else:
            print(f'{other_team.name} wins the battle!')


if __name__ == '__main__':

    # Create Heroes
    hero1 = Hero("Batman", 200)
    hero2 = Hero("Superman", 250)
    opponent1 = Hero("Joker", 150)
    opponent2 = Hero("Lex Luthor", 180)

    # Create Teams
    team1 = Team("Justice League")
    team2 = Team("Legion of Doom")

    # Add heroes to teams
    team1.add_hero(hero1)
    team1.add_hero(hero2)
    team2.add_hero(opponent1)
    team2.add_hero(opponent2)

    # Add abilities to heroes
    ability1 = Ability('Super Speed', 400)
    ability2 = Ability('Super Eyes', 110)
    ability3 = Ability('Wizard Wand', 60)
    ability4 = Ability('Wizard', 10)

    hero1.add_ability(ability1)
    hero2.add_ability(ability2)
    opponent1.add_ability(ability3)
    opponent2.add_ability(ability4)

    # Battle the teams
    team1.attack(team2)