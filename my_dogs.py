import dog


# instantiation call that creates a Dog object:
my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)


wyatt_dog = dog.Dog("Wyatt", "Bulldog")
wyatt_dog.bark()

bri_dog = dog.Dog("Bri", "poodle")
bri_dog.sit()

patch_dog = dog.Dog("Patch", "beagle")
patch_dog.roll()


