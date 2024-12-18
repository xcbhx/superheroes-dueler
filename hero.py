from ability import Ability
from armor import Armor
from weapon import Weapon

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
        self.deaths = 0
        self.kills = 0 


    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''
        # Fight each hero until a victor emerges.
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if not self.abilities and not opponent.abilities:
            print('Draw')
            return
        else:
         # 1) else, start the fighting loop until a hero has won
            while self.is_alive() and opponent.is_alive():
            # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
                opponent_damage = self.attack()
                opponent.take_damage(opponent_damage)
            # 3) After each attack, check if either the hero (self) or the opponent is alive
                if not opponent.is_alive():
                    print(f'{self.name} won!')
                    # Update statistics (helper method)
                    self.add_kill(1)
                    opponent.add_death(1)
                    return
                
                # Opponent attacks the hero
                self_damage = opponent.attack()
                self.take_damage(self_damage)

            # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
                if not self.is_alive():
                    print(f'{opponent.name} won!')
                    # Update statistics
                    opponent.add_kill(1)
                    self.add_death(1)
                    return
            


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
        if not self.is_alive():
            return 0
        return sum(armor.block() for armor in self.armors)
    
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the denfense.'''
        # Calculate the defense
        defense = self.defend()
        # Subtract the defense from the incoming damage
        damage_to_take = max(0, damage - defense) # ensure no negative damage
        # Update the hero's health
        self.current_health -= damage_to_take

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else:
            return True
        
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills
        
    def add_death(self, num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths



if __name__ == '__main__':

    # Instantiate Hero and Weapon
    hero = Hero('Wonder Woman')
    weapon = Weapon('Lasso of Truth', 90)

    # Instantiate more heores for fight testing
    hero1 = Hero('Wonder Woman')
    hero2 = Hero('Dumbledore')


    # Create abilities and armor
    # ability = Ability('Great Debugging', 50)
    # armor = Armor('Great Debugging', 20)
    # another_ability = Ability('Smarty Pants', 90)
    # another_armor = Armor('Fight', 30)
    ability1 = Ability('Super Speed', 300)
    ability2 = Ability('Super Eyes', 130)
    ability3 = Ability('Wizard Wand', 80)
    ability4 = Ability('Wizard', 20)

    # Create another hero and add abilities/armor
    # hero = Hero('Grace Hopper', 200)
    # shield = Armor('Shield', 50)

    # Add abilities to heroes
    # hero.add_ability(ability)
    # hero.add_armor(armor)
    # hero.add_ability(another_ability)
    # hero.add_armor(another_armor)
    # hero.add_armor(shield)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    # Add weapon to the hero
    hero.add_weapon(weapon)
    print(f'Weapon Attack Damage: {hero.attack()}')

    # Test damage and is_alive
    # print('\n=== Testing Damage and Health ===')
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    # Trigger a fight between the two heroes
    print('\n=== Hero Fight ===')
    hero1.fight(hero2)

    # Test attack and defend
    # print('\n=== Hero Stats ===')
    # print('Attack Damage:', hero.attack())
    # print('Total Defense:', hero.defend())
    # print(f'Current Health: {hero.current_health}')
