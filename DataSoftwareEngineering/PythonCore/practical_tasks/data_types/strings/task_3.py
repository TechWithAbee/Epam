# Data Types. Strings. Task 3
# Implement a function that receives a string and replaces all " symbols with ' and vice versa.

def replacer(s: str) -> str:
    a = ""
    for i in s: # I "a\'m"
        if i == '"':
            a += "'"
        elif i == "'":
            a += '"'
        else:
            a += i
    return a

s = 'I "a\'m" '
a = replacer(s)
print(a) # I am '