class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


    # Methods are defined as their own named functions inside the class
    def bark(self):
        print(f'{self.name} say Woof!')
    
    def sit(self):
        print(f'{self.name} sits.')

    def roll(self):
        print(f'{self.name} rolls over.')