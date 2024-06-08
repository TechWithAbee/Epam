# Write a decorator which logs information about calls of decorated function,
# values of its arguments, values of keyword arguments and execution time. Log
# should be written to a file.

# Example of using

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
        start_time = time.time() # get current time 
        result = func(*args, **kwargs)
        end_time = time.time() # get current time 
        exec_time = end_time - start_time

        arg_str = ", ".join(f"{k}={v}" for k, v in zip(func.__code__.co_varnames, args))
        kwarg_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        
        with open(filepath, 'w') as file:
            file.write(f'{func.__name__}; args: {arg_str}; kwargs: {kwarg_str}; execution time: {exec_time}')
        
        return result
    return wrapper

@log
def foo(a, b, c):
    return a + b + c

print(foo(1, 2, c=3))