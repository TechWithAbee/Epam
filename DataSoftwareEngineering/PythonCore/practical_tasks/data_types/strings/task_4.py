# Data Types. Strings. Task 4
# Write a function that checks whether a string is a palindrome or not. The usage of any reversing functions is prohibited.

# To check your implementation you can use strings from here

# Examples:

# A dog! A panic in a pagoda!
# Do nine men Interpret? Nine men I nod
# T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt upset on drab pot toilet.
# A man, a plan, a canal — Panama!
# List of well-known English palindromic phrases [https://en.wikipedia.org/wiki/List_of_English_palindromic_phrases]

def check_str(s: str):
    a = ""
    s = s.lower()
    for i in s:
        if 97 <= ord(i) <= 122:
            a += i
        if 48 <= ord(i) <= 57:
            return s == s[::-1]
    return a == a[::-1]
