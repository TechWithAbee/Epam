from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    # Sort and filter the indexes to only include valid ones
    indexes = sorted([i for i in indexes if 0 <= i < len(s)])
    
    # If there are no valid indexes, return the original string as a single-element list
    if not indexes:
        return [s]
    
    # Initialize the result list and the starting index
    result = []
    start = 0
    
    for index in indexes:
        # Append the substring from the start index to the current index
        result.append(s[start:index])
        # Update the start index to the current index
        start = index
    
    # Append the remaining part of the string
    result.append(s[start:])
    
    return result

# Examples
print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))  # ["python", "is", "cool", ",", "isn't", "it?"]
print(split_by_index("no luck", [42]))  # ["no luck"]
