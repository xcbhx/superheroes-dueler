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
                print(f'Finished creating hero: {hero.name}')
            else:
                print('Invalid choice. Please try again.')
        return hero
    

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_name = input('Enter the name of Team One: ')
        self.team_one = Team(team_name) # Initialize team_one with a name
        num_of_team_members = int(input('How many members would you like on Team One?\n'))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        team_name = input('Enter the name of Team Two: ')
        self.team_two = Team(team_name) # Initialize team_two with a name
        # Prompt for the number of team members
        num_of_team_members = int(input('How many members would you like on Team Two?\n'))
        # Create each hero and add them to team_two
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # Ensure both teams exist
        if not self.team_one or not self.team_two:
            print('Both teams need to be created before a battle can occur.')
            return
        
        print(f'{self.team_one.name} and {self.team_two.name} are battling!')
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print('\n')
        print(f'{self.team_one.name} statistics:')
        self.team_one.stats()
        print('\n')
        print(f'{self.team_two.name} statistics:')
        self.team_two.stats()
        print('\n')

        # Calculate average K/D for Team One
        team_one_kills = 0
        team_one_deaths = 0
        for hero in self.team_one.heroes:
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths
        if team_one_deaths == 0:
            team_one_deaths = 1  # Avoid division by zero
        print(f'{self.team_one.name} average K/D was: {team_one_kills / team_one_deaths:.2f}')

        # Calculate average K/D for Team Two
        team_two_kills = 0
        team_two_deaths = 0
        for hero in self.team_two.heroes:
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        if team_two_deaths == 0:
            team_two_deaths = 1  # Avoid division by zero
        print(f'{self.team_two.name} average K/D was: {team_two_kills / team_two_deaths:.2f}')

        print('\nSurviving heroes:')
        # List surviving heroes from Team One
        print(f'Survivors from {self.team_one.name}:')
        team_one_survivors = [hero.name for hero in self.team_one.heroes if hero.is_alive()]
        if team_one_survivors:
            print(', '.join(team_one_survivors))
        else:
            print('No survivors')

        # List surviving heroes from Team Two
        print(f'Survivors from {self.team_two.name}:')
        team_two_survivors = [hero.name for hero in self.team_two.heroes if hero.is_alive()]
        if team_two_survivors:
            print(', '.join(team_two_survivors))
        else:
            print('No survivors')

        # Declare the winning team
        if len(team_one_survivors) > len(team_two_survivors):
            print(f'\n{self.team_one.name} wins!')
        elif len(team_two_survivors) > len(team_one_survivors):
            print(f'\n{self.team_two.name} wins!')
        else:
            print("\nIt's a tie!")


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input('Play Again? Y or N: ')

        #Check for Player Input
        if play_again.lower() == 'n':
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()