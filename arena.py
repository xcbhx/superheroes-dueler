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
    

    def create_hero(self):
        '''Prompt user for Hero information
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name) # Create the hero object

        add_item = None
        while add_item != '4': #Keep looping until the user chooses 'Done'
            add_item = input('[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding item\n\nYour choice: ')
            if add_item == '1':
                # Add an ability to the hero
                ability = self.create_ability()
                hero.add_ability(ability)
                print(f'Added ability: {ability.name}')
            elif add_item == "2":
                # Add a weapon to the hero
                weapon = self.create_weapon()
                hero.add_ability(weapon)
                print(f'Added weapon: {weapon.name}')
            elif add_item == "3":
                # Add an armor to the hero
                armor = self.create_armor()
                hero.add_ability(armor)
                print(f'Added armor: {armor.name}')
            elif add_item == '4':
                print(f'Finished cerating hero: {hero.name}')
            else:
                print('Invalid choice. Please try again.')
        return hero
    

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # Prompt for the number of team members
        num_of_team_members = int(input('How many members would you like on Team Two?\n'))
        # Create each hero and add them to team_two
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)