# Functions. Decorators. Decorators. Task 3.
# Create decorator validate which validates arguments in set_pixel function. All function parameters should be between 0(int) and 256(int) inclusive.
# In case if all parameters are valid, set_pixel function should return "Pixel created!" message. Otherwise, it should return "Function call is not valid!" message.
# Use functools.wraps where is it necessary.
# Don't forget about doc stings.
# Examples

# >>> set_pixel(0, 127, 300)
# Function call is not valid!
# >>> set_pixel(0,127,250)
# Pixel created!


def validate(func):
    def wrapper(*args):
        for arg in args:
            if arg < 0 or arg > 256:
                return "Function call is not valid!"
        return func(*args)
    return wrapper
    

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"

print(set_pixel(0, 127, 300))
print(set_pixel(0,127,250))