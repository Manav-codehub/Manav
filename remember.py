"abstract class and abstract method in python "

# from abc import ABC,abstractmethod


# class father(ABC):
#     @abstractmethod
#     def property(self):
#         pass

#     @abstractmethod
#     def car(self):
#         pass

# class son1(father):
#     def property(self):
#         print("you get noidas property")

#     def car(self):
#         print("you get luxury car")
3


# class son2(father):
#     def property(self):
#         print("you get delhi property")

#     def car(self):
#         print("you get racing  car")

# s1=son1()
# s2=son2()


# s1.property()
# s2.property()
# s1.car()
# s2.car()

"polymorphism using method overriding"

# class animal:
#     def make_sound(self):
#         print("animal make sound")

# class dog(animal):
#     def make_sound(self):
#         print("bark")

# class cat(animal):
#     def make_sound(self):
#         print("meow")

# animals=[dog(),cat()]

# for i in animals:
#     i.make_sound()

"operator overloading in python "

# class employee:
    
#     def __init__(self,n,s,r):
#         self.name=n
#         self.salary=s
#         self.role=r
    
#     def show(self):
#         print(f"name of programmer is {self.name} with {self.salary} with {self.role}")

#     def __add__(self,x):
#         return self.role+x.role
    
#     def __truediv__(self,x):
#         return self.salary+x.salary


# e1=employee("manav",500,"ds")
# e2=employee("yuvi",400,"ca")
# print(e1+e2)

# class vector:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c

#     def show(self):
#         print(f"{self.a}a+{self.b}b+{self.c}c")

#     def __add__(self,x):
#         return vector (self.a+x.a,self.b+x.b ,self.c+x.c )
        



# v1=vector(2,4,6)
# v2=vector(3,6,9)

# print(type(v1+v2))

"static method "
# A static method in Python is a method that belongs to a class but does not use self or cls. 
# This means it does not depend on the instance (self) or the class (cls). 
# It behaves just like a regular function but is placed inside a class for better organization.

# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

# # Calling static method using class name
# print(MathUtils.add(5, 3))  # Output: 8

# # Calling static method using instance
# obj = MathUtils()
# print(obj.add(10, 2))  # Output: 12

"classmethod"
# class School:
#     name = "Greenwood High"  # Class variable

#     @classmethod
#     def change_school_name(cls, new_name):
#         cls.name = new_name  # Modifies class variable

# print(School.name)  # Output: Greenwood High

# School.change_school_name("Sunrise Academy")  # Calling class method
# print(School.name)  # Output: Sunrise Academy

"__call__"

# class Multiplier:
#     def __init__(self, factor):
#         self.factor = factor
    
#     def __call__(self, num):
#         return self.factor * num

# double = Multiplier(2)
# print(double(5))  # Output: 10

"__eq__ , __lt__"

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height  # Calculate area

#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() == other.area()
#         return False  # If not a Rectangle, return False

#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() < other.area()
#         return False  # If not a Rectangle, return False

# # Creating rectangle objects
# r1 = Rectangle(4, 5)  # Area = 20
# r2 = Rectangle(2, 10) # Area = 20
# r3 = Rectangle(3, 6)  # Area = 18

# # Testing __eq__ (==)
# print(r1 == r2)  # True (same area)

# # Testing __lt__ (<)
# print(r3 < r1)   # True (18 < 20)
# print(r1 < r2)   # False (both have area 20)

"__iter__"

# class NumberList:
#     def __init__(self, numbers):
#         self.numbers = numbers

#     def __iter__(self):
#         return iter(self.numbers)  # Return an iterator for the list

# # Creating a NumberList object
# numbers = NumberList([1, 2, 3, 4])

# # Using a for loop to iterate over the object
# for num in numbers:
#     print(num)

"__del__"
# class TemporaryFile:
#     def __init__(self, filename):
#         self.filename = filename
#         print(f"File '{self.filename}' created.")

#     def __del__(self):
#         print(f"File '{self.filename}' deleted!")

# # Creating and deleting a TemporaryFile object
# temp = TemporaryFile("temp.txt")
# del temp  # Explicitly deleting the object to trigger __del__


"os"

# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")
    
"shutil"

# import shutil
# import os

# # shutil.copy("main.py", "main2.py")
# # shutil.copytree(".tutorial", "mytutorial")
# # shutil.move(".tutorial/file.file", "file.file")
# # shutil.rmtree("mytutorial")
# os.remove("file.file")


" decorators"
# def my_decorator(func):
#     def wrapper():
#         print("Function is being called")
#         func()  # Call the original function
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello, world!")

# greet()


"Method Overriding (Runtime Polymorphism)"

# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Bark"

# class Cat(Animal):
#     def speak(self):
#         return "Meow"

# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.speak())  # Calls the overridden method


"Method Overloading (Not Natively Supported)"

# class MathOperations:
#     def add(self, a, b=0, c=0):
#         return a + b + c

# math_obj = MathOperations()
# print(math_obj.add(2))       # 2
# print(math_obj.add(2, 3))    # 5
# print(math_obj.add(2, 3, 4)) # 9

"operator overloading"

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2  # Calls __add__ method
# print(p3)     # Output: (4, 6)


"Duck Typing"

# class Dog:
#     def speak(self):
#         return "Bark"

# class Human:
#     def speak(self):
#         return "Hello"

# def make_sound(entity):
#     print(entity.speak())

# make_sound(Dog())   # Output: Bark
# make_sound(Human()) # Output: Hello
