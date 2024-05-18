# Implement the keyword encoding and decoding for the Latin alphabet. The keyword cipher uses a keyword to rearrange the letters in the alphabet. You should add the provided keyword at the beginning of the alphabet. A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet. The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in alphabetical order, excluding those already used in the key.

# Encryption:

# The keyword is "Crypto"

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# C R Y P T O A B D E F G H I J K L M N Q S U V W X Z
# Example:

# >>> cipher = Cipher("crypto")
# >>> cipher.encode("Hello world")
# "Btggj vjmgp"

# >>> cipher.decode("Fjedhc dn atidsn")
# "Kojima is genius"


class Cipher:
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'

    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.keyword_map = dict()
        self.alphabet = self.alphabet.split()
        self.new_alphabet = ''.join([char for char in self.keyword] + [char for char in self.alphabet if char not in self.keyword])
        
        print('old_alphabet:', ''.join(self.alphabet))
        print('new_alphabet:', self.new_alphabet)

        for i, char in enumerate(self.alphabet):
            self.keyword_map[char] = self.new_alphabet[i]
        
        print('keyword_map:', self.keyword_map)
    
    def encode(self, text):
        encoded_text = ''
        for char in text:
            if char.upper() in self.keyword_map:
                if char.isupper():
                    encoded_text += self.keyword_map[char.upper()]
                else:
                    encoded_text += self.keyword_map[char.upper()].lower()
            else:
                encoded_text += char
        return encoded_text
    
    def decode(self, text):
        decoded_text = ''
        for char in text:
            if char.upper() in self.keyword_map.values():
                if char.isupper():
                    decoded_text += [key for key, value in self.keyword_map.items() if value == char.upper()][0]
                else:
                    decoded_text += [key for key, value in self.keyword_map.items() if value == char.upper()][0].lower()
            else:
                decoded_text += char
        return decoded_text


cipher = Cipher("crypto")
print(cipher.encode("Hello World"))
print(cipher.decode("Btggj vjmgp"))