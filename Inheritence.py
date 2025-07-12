#inheritence, super funtion, inheriting parents function and constructors

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"The name is {self.name} and the degree is "

    def __str__(self):
        pass

class Student(Person):
    def __init__(self, name, degree):
        # super function is used to inherit the parent constructor values like self.name = name.
        # We don’t have to write self.name = name here because we inherited it from above using super().
        super().__init__(name)
        self.degree = degree

p1 = Person("Deepak")
s1 = Student("Rohit", "Bca")

print(s1.display() + s1.degree)

# So far, this is how we inherit the class from one to another.
# The super() method in the child class constructor is important to actually inherit parent constructor code.
# The __init__ function gets overridden, and all other functions with the same name will get overridden by new functions in Student.

#other advance topics for later on
"""Multiple inheritance (class Child(A, B):)

Abstract base classes (using abc module)

Method Resolution Order (MRO)

super() in multiple inheritance context

Overriding other methods like __str__()"""