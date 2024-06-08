# Description
# Create a class SchoolMember which represents any person in school.
# Classes Teacher and Student are inherited from SchoolMember.
# Classes should have the same interface with the public show () method.
# Teacher accepts name (str), age (int), salary (int).
# Student accepts name (str), age (int), grades.
# Move the same logic of initialization to the class SchoolMember.
# Method show() returns string (see string patters in Example).

# Example

# >>> persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

# >>> for person in persons:
#        print(person.show())

# "Name: Mr.Snape, Age: 40, Salary: 3000"
# "Name: Harry, Age: 16, Grades: 75"

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"

persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]

for person in persons:
    print(person.show())

# "Name: Mr.Snape, Age: 40, Salary: 3000"
# "Name: Harry, Age: 16, Grades: 75"