# Decorators Factory
# Create a decorators factory (decorator itself). The factory accepts a function (lambda) as an input and returns a decorator that will return the result of the function as the first argument, 
# the result of the decorated function is passed. The function which the factory accepts (in the example below it is a lambda) can take one positional parameter only.
# For example:

# >>> @decorator_apply(lambda user_id: user_id + 1)
# >>> def return_user_id(num: int): 
#         return num
# >>> return_user_id(42) 
# >>> 43


def decorator_apply(decorator_arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return decorator_arg(func(*args, **kwargs))
        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num

print(return_user_id(42))