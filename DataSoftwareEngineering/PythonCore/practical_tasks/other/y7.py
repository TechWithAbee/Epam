from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    return tuple(map(int, str(num)))

print(get_tuple(87178291199))


from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    return list(zip(lst, lst[1:]))

print(get_pairs([1, 2, 3, 8, 9]))  # [(1, 2), (2, 3), (3, 8), (8, 9)]
print(get_pairs(['need', 'to', 'sleep', 'more'])) # [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')] 
print(get_pairs([1]))  # []