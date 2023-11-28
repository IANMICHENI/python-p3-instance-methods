#!/usr/bin/env python3
class Dog:
   def bark(self):
    print("Woof!")

   def sit(self):
        print("The dog is sitting.")
        
fido = Dog()
fido.bark()
# Woof!

fido.sit()
# AttributeError: 'Dog' object has no attribute 'sit'
pass
