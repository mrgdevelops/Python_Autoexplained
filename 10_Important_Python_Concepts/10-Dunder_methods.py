# 10 Important Python Concepts in 20 minutes
# https://www.youtube.com/watch?v=Gx5qb1uHss4

from typing import Self

class Motorbike:
    def __init__(self, brand: str, horsepower: int) -> None: # Constructor (initializer), returns nothing
        self.brand = brand
        self.horsepower = horsepower
    
    def __str__(self) -> str: # Dunder method
        return f'Motorbike {self.brand} with {self.horsepower} horsepower'

yamahaDragStar: Motorbike = Motorbike('Yamaha', 50) # instance of the class (object)

print(yamahaDragStar) # Returns: <__main__.Motorbike object at 0x7f8b1c3b3d30>
# With the __str__ method, it returns: Motorbike Yamaha with 50 horsepower
