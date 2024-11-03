# 10 Important Python Concepts in 20 minutes
# https://www.youtube.com/watch?v=Gx5qb1uHss4

# Methods are functions that are defined inside a class

class Motorbike:
    def __init__(self, brand: str, horsepower: int) -> None: # Constructor (initializer), returns nothing
        self.brand = brand
        self.horsepower = horsepower
        
    def ride(self) -> None: # Method
        print(f'Riding the motorbike {self.brand}')
        
    def getInfo(self) -> None: # Method
        print(f'This motorbike is {self.brand} and has {self.horsepower} horsepower')

yamahaDragStar: Motorbike = Motorbike('Yamaha', 50) # instance of the class (object)
yamahaDragStar.ride()
yamahaDragStar.getInfo()

harleyFatBoy: Motorbike = Motorbike('Harley', 100)
harleyFatBoy.ride()
harleyFatBoy.getInfo()
