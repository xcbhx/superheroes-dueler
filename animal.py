
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        # The eat method should print the animal's name and "is eating"
        print(f'{self.name} is eating.')

    def drink(self):
        # The drink method should print the animal's name and "is drinking"
        print(f'{self.name} is drinking.')


# create the Frog class, which is a subclass of Animal, and has the method jump, 

class Frog(Animal):
    def jump(self):
        # which prints the frog's name and "is jumping"
        print(f'{self.name} is jumping.')
    

# Instantiate 
pet_name = Animal('Clay')
pet_name.eat()
pet_name.drink()

pet_name2 = Frog('Duck')
pet_name2.jump()