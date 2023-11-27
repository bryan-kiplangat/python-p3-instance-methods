#!/usr/bin/env python3

class Dog:
    def bark(self):
        print("Woof!")
        
    def sit(sit):
        print("The dog is sitting.")
    
# instantiate dog class to fido
fido = Dog()
fido.bark()
fido.sit()

snoopy = Dog()

# Each of these instances is totally unique, even though they are all born from Dog
print(fido)
print(snoopy)
print(snoopy == fido) #false