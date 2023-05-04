"""
Python is an object-oriented programming (OOP) language. This means that it supports the creation of
objects, which are instances of classes that encapsulate data and behavior. In this answer, we'll go
over some of the key concepts of object-oriented programming in Python.

# Classes

In Python, you define a class using the class keyword followed by the name of the class, a colon, and
the body of the class. The body of the class contains the attributes (variables) and methods (functions)
that define the behavior of the class.

Here's an example of a simple class definition in Python:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")
In this example, we define a class called Person. It has two attributes, name and age, and one method,
say_hello. The __init__ method is a special method that is called when a new instance of the class is
created. It sets the initial values of the name and age attributes.

# Objects

To create an object (also called an instance) of a class in Python, you simply call the class like a
function, passing in any necessary arguments. This creates a new object with the attributes and
methods defined by the class.

Here's an example of creating a new Person object:

person = Person("Alice", 30)
In this example, we create a new Person object with the name "Alice" and the age 30. The person
variable now contains a reference to this object.

# Attributes

Attributes are variables that are attached to an object. They store data that is specific to the object.
You can access an object's attributes using dot notation:

print(person.name)  # Output: Alice
print(person.age)   # Output: 30
In this example, we access the name and age attributes of the person object using dot notation.

# Methods

Methods are functions that are attached to an object. They define the behavior of the object. You
can call an object's methods using dot notation:

person.say_hello()  # Output: Hello, my name is Alice and I am 30 years old.
In this example, we call the say_hello method of the person object using dot notation.

# Inheritance

Inheritance is a way to create a new class that is a modified version of an existing class.
The new class (called the subclass) inherits all the attributes and methods of the existing
class (called the superclass), and can add or override attributes and methods as needed.

Here's an example of a subclass that inherits from the Person class:

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def say_hello(self):
        print("Hello, my name is", self.name, "and I am a student in grade", self.grade)
In this example, we define a new class called Student that inherits from the Person class.
It adds a new attribute called grade and overrides the say_hello method to print a different message.

# Polymorphism

Polymorphism is the ability of objects to take on multiple forms. In Python, this means that
 objects of different classes can be treated as if they are the same type. This allows you to write

"""


# main concepts in oops
"""
The main concepts in object-oriented programming (OOP) in Python are:

1. Classes: A class is a blueprint for creating objects that define a set of attributes (variables) and 
methods (functions) that define the behavior of the objects.

2. Objects: An object is an instance of a class. It has its own set of attributes and methods that define 
its behavior.

3. Encapsulation: Encapsulation is the idea of hiding the implementation details of a class from the outside 
world, and providing a clean and simple interface for interacting with the class. This is achieved in Python 
using access modifiers like public, private, and protected.

4. Inheritance: Inheritance is a way to create a new class that is a modified version of an existing class. The 
new class (called the subclass) inherits all the attributes and methods of the existing class (called the 
superclass), and can add or override attributes and methods as needed.

5. Polymorphism: Polymorphism is the ability of objects to take on multiple forms. In Python, this means that 
objects of different classes can be treated as if they are the same type. This allows you to write more 
generic and reusable code.

6. Abstraction: Abstraction is the idea of focusing on the essential features of an object, while ignoring 
the details that are not relevant to the current context. This is achieved in Python by defining abstract 
base classes, which provide a common interface for a group of related classes.

7. Method overriding: Method overriding is the ability to define a method in a subclass that has the same 
name and parameters as a method in the superclass, but with a different implementation.

8. Method overloading: Method overloading is the ability to define multiple methods with the same name in 
a class, but with different parameters. In Python, method overloading is not supported natively, but can 
be achieved using default parameters or variable-length argument lists.

By understanding these main concepts of OOP in Python, you can write more structured, 
maintainable, and reusable code.
"""