"1"
# class student:
#     def __init__(self,n,m,r):
#         self.name=n
#         self.roll_number=r
#         self.marks=m
        
    
#     def result(self):
#         self.marks
#         if 90<  self.marks <=100 :
#             print("A1 grade")
#         elif 80<  self.marks <=90 :
#             print("A2 grade")
#         elif 70<  self.marks <=80 :
#             print("B1 grade")
#         elif 60<  self.marks <=70 :
#             print("B2 grade")
#         elif 50<  self.marks <=60 :
#             print("C1grade")
#         elif 40<  self.marks <=50 :
#             print("C2 grade")
#         elif 30< self.marks <=40:
#             print("FAIL")
    
#     def detail(self):
#         grade=self.result()
#         print(f"The student {self.name} whose roll number {self.roll_number} got {grade}")

# s=student("manav",79,672873676)
# print(s.detail())
# print(s.result())


"2"

# class BankAccount:
#     """
#     A class to represent a bank account with methods to deposit, withdraw,
#     and check balance. Includes exception handling for invalid operations.
#     """

#     def _init_(self, initial_balance=0):
#         """
#         Initialize the BankAccount with an initial balance.
#         """
#         if initial_balance < 0:
#             raise ValueError("Initial balance cannot be negative.")
#         self.balance = initial_balance

#     def deposit(self, amount):
#         """
#         Deposit a specified amount into the account.
#         """
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive.")
#         self.balance += amount
#         print(f"Deposited: {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         """
#         Withdraw a specified amount from the account.
#         """
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive.")
#         if amount > self.balance:
#             raise ValueError("Insufficient funds.")
#         self.balance -= amount
#         print(f"Withdrawn: {amount}. Remaining balance: {self.balance}")

#     def check_balance(self):
#         """
#         Display the current balance of the account.
#         """
#         print(f"Current balance: {self.balance}")


# # Example usage
# try:
#     account = BankAccount(500)  # Initialize with a balance of 500
#     account.deposit(400)        # Deposit 400
#     account.withdraw(200)       # Withdraw 200
#     account.check_balance()     # Check balance
#     account.withdraw(1000)      # Attempt to withdraw more than balance (to test error handling)
# except ValueError as e:
#     print(f"Error: {e}")


"3"
# class Car:
#     """
#     A class to represent a car with attributes for brand, model, and year.
#     Includes methods to start the car and display its details.
#     """

#     def __init__(self, brand, model, year):
#         """
#         Initialize the Car with brand, model, and year attributes.
#         The car is initially off.
#         """
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.is_started = False

#     def display_details(self):
#         """
#         Display the details of the car.
#         """
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

#     def start_car(self):
#         """
#         Start the car if it is off; turn it off if it is already running.
#         """
#         if not self.is_started:
#             self.is_started = True
#             print("The car has started.")
#         else:
#             self.is_started = False
#             print("The car has been turned off.")


# # Example usage
# my_car = Car("Ferrari", "LaFerrari", 2013)
# my_car.display_details()  # Display the car details
# my_car.start_car()        # Start the car
# my_car.start_car()        # Turn off the car
"4"

# class encapsulation:
#     def __init__(self,n,a):
#         self.__name=n
#         self.__age=a

    
#     def show(self):
#         print(f"the name of person is {self._name} and his age is {self._age}")

# e=encapsulation("manav",100)
# e.show()

"5"

import pandas as pd
sales_data = {
    "sales": [
        {"Product": "Laptop", "Price": 700, "Quantity": 10},
        {"Product": "Headphones", "Price": 50, "Quantity": 30},
        {"Product": "Keyboard", "Price": 20, "Quantity": 15},
        {"Product": "Mouse", "Price": 25, "Quantity": 40},
        {"Product": "Monitor", "Price": 150, "Quantity": 12}
    ]
}
x=pd.DataFrame(sales_data)
print(x)
x.to_csv("hello3.csv")

y=pd.read_csv("C:\\Users\\Manav\\Downloads\\python\hello3.csv",nrows='Price')>100
print(y)
