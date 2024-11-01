from abc import ABC, abstractmethod

class animal():
    
    @abstractmethod
    def make_sound(self):
        pass
    
    def descripe(self):
        print("Animal description")
        
        
class Dog(animal):
    def make_sound(self):
        print("Dog sound")
        return super().make_sound()        
    
class Cat(animal):
    def make_sound(self):
        print("Cat sound")
        return super().make_sound()   
    
class Cow(animal):
    def make_sound(self):
        print("Cow sound")
        return super().make_sound()       
        