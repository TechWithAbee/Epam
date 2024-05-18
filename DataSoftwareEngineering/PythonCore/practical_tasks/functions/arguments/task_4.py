# Functions. Decorators. Functions Arguments. Task 3.
# Implement a function that receives a changeable number of dictionaries (keys - letters, values - numbers) 
# and combines them into one dictionary. Dict values should be summarized in case of identical keys

# def combine_dicts(*args):
#     ...

# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}

# print(combine_dicts(dict_1, dict_2))
# >>> {'a': 300, 'b': 200, 'c': 300}

# print(combine_dicts(dict_1, dict_2, dict_3))
# >>> {'a': 600, 'b': 200, 'c': 300, 'd': 100}

from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    new_dict = dict()
    for arg in args:
        for item, value in arg.items():
            new_dict[item] = new_dict.get(item, 0) + value
    return new_dict
