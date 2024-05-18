# Data Types. Lists. Task 1
# Write a Python program that accepts a sequence of words as input and prints the unique words in a sorted form.

# Examples:

# Input:

# ('red', 'white', 'black', 'red', 'green', 'black') 
# Output:

# ['black', 'green', 'red', 'white']


from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    a = []
    for i in str_list:
        if i not in a:
            a.append(i)
    a.sort()
    return a
    
