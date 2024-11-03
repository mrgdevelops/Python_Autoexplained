# 10 Important Python Concepts in 20 minutes
# https://www.youtube.com/watch?v=Gx5qb1uHss4

from datetime import datetime

# Defining functions:

def show_date() -> None: # None means that the function does not return anything (is optional)
    print('This is the current date and time:')
    print(datetime.now())

def greet(name: str) -> None:
    print(f'Ciao, {name}!')
    
def add(a: float, b: float) -> float:
    return a + b

# Calling the same function several times:
show_date()
show_date()
show_date()

# Calling functions with arguments:
greet('Alice')
greet('Bob')

print(add(2, 3))
