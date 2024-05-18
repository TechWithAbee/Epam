# Data Types. Strings. Task 2
# Implement a function get_longest_word(s: str) -> str which returns the longest word in the given string. 
# The word can contain any symbols except whitespaces (' ', '\n', '\t' and so on). 
# If there are multiple longest words in the string with the same length return the word that occurs first.

# Example:

# >>> get_longest_word('Python is simple and effective!')
# 'effective!'

def get_longest_word(s: str) -> str:
    w = ""
    g = 0
    s = s.split()
    for i in s:
        if g < len(i):
            g = len(i)
            w = i
    return w
