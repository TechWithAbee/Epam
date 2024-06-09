# You have to overload the addition operator in Counter class. Use the __add__() magic method to overload the addition.
# For example, in case of a + b, a object should have __add__() which accepts b as a second parameter (self goes first).
# In this case, Counter object accepts a list from int as a parameter. Object to summarize with will be a str object.
# The result should be a list of strings which have the following pattern: 
# 1 test - one object from list and str separated by the whitespace.

# Example

# >>> Counter([1, 2, 3]) + "mississippi"

# ["1 mississippi", "2 mississippi" , "3 mississippi"]


from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, string):
        new_list = []
        for i in self.values:
            new_list.append(str(i) + " " + string)
        return new_list

# example

print(Counter([1, 2, 3]) + "mississippi") # ["1 mississippi", "2 mississippi" , "3 mississippi"]