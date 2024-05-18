# Decorators Factory
# Create a decorator factory (decorator itself). The factory accepts a function (lambda) as an input and returns a decorator that will return the result of the function as the first argument. The result of the decorated function is passed. The function that the factory accepts (in the example below, it is a lambda) can only take one positional parameter.

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
def return_user_id(num: int): 
    return num

print(return_user_id(42) )
# >>> 43


print('-----------------')

def foo(positional, only, /, either, pos, or_='default', *, keyword, just, **keywords):
    print(positional, only, either, pos, or_, keyword, just, keywords)

foo('a', 'b', 1, 2, 'or_', keyword= 'keyword', just='just', unknown_keyword='unknown_keyword')

print('-------global----------')

x = 1
def foo():
    globals()['x'] = 2
    def bar():
        print(x)
    bar()
foo()

print('-----------------')
x = 1
def foo():
    x = 2
    def bar():
        global x
        print(x)
    bar()
x = 3
foo()

print('-----------------')

x = 1
def foo():
    x = 2
    def bar(x=3):
        print(x)
    bar()
foo()

print('-----------------')

x = 1
def foo():
    # nonlocal x
    def bar():
        print(x)
    bar()
x = 3
foo()


print('-----------------')

from typing import List, Optional


def split(data: str, sep: Optional[str] = None, maxsplit: int = -1) -> List[str]:
    if sep is None:  # Default split by whitespace
        return _split_whitespace(data, maxsplit)
    else:  # Split by the specified separator
        return _split_by_separator(data, sep, maxsplit)

def _split_whitespace(data: str, maxsplit: int) -> List[str]:
    if maxsplit == 0:
        return [data.strip()]
    
    result = []
    word = []
    splits = 0
    
    i, n = 0, len(data)
    while i < n:
        if data[i].isspace():
            if word or (result and result[-1]):
                result.append(''.join(word))
                word = []
                splits += 1
                if 0 < maxsplit == splits:
                    break
        else:
            word.append(data[i])
        i += 1
    
    if word or (not result and not word):
        result.append(''.join(word))
    
    if 0 < maxsplit == splits and i < n:
        remaining = data[i:].lstrip()
        if remaining:
            result.append(remaining)
    
    return [x for x in result if x]

def _split_by_separator(data: str, sep: str, maxsplit: int) -> List[str]:
    if maxsplit == 0:
        return [data]
    
    result = []
    word = []
    sep_len = len(sep)
    splits = 0
    i = 0

    # Handle the initial separator at the beginning of the string
    if data[:sep_len] == sep:
        result.append('')
        splits += 1
        i += sep_len

    while i < len(data):
        if data[i:i + sep_len] == sep:
            result.append(''.join(word))
            word = []
            splits += 1
            i += sep_len
            if 0 < maxsplit == splits:
                break
        else:
            word.append(data[i])
            i += 1
    
    if word:
        result.append(''.join(word))
    
    if 0 < maxsplit == splits and i < len(data):
        result.append(data[i:])
    
    return result

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']


