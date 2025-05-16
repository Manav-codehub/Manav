"fibonacci"
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))

"2"
# def docstring(x):
#     '''hii! i am inside docstring'''
#     return x*2
# print(docstring(2))
# print(docstring.__doc__)

"3"

# class A:
#     '''here i am with multiple parameter'''
#     def __init__(self):
#         self.name="john"
#         self.age=79

# a=A()
# print(a.name)
# print(a.age)
# print(a.__doc__)

"4"
# class vector:
#     '''docstring under a class'''
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c

#     def show(self):
#         '''docstring under show method'''
#         print(f"{self.a}a \n {self.b}b \n{self.c}c")

# v=vector(2,4,6)
# v.show()
# print(vector.__doc__)
# print(v.show.__doc__)

"5"
# import csv

# def sum_column(csv_filename, column_name):
#     total = 0
#     try:
#         with open(csv_filename, mode='r') as file:
#             csv_reader = csv.DictReader(file)
#             for row in csv_reader:
#                 # Convert the column value to float and add to total
#                 total += float(row[column_name])
#     except FileNotFoundError:
#         print(f"Error: The file '{csv_filename}' does not exist.")
#     except KeyError:
#         print(f"Error: Column '{column_name}' not found in CSV file.")
#     except ValueError:
#         print("Error: Some values in the column are not numeric.")
#     else:
#         print(f"The sum of the '{column_name}' column is: {total}")

# # Example usage
# csv_filename = "data.csv"
# column_name = "Amount"  # Replace with the actual column name you want to sum
# sum_column(csv_filename, column_name)

"6"
# import shutil  # This module is used for file operations like copying

# # Read and print the contents of the original file
# with open("JSON.txt", "r") as f:
#     print(f.read())

# # Copy the original file to a new file
# shutil.copy("JSON.txt", "JSON_copy.txt")

# # Read and print the contents of the copied file
# with open("JSON_copy.txt", "r") as g:
#     print(g.read())

"7"
# class bankaccount:
#     def __init__(self,blc):
#         self.balance=blc

#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"deposit amount{amount},current balance{self.balance}")

#     def withdraw(self,amount):
#         if self.balance>=amount:
#          self.balance-=amount
#          print(f"withdraw amount{amount},current amount{self.balance}")
#         else:
#            print(f"insufficient balance ! current balance{self.balance}")

# b=bankaccount(1000)
# b.deposit(500)
# b.withdraw(400)


    

"8"
# class employee:
#     def __init__(self,n,r):
#         self.name=n
#         self.role=r

# class manager(employee):
#     def show1(self):
#         print(f"name of developer is {self.name} and his role is {self.role}")

# class developer(employee):
#     def show2(self):
#         print(f"name of manager is {self.name} and his role is {self.role}")

# e=employee("manav","data scientist")
# m=manager("manav","data scientist")
# m.show1()
# d=developer("manav1","data scientist1")
# d.show2()

"9"
# class public:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a

# class protected:
#     def __init__(self,n1,a1):
#         self.__name=n1
#         self.__age=a1

# p=public("manav",78)
# print(p.name)
# print(p.age)

# p=protected("manav1",75478)
# print(p.__name)
# print(p.__age)


"10"
# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
        
# class circle(shape):
#     def area(self,radius):
#         self.radius=radius
#         super().__init__(radius,radius)
#     def show(self):
#         return 3.14 * self.radius+self.radius

# class rectangle(shape):
#     def area(self,length,weidth):
#         self.length=length
#         self.weidth=weidth
#         super().__init__(length,weidth)
#     def show2(self):
#         return self.length+self.weidth

# s=shape(6,6)  

# c=circle(5,7)
# c.show()

# r=rectangle(5,5)
# r.show2()

"11"

# class A:
#     def show(self):
#      return "hello"

# class B:
#     def show2(self):
#      return "hello1"


# class C(A,B):
#     def show3(self):
#      return "hello2"

# a=A()
# print(a.show())
# b=B()
# print(b.show2())
# c=C()
# print(c.show())
# print(c.show2())
# print(c.show3())
# print(C.mro())

"12"
# class mymeta(object):
#     def __new__(name,base,getattr):
#         super().__new__(name,base,getattr)

# class world(metaclass=mymeta):
#     def show(self):
#         print("class is being created ")

# w=world()
# w.show()


# import asyncio

# async def function1():
#     await asyncio.sleep(3)
#     print("function 1")

