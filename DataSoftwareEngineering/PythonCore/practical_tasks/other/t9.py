# class Callable:
#     def __call__(self, *args, **kwargs):
#         print('Called with', args, kwargs)

# c = Callable()
# c(1, 2, 3, x=4, y=5)

# You have to overload the addition operator in the Counter class. Use the __add__() magic method to overload the addition.

# For example, in the case of a + b, the a object should have __add__(), which accepts b as a second parameter (self goes first).

# In this case, the Counter object accepts a list from int as a parameter. The object to summarize with will be a str object. The result should be a list of strings with the following pattern: 1 test - one object from list and str separated by the whitespace.

# Example
# >>> Counter([1, 2, 3]) + "Mississippi"

# ["1 Mississippi", "2 Mississippi" , "3 Mississippi"]


class Counter:
    def __init__(self, lst):
        self.lst = lst

    def __add__(self, string):
        new_list = []
        for i in self.lst:
            s = str(i) + " " + string
            new_list.append(s)
        return new_list

a = Counter([1, 2, 3]) + "Mississippi"
print(a)

print("-------------------------------------------------")

# Magic Methods. Task 2
# Create a hierarchy out of birds. Implement four classes:

# Class Bird with an attribute name and methods fly and walk.
# Class FlyingBird with attributes name, ration, and with the same methods. ration must have a default value. Implement the method eat, which will describe its typical ration.
# Class NonFlyingBird with the same characteristics but obviously without an attribute fly. Add the same "eat" method but with other implementations regarding the swimming bird tastes.
# Class SuperBird, which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
# Implement a str() function call for each class.

# Example:

# >>> b = Bird("Any")
# >>> b.walk()
# "Any bird can walk"

# p = NonFlyingBird("Penguin", "fish")
# >> p.swim()
# "Penguin bird can swim"
# >>> p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# >>> p.eat()
# "It eats mostly fish"

# c = FlyingBird("Canary")
# >>> str(c)
# "Canary bird can walk and fly"
# >>> c.eat()
# "It eats mostly grains"

# s = SuperBird("Gull")
# >>> str(s)
# "Gull bird can walk, swim and fly"
# >>> s.eat()
# "It eats mostly fish"
# Look at the mro method or the attribute __mro__ of your last class.


class Bird:
    def __init__(self, name) -> None:
        self.name = name
    
    def walk(self):
        return f"{self.name} bird can walk"
    
    def __str__(self):
        return f"{self.name} bird can walk"
    
class FlyingBird(Bird):
    def __init__(self, name, ration="grains") -> None:
        super().__init__(name)
        self.ration = ration
    
    def fly(self):
        return f"{self.name} bird can fly"
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def __str__(self):
        return f"{self.name} bird can walk and fly"
    
    
class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish") -> None:
        super().__init__(name)
        self.ration = ration
    
    def eat(self):
        return f"It eats mostly {self.ration}"
    
    def swim(self):
        return f"{self.name} bird can swim"
    
    def __str__(self):
        return f"{self.name} bird can walk and swim"
    
class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="fish") -> None:
        super().__init__(name, ration)
    
    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"

b = Bird("Any")
print(b.walk())

p = NonFlyingBird("Penguin", "fish")
print(p.swim())
# print(p.fly())
print(p.eat())

c = FlyingBird("Canary")
print(str(c))
print(c.eat())

s = SuperBird("Gull")
print(str(s))
print(s.eat())
print(SuperBird.__mro__)

print("-------------------------------------------------")