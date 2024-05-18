# Functions. Decorators. Functions Arguments. Task 2.
# Create generic union and intersect functions to work with sets. 
# The functions must accept an arbitrary number of arguments of different types: list, tuple, and set. 
# Each function must return the value of the set type. For example:

# >>> union(('S', 'A', 'M'), ['S', 'P', 'A', 'C'])
# {'S', 'P', 'A', 'M', 'C'}

# >>> intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))
# {'S', 'C'}

def union(*args) -> set:
    result = set()
    for arg in args:
        result |= set(arg)
    return result


def intersect(*args) -> set:
    result = set(args[0])
    for arg in args[1:]:
        result &= set(arg)
    return result
    