# async def function2():
#     await asyncio.sleep(4)
#     print("function2")

# async def function3():
#     await asyncio.sleep(5)
#     print("function3")

# async def main():
#    x=asyncio.create_task(function1())
# #    await function1()
#    await function2()
#    await function3()
   

# asyncio.run(main())


# import asyncio
# import requests

# async def function1():
#     async  def DownloadFile(url):
#      await asyncio.sleep(5)
#      url="https://www.bing.com/images/search?view=detailV2&ccid=pzQ2E2Kx&id=6F172D670E9ACBE67D8051B3B2DDE267EDB9C88D&thid=OIP.pzQ2E2KxjUjzhh9YMn7ZrAHaD3&mediaurl=https%3A%2F%2Fcloudinary-marketing-res.cloudinary.com%2Fimages%2Fw_1000%2Cc_scale%2Fv1679921049%2FImage_URL_header%2FImage_URL_header-png%3F_i%3DAA&exph=523&expw=1000&q=iamge+url&simid=608030111484181084&FORM=IRPRST&ck=A382869578E5F73E9341A5698692C853&selectedIndex=9&itb=1&cw=1339&ch=664&ajaxhist=0&ajaxserp=0"
#      local_filename = url.split('/')[-1]
#      r = requests.get(url)
#      f = open(local_filename, 'wb')
#      for chunk in r.iter_content(chunk_size=512 * 1024): 
#         if chunk: 
#             f.write(chunk)
#      f.close()
#      return DownloadFile

# async def function2():
#   async def DownloadFile1(url):
#      await asyncio.sleep(6)
#      url="https://www.bing.com/images/search?view=detailV2&ccid=9CLjGOB5&id=EE3F4BBCF5DBF50B01B555E8633B56B1DDFD468B&thid=OIP.9CLjGOB5KM36PeF371DAugHaFW&mediaurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fz%2Fd-illustration-computer-keyboard-script-short-url-two-adjacent-green-buttons-short-url-concept-109798448.jpg&exph=1157&expw=1600&q=iamge+url&simid=608044448059560474&FORM=IRPRST&ck=4F53B3A3135560BDBE290D43EE137FA8&selectedIndex=20&itb=0&cw=1339&ch=664&ajaxhist=0&ajaxserp=0"
#      local_filename = url.split('/')[-1]
#      r = requests.get(url)
#      f = open(local_filename, 'wb')
#      for chunk in r.iter_content(chunk_size=512 * 1024): 
#         if chunk: 
#             f.write(chunk)
#      f.close()
#      return DownloadFile1


# async def hello1():
#    await function1()
#    await function2()

# asyncio.run(hello1())

# import asyncio
# async def function1():
#     print("function1")
#     if asyncio.sleep()>3:
#         raise TimeoutError
#     else:
#         print(asyncio.sleep(3))
    


# async def hello():
#    await function1()

# asyncio.run(hello())

import threading
import time 
from concurrent.futures import ThreadPoolExecutor 

def function1(second):
    print(f"sleeep for {second}")
    time.sleep(second)

def function2(second):
    print(f"sleeep for {second}")
    time.sleep(second)

def function3(second):
    print(f"sleeep for {second}")
    time.sleep(second)
def main():
  time1=time.perf_counter()
  function1(2)
  function2(4)
  function3(6)
  time2=time.perf_counter()
  print(time2-time1)

  t1=threading.Thread(target=function1,args=[2])
  t2=threading.Thread(target=function2,args=[4])
  t3=threading.Thread(target=function3,args=[6])

  time3=time.perf_counter()
  t1.start()
  t2.start()
  t3.start()

  t1.join()
  t2.join()
  t3.join()
  time4=time.perf_counter()

  print(time4-time3)

def case1():
    with ThreadPoolExecutor() as executor:
        future1=executor.submit(function1,2)
        print(future1.result())

    with ThreadPoolExecutor() as executor:
        future2=executor.submit(function1,2)
        print(future2.result())


    with ThreadPoolExecutor() as executor:
        future3=executor.submit(function1,2)
        print(future3.result())

def case2():
    with ThreadPoolExecutor() as executor:
        l=[10,20,30,40,50]
        result1=executor.map(function1,l)
        result2=executor.map(function2,l)
        result3=executor.map(function3,l)
        
        for i in result1:
            print(i)
        for j in result2:
            print(j)
        for k in result3:
            print(k)

case1()
case2()


