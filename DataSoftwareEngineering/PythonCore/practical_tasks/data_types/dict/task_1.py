# Data Types. Dictionaries. Task 1.
# Write a Python program to count the frequency of each character in a string (ignore the case of letters).

# Example:

# Input: 'Oh, it is python'

# Output: {" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}

from typing import Dict

def get_dict(s: str) -> Dict[str, int]:
    s = s.lower()
    my_dict = {}
    for i in s:
        my_dict[i] = my_dict.get(i, 0) + 1
    return my_dict

# Usage
print(get_dict('Oh, it is python'))