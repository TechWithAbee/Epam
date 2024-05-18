# Functions. Decorators. Functions Arguments. Task 0.
# Implement a function that takes a number as an argument and returns a dictionary, 
# where a key is a number, and the value is the square of that number.

# Example:

# >>> generate_squares(5)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    """
    Add your code here or call it from here   
    """
    my_dict = {}
    for i in range(1, num+1):
        my_dict[i] = i**2
    return my_dict

# Test the function
print(generate_squares(5)) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}