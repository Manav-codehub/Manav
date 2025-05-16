# x=int(int(input("enter the value of x")))
# if x%2==0:
#     print("True")
# else:
#     print("False")

# def find_even_odd(cx=int(input("enter the cx"))):
#     if cx%2==0:
#         print("cx is even ")
#     else:
#         print("cx is odd")
# find_even_odd()

# def factorial(x):
#     if (x==0 or x==1):
#         return 1
#     else:
#         return x * factorial(x-1)
# print(factorial(6))

# a=['s','t','r','i','n','g']
# a.reverse()
# print(a)

# list=[1,2,3,4,5,6,7,8,9,10]
# list2=[]
# for number in list:
#     if number %2==0:
#         print(number*2)
#     list.append(list2)
#     print(list2)

# def double(x):
#     x*2
# lt=[5]
# double=list(map(lambda x=5:x*x,lt))
# print(double)

# import time #type:ignore

# def hello():
#     time.sleep(10)
#     print("hello")

# hello()

# class A:
#     def __init__(self,Nam1,sl1):
#         self.name=Nam1
#         self.salary=sl1
    
#     def show(self):
#         print(f"the name of employee is {self.name} and he earns {self.salary}")

# class B(A):
#     pass

# a=A("manav",1000000)
# b=B("yuvi",5000000)
# print(a.show())
# print(b.show())

# def greet(x):
#     def y():
#         print("start")
#         x()
#         print("end")
#     return y
# @greet
# def hello():
#     print("mid")

# hello()


# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def function(second):
#     time.sleep(second)
#     print(f"sleep for {second} second")

# def demo():
#   time1=time.perf_counter()
#   function(5)
#   function(6)
#   function(7)
#   time2=time.perf_counter()
#   print(time2-time1)

#   time1=time.perf_counter()
#   t1=threading.Thread(target=function,args=[5])
#   t2=threading.Thread(target=function,args=[6])
#   t3=threading.Thread(target=function,args=[7])

#   t1.start()
#   t2.start()
#   t3.start()

#   t1.join()
#   t2.join()
#   t3.join()
#   time2=time.perf_counter()
#   print(time2-time1)

# with ThreadPoolExecutor() as executor:
#     future1 = executor.submit(function,3)
#     future2 = executor.submit(function,6)
#     future3 = executor.submit(function,9)
    
#     print(future1.result())
#     print(future2.result())
#     print(future3.result())

#     x=[2,3,4,5,6]
#     results=executor.map(function,x)
#     for result in results:
#         print(result) 


# class Bank_account:
#     balance=0.0
#     def __init__(self,ahn,an,bal,bal2,an2):
#         self.account_holder_name=ahn
#         self.account_number=an
#         self.balance=float(bal)
#         self.balance2=float(bal2)
#         self.account_number2=an2

#     def show(self):
#         print(f"The name of account holder is {self.account_holder_name} and his account number is {self.account_number} with {self.balance} balance")
    
#     def deposit(self):
#         print(f"the deposit amount is {self.balance+self.balance2}")

#     def withdraw(self):
#         print(f"you withdraw {self.balance-self.balance2} ")
    
#     def current(self):
#         print(f"the current balance is {self.balance-self.balance2} ")

#     def transfer(self):
#         print(f"you are tranfer is ammont {self.balance} to {self.account_number2}")
    

# class Bank_account2(Bank_account):
#     pass

# b1=Bank_account("manav",177090870,100.0,50.0,177908223)
# b1.show()
# b1.deposit()
# b1.withdraw()
# b1.current()
# b1.transfer()
# b2=Bank_account2("yuvi",789067578,500.0,100.0,475585875)
# b2.show()
# b2.deposit()
# b2.withdraw()
# b2.current()
# b2.transfer()


# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def show(self):
#         return self.x * self.y
    
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#         super().__init__(radius,radius)
#     def area(self):
#       return 3.14 * super().show()
    
# # rec=shape(6,6)
# # print(rec.show())

# c=circle(5)
# print(c.show())


# p1=point(1,2)
# p2=point(3,4)
# print(p1+p2)


class employee:
    def __init__(self,n,s,r):
        self.name=n
        self.salary=s
        self.role=r

    def show(self):
        print(f"the name of employee is {self.name} and he takes {self.salary} for {self.role} role")

    def __add__(self,x):
        return self.salary+x.salary




e1=employee("manav",500000,"data scientist")
e2=employee("manav",1500000,"senior data scientist")
e1.show()
e2.show()
print(e1+e2)
