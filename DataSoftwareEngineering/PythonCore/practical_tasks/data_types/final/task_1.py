# Data Types. Final task 1
# Write a Python program to print all the unique values of all the dictionaries in a list.

# Example:

# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique_values = set()
    for dictionary in lst: # {"V":"S001", "V":"S001", "V":"S001"}
        for value in dictionary.values():
            unique_values.add(value)
    return unique_values

# Usage
print(check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])) # {'S005', 'S002', 'S007', 'S001', 'S009'}