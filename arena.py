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