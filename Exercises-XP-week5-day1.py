#Exercise 1

from os import name
from pip import main


class Cat:
    species = 'mammal'
    def __init__(self, cat_name, cat_age,cat_race):
        print("A new cat has been initialized !")
        self.name = cat_name
        self.age = cat_age
        self.race = cat_race

    
    def show_details(self):
        print("My name is:"+self.name)
        print("My age is:"+str(self.age)+" "+"month")
        print("My race is:"+" "+self.race)


simba = Cat("Simba",2,"Persian")
garlfield = Cat("garlfield",1,"Persian")
simba.show_details()


def get_oldest_cat(*args):
    return max(args)

print(f"The oldest cat is {get_oldest_cat(simba.age, garlfield.age)} years old.")


#Exercise 2

class Dog:
    species = 'dog'
    def __init__(self,dog_name,dog_height):
        print("A new dog has been initialized !")
        self.name = dog_name
        self.height = dog_height
    
    
    def bark(self):
        print("{} goes woof!".format(self.name))

    def jump(self):
        x = self.height / 2.54
        print(self.name +" "+ "jumps in {} cm".format(x))


name_dog = Dog("Alex",20)
name_dog.bark()
name_dog.jump() 

david_dog = Dog("Rex",50)
sarahs_dog = Dog("Teacup",20)
david_dog.jump()
david_dog.bark()
sarahs_dog.jump()
sarahs_dog.bark()

def get_biggest_dog(*args):
    return max(args)

print(f"The biggest dog is {get_biggest_dog(name_dog.height, david_dog.height)} cm.")


#Exercise 3

class Song:
    def __init__(self,lyrics):
        self.lyrics = lyrics

list=[]
list.append(Song('There’s a lady who sure,all that glitters is gold,and she is buying a stairway to heaven'))

for obj in list:
    print( obj.lyrics,sep =' ' )
