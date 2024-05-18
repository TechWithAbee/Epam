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

# Example usage
b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# Output: Author='William Faulkner', Name='The Sound and the Fury', Price='12'

b.price = 55
print(b.price)  # Output: 55

try:
    b.price = -12
except ValueError as e:
    print(e)  # Output: Price must be between 0 and 100.

try:
    b.price = 101
except ValueError as e:
    print(e)  # Output: Price must be between 0 and 100.

try:
    b.author = "new author"
except ValueError as e:
    print(e)  # Output: Author cannot be changed.

try:
    b.name = "new name"
except ValueError as e:
    print(e)  # Output: Name cannot be changed.
