# Implement a function that works the same as str.split method
# (without using str.split itself, ofcourse).
# Pay attention to strings with multiple spaces. For example: '    Hi     Python    world!'
# Example:

#     def split(data: str, sep=None, maxsplit=-1):


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
    # assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']