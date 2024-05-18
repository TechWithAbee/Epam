# Data Types. Strings. Task 1
# Fractions
# Create a function that takes two parameters of string type which are fractions with the same denominator and returns a sum expression of these fractions and the sum result.

# For example:

# >>> a_b = '1/3'
# >>> c_b = '5/3'
# >>> get_fractions(a_b, c_b)
# '1/3 + 5/3 = 6/3'

def get_fractions(a_b: str, c_b: str) -> str:
    _a_b = a_b.split('/')
    a = _a_b[0]
    b = _a_b[1]
    _c_b = c_b.split('/')
    c = _c_b[0]
    b = _c_b[1]
    u = int(a) + int(c)
    return f'{a_b} + {c_b} = {str(u)}/{b}'
