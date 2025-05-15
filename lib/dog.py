#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):  # Correct spelling and default value
        self.name = name
        self.breed = breed

# Create dogs OUTSIDE the class
dog1 = Dog("Fido", "Dalmatian")
dog2 = Dog("Fido")  # No breed, should default to "Mutt"

print(dog1.name)   # Fido
print(dog1.breed)  # Dalmatian

print(dog2.name)   # Fido
print(dog2.breed)  # Mutt
