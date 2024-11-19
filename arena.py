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