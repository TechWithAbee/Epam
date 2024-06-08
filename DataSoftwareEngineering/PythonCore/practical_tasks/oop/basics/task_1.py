# Develop a class Field with "full encapsulation", whose attributes are accessed 
# and data changes are implemented through method calls.
# In OOP, it is generally accepted to start the names of methods for extracting data with the word "get",
# and the names of the methods in which fields are equated to a certain value - "set".
# In this task, you need to implement get_value and set_value methods for Field class (__value property).

class Field:
    __value = None
    def __init__(self):
        self.__value = None
    
    def get_value(self, ):
        return self.__value
    
    def set_value(self, value):
        self.__value = value

# Example:
f = Field()
f.set_value(42)
print(f.get_value()) # 42

f.set_value(43)
print(f.get_value()) # 43

f.set_value("value")
print(f.get_value()) # "value"
