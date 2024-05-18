# Data Types. Lists. Task 2
# Update the get_fizzbuzz_list function. The function has to generate and 
# return a list with numbers from 1 to n inclusive where the n is passed as a parameter to the function. 
# But if the number is divided by 3 the function puts a Fizz word into the list, 
# and if the number is divided by 5 the function puts a Buzz word into the list. 
# If the number is divided by both 3 and 5 the function puts FizzBuzz into the list.

from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    a = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            a.append("FizzBuzz")
        elif i % 3 == 0:
            a.append("Fizz")
        elif i % 5 == 0:
            a.append("Buzz")
        else:
            a.append(i)
    return a
