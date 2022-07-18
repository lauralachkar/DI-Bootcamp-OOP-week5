from os import name
from pip import main

class Farm:
    def __init__(self,farm_name,animal_type,animal_number):
        print("A new farm has been initialized !")
        self.name = farm_name
        self.type = animal_type
        self.number = animal_number

    def get_info(self):
        print("Welcome to the"+" "+"farm"+" "+self.name+"!!!!")
        print("In this"+" "+self.name+" "+"farm"+" "+ "there is "+self.type)
        print("In this"+" "+self.name+" "+"farm"+" "+ "there is "+str(self.number)+" "+self.type)
     
    


macdonald = Farm("macdonald","sheep",20)
Heartland = Farm("Hearland","horses",30)
macdonald.get_info() 
Heartland.get_info()


animalType= [Farm("macdonald","sheep",20), Farm("Hearland","horses",30)]
for f in sorted(animalType, key=lambda x: x.type):
    print(f.type)


