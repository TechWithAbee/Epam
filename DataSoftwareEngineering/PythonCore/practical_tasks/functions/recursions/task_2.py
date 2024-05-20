# Functions. Decorators. Recursions. Task 2.
# Define a function linear_seq(sequence) which converts a passed sequence to a sequence without nested sequences.

# Example:

# def linear_seq(sequence):
#     pass
  
# sequence = [1,2,3,[4,5, (6,7)]]

# >>> print(linear_seq(sequence))
# [1,2,3,4,5,6,7]

from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    total = []
    for item in sequence: # [1,2,3,[4,5, (6,7)]]
        if isinstance(item, (list, tuple)):
            total.extend(linear_seq(item))
        else:
            total.append(item)
    return total

# Test the function
sequence = [1,2,3,[4,5, (6,7)]]

print(linear_seq(sequence)) # [1,2,3,4,5,6,7]