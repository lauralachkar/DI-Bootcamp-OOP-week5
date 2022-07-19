#Exercise 1

from cProfile import run
from os import name
from turtle import speed


class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

simba = Siamese("Simba",2)
gouss = Chartreux("gouss",1)
max = Bengal("max",1)
allcats = [simba,gouss,max]
simba.name
sarahPets = Pets(allcats)
sarahPets.walk()

#Exercise 2

class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(self.name + " "+"is"+" "+"barking")

    def run_speed(self):
        speed = (self.weight/self.age)*10
        print(self.name,speed)

    # def fight(self,other_dog):
    #     other_dog_speed = other_dog.run_speed
    #     if(self.run_speed > other_dog_speed):
    #         return self.name
    #     else:
    #         return other_dog.name    


Owen = Dog("Owen",20,15)
Bucki = Dog("Bucki",30,5)
Owen.bark()
Bucki.bark()
Owen.run_speed()
Bucki.run_speed()
# Bucki.fight(Owen)

