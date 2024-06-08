# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.
# Example:

# >>> p = Sun.inst()
# >>> f = Sun.inst()
# >>> p is f
# True

class Sun:
    _instance = None

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance