from hero import Hero

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
                hero.current_health = hero.starting_heath