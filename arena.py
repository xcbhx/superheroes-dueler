from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team 

class Arena:
    def __init__(self):
        '''Instantiate properties
        team_one: None
        team_two: None
        '''
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input('What is the ability name?')
        max_damage = input('What is the max damage of the ability?')

        return Ability(name, max_damage) 
    
    def create_weapon(self):
        '''Prompt user for Weapon information
        return Weapon with values from user input. 
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        weapon_name = input('Enter the name of weapon: ')
        # Prompt the user for the weapon's attack damage
        try:
            weapon_damage = int(input(f'Enter the attack damage for {weapon_name}: '))
        except ValueError:
            print("Invalid input. Attack damage must be a number. Defaulting to 10.")
        weapon_damage = 10 

        # return the new weapon object.
        return Weapon(weapon_name, weapon_damage)
    
    def create_armor(self):
        '''Prompt user for Armor information
        return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the armor's name
        armor_name = input('Enter the name of the armor: ')

        # Prompt the user for the armor's max block value
        try:
            armor_max_block = int(input(f'Enter the maximum block value for {armor_name}: '))
        except ValueError:
            print('Invalid input. Maximum block value must be a number. Defaulting to 10.')
            armor_max_block = 10
        #  return the new armor object with values set by user.
        return Armor(armor_name, armor_max_block)
    

    