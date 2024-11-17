from ability import Ability

import random 

class Weapon(Ability):
    def attack(self):
        '''This method returns a random value between one half 
        to the full attack power of the weapon.
        '''
        # Use integer division between half of max_damage
        half_damage = self.max_damage // 2
        # Return a random integer between half_damage and max_damage
        return random.randint(half_damage, self.max_damage)



# Instantiate 
if __name__ == '__main__':
    weapon = Weapon('Debugging Weapon', 50)
    print(f'Weapon attack value: {weapon.attack()}')
