# You have to implement class Book with attributes price, author, name.


# author and name fields have to be immutable;

# price field may be changes but has to be in 0 <= price <= 100 range.

# If user tries to change author or name fields after
# initialization or set price out of range, the ValueError should be raised.
# Implement descriptors PriceControl and NameControl to validate parameters.

# Example

# >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
# >>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# Author='William Faulkner', Name='The Sound and the Fury', Price='12'

# >>> b.price = 55
# >>> b.price
# 55
# >>> b.price = -12  # => ValueError: Price must be between 0 and 100.
# >>> b.price = 101  # => ValueError: Price must be between 0 and 100.

# >>> b.author = "new author"  # => ValueError: Author can not be changed.
# >>> b.name = "new name"      # => ValueError: Name can not be changed.

class PriceController:
    def __get__(self, instance, owner):
        return instance._price

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        instance._price = value

class NameController:
    def __init__(self, name):
        self._name = name

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        if hasattr(instance, '_initialized'):
            raise ValueError("Name cannot be changed.")
        self._name = value

class AuthorController:
    def __init__(self, author):
        self._author = author

    def __get__(self, instance, owner):
        return self._author

    def __set__(self, instance, value):
        if hasattr(instance, '_initialized'):
            raise ValueError("Author cannot be changed.")
        self._author = value

class Book:
    author = AuthorController("Author")
    name = NameController("Name")
    price = PriceController()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
        self._initialized = True

b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")

b.price = 55
b.price # 55
# b.price = -12  # => ValueError: Price must be between 0 and 100.
# b.price = 101  # => ValueError: Price must be between 0 and 100.

# b.author = "new author"  # => ValueError: Author can not be changed.
b.name = "new name"      # => ValueError: Name can not be changed.