# Functions. Decorators. Decorators. Task 2
# Write a decorator that logs information about calls of decorated functions, the values of its arguments, keyword arguments, and execution time. The log should be written to a file.

# Example of Using
# @log
# def foo(a, b, c):
#     ...

# foo(1, 2, c=3)
# log.txt
# ...
# foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
# ...

import time


def log(func):
    def wrapper(*args, **kwargs):
        filepath = 'log.txt'
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time

        arg_str = ", ".join(f"{k}={v}" for k, v in zip(func.__code__.co_varnames, args))
        kwarg_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        
        with open(filepath, 'w') as f:
            f.write(f'{func.__name__}; args: {arg_str}; kwargs: {kwarg_str}; execution time: {exec_time}')
        
        return result
    return wrapper

@log
def foo(a, b, c):
    pass

foo(1, 2, c=3)