# 10 Important Python Concepts in 20 minutes
# https://www.youtube.com/watch?v=Gx5qb1uHss4

# Classes are just BLUEPRINTS for creating objects

class Motorbike:
    def __init__(self, colour: str, horsepower: int) -> None: # Constructor (initializer), returns nothing
        self.colour = colour
        self.horsepower = horsepower
        
harleyFatBoy: Motorbike = Motorbike('black', 100) # instance of the class (object)
print(harleyFatBoy.colour)
print(harleyFatBoy.horsepower)

yamahaDragStar: Motorbike = Motorbike('blue', 50)
print(yamahaDragStar.colour)
print(yamahaDragStar.horsepower)
