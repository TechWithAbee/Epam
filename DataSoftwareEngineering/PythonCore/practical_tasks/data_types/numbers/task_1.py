# Data Types. Numbers. Task 1

# Rounding
# Create a function with two parameters a and b. The function calculates the following expression:

# (12 * a + 25 * b) / (1 + a**(2**b))	

# and returns a result of the expression rounded up to the second decimal place.

from typing import Union

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  r = None
  expression = (12 * a + 25 * b) / (11 + a ** (2 ** b))
  r = round(expression, 2)
  return r

# Test the function
print(some_expression_with_rounding(1, 2))
