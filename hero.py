from ability import Ability
from armor import Armor

import random

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        # abilities nad armors don't have starting values,
        # and are set to empty lists on initialization 
        self.abilities = list()
        self.armors = list()
        # We know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health


    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        #1) randomly choose winner,
        # Hint: Look into random library, more specifically the choice method
        winner = random.choice([self, opponent])
        loser = self if winner == opponent else opponent
        print(f'{winner.name} defeats {loser.name}!')

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        # we use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            # return the total damage 
        return total_damage
        
    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        if self.current_health <= 0:
            return 0 # Hero is dead, no defense
        
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.block()
        return total_defense






if __name__ == '__main__':

    # Instantiate two heros 
    hero1 = Hero('Wonder Woman', 150)
    hero2 = Hero('Dumbledore', 180)

    # Trigger a fight between the two heroes
    print('\n=== Hero Fight ===')
    hero1.fight(hero2)

    ability = Ability('Great Debugging', 50)
    armor = Armor('Great Debugging', 20)
    another_ability = Ability('Smarty Pants', 90)
    another_armor = Armor('Fight', 30)

    hero = Hero('Grace Hopper', 200)

    hero.add_ability(ability)
    hero.add_armor(armor)
    hero.add_ability(another_ability)
    hero.add_armor(another_armor)

    # Test attack and defend
    print('\n=== Hero Stats ===')
    print('Attack Damage:', hero.attack())
    print('Total Defense:', hero.defend())