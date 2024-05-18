# Functions. Decorators. Recursions. Task 1.
# Define a function seq_sum(sequence) which allows counting the sum of elements. 
# Elements of all nested sequences should be included.

# Example:

# def seq_sum(sequence):
#     pass
  
# sequence = [1,2,3,[4,5, (6,7)]]

# >>> print(seq_sum(sequence))
# 28

from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    total = 0
    for item in sequence: # [1,2,3,[4,5, (6,7)]]
        if isinstance(item, (list, tuple)): # (6,7)
            total += seq_sum(item) # [4,5, (6,7)]
        else:
            total += item # 0+1=1
    return total

# Test the function
sequence = [1,2,3,[4,5, (6,7)]]

print(seq_sum(sequence)) # 28
