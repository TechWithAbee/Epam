# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.
# Example:

# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True

class Sun: # 1. `class Sun:` - This line is defining a new class named `Sun`.
    _instance = None # 2. `_instance = None` - This is a class variable that will hold the single instance of the `Sun` class. It is initially set to `None`.

    @classmethod # 3. `@classmethod` - This is a decorator in Python that makes the method `inst()` a class method. Class methods receive the class as the first argument (conventionally named `cls`) instead of an instance (`self`).
    def inst(cls): # 4. `def inst(cls):` - This is the definition of the class method `inst()`. This method will be used to create and return the single instance of the `Sun` class.
        if cls._instance is None: # 5. `if cls._instance is None:` - This line checks if the `_instance` class variable is `None`. If it is, that means an instance of the `Sun` class has not been created yet.
            cls._instance = cls() # 6. `cls._instance = cls()` - If `_instance` is `None`, this line creates a new instance of the `Sun` class and assigns it to `_instance`.
        return cls._instance # 7. `return cls._instance` - This line returns the instance of the `Sun` class. If an instance already existed, it simply returns that. If not, it creates a new one and then returns it.

# The purpose of this design pattern is to ensure that only one instance of the `Sun` class can ever be created. This can be useful in situations where you want to ensure that a certain resource or state is accessed globally and consistently across your program.

# Example usage:
p = Sun.inst()
f = Sun.inst()
print(p is f)