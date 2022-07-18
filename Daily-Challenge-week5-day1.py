from os import name
from re import M
from turtle import pen
from pip import main

class Farm:
    def __init__(self,farm_name,animal_type,animal_number):
        print("A new farm has been initialized !")
        self.list1 =[]
        self.name = farm_name
        self.type = animal_type
        self.number = animal_number

    def get_info(self):
        print("Welcome to the"+" "+"farm"+" "+self.name+"!!!!")
        print("In this"+" "+self.name+" "+"farm"+" "+ "there is "+self.type)
        print("In this"+" "+self.name+" "+"farm"+" "+ "there is "+str(self.number)+" "+self.type)
    
    def get_animal_types(self):
        self.list1 = self.type.split(" ")
        print(self.list1)
    
    # def get_short_info(self):
    #     print(f"{self.name} farm has{','.join(self.get_animal_types())}.")
    #     print(self.list1)



macdonald = Farm("macdonald","sheep",20)
Heartland = Farm("Hearland","horses",30)
macdonald.get_info() 
Heartland.get_info()
macdonald.get_animal_types()
Heartland.get_animal_types()

