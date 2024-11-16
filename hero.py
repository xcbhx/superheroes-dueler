import random

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
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




if __name__ == "__main__":

    # Instantiate two heros 
    hero1 = Hero('Wonder Woman', 150)
    hero2 = Hero("Dumbledore", 180)

    # Trigger a fight between the two heroes
    hero1.fight(hero2)