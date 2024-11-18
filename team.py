from hero import Hero

class Team:
    def __init__(self, name):
        self.name = name

        def stats(self):
            '''Print team statistics'''
            for hero in self.heroes:
                kd = hero.kills / hero.deaths
                print(f'{hero.name} Kill/Deaths: {kd}')
                