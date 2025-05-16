class mymeta(type):
    def __new__(cls,name,bases,attrs):
        uppercase_attrs={}
        for key,value in attrs.items():
            if callable(value):
                uppercase_attrs[key.upper()]=value

            else:
                uppercase_attrs[key]=value
        return super().__new__(cls,name,bases,uppercase_attrs)
    
class name(metaclass=mymeta):
    def hello1(self):
        return "hello friend"
        
    def hello2(self):
        return "hello world "
    
n=name()

print(n.HELLO1())
print(n.HELLO2())

try:
    print(n.hello())  
except AttributeError as e:
    print(f"Error: {e}")  





# Define the metaclass that converts all method names to uppercase
# class UpperCaseMethodsMeta(type):
#     def __new__(cls, name, bases, attrs):
#         # Create a new dictionary to hold the updated methods
#         uppercase_attrs = {}
        
#         for key, value in attrs.items():
#             # Check if the attribute is a method (i.e., callable)
#             if callable(value):
#                 # Rename the method to be uppercase
#                 uppercase_attrs[key.upper()] = value
#             else:
#                 # Keep other attributes unchanged
#                 uppercase_attrs[key] = value
        
#         # Create the class with the modified attributes
#         return super().__new__(cls, name, bases, uppercase_attrs)

# # Create a class using the metaclass
# class MyClass(metaclass=UpperCaseMethodsMeta):
#     def greet(self):
#         return "Hello, World!"

#     def say_goodbye(self):
#         return "Goodbye, World!"

# # Test the class
# obj = MyClass()

# # Verify that the method names are now uppercase
# print(obj.GREET())        # Output: Hello, World!
# print(obj.SAY_GOODBYE())  # Output: Goodbye, World!

# # Check that accessing the methods with lowercase names will raise an error
# try:
#     print(obj.greet())  # This will raise an AttributeError
# except AttributeError as e:
#     print(f"Error: {e}")  # Output: Error: 'MyClass' object has no attribute 'greet'
