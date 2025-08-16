#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Fido", breed="Pug"):
        self._name = "Fido"
        self.name = name

        self._breed ="Pug"
        self.breed = breed


        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, dog_name):
        if isinstance(dog_name, str) and 1<= len(dog_name) <=25:
            self._name=dog_name
        else:
            print("Name must be string between 1 and 25 characters.")
    # pass
    # pass

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, dog_breed):
        if dog_breed in APPROVED_BREEDS:
            self._breed = dog_breed
        else:
            print("Breed must be in list of approved breeds.")
