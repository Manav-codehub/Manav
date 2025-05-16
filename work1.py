# # section 1 -:Core Python Concepts

# # answer 1 
# #  docstring is like a comment but it arrive just after function or any class to define something 
# def doc_string(x):
#     '''here is a docstring '''
#     y=x+5
#     return y
# print(doc_string(5))

# # answer 2 
# def factorial(x):
#     if(x==0 or x==1):
#         return 1
#     else:
#         return x * factorial(x-1)
# print(factorial(5))

# # answer 3
# # lambda fuction is used in programming to avoid writing  big code basically lambda function is used to code in small syntax 
# def lambda_use(x):
#     y=x*x
#     return y
# square=lambda x:x*2
# print(lambda_use(5))
# print(square(3))

# # Section 2: Object-Oriented Programming (OOPs)
# # answer 4
# class employee:
    
#     def __init__(self,n,i,w):
#         self.name=n
#         self.id=i
#         self.work=w

#     def show(self):
#         print(f"The name of employyee is {self.name} and his id {self.id} and he is {self.work}")

# class single(employee):
#     def __init__(self,n,i,w):
#         self.name=n
#         self.id=i
#         self.work=w

#     def show1(self):
#         print(f"The name of employyee is {self.name} and his id {self.id} and he is {self.work}")

# e=employee("manav sharma ",565656,"data scientist")
# s=single("yashnit",454545,"CA")
# s2=single("manav sharma ",565656,"data scientist")
# # e.show()
# s.show()
# s2.show1()

# # answer 5
# class A:
#     def show(self):
#         print("this is a A class")

# class B:
#     def show1(self):
#         print("this is a B class")

# class C:
#     def show2(self):
#         print("this is a C  class")

# class D(A,B,C):
#     def show3(self):
#         print("this is a D class")

# d=D()
# d.show()
# d.show1()
# d.show2()
# d.show3()

# # answer 6 
# class dog:
#     def dog_bark(self):
#         print("bark")
        
# class cat(dog):
#     def cat_meow(self):
#         print("meow")
        
# class cow(cat):
#     def cow_moos(self):
#         print("moos")
        
# class lion(cow):
#     def lion_roar(self):
#         print("roar")

# d=dog()
# c=cat()
# c1=cow()
# l=lion()
# d.dog_bark()
# c.cat_meow()
# c1.cow_moos()
# l.lion_roar()

# # answer 7 

# class A:
#     def show(self):
#         print("this is A class")

# class B(A):
#     def show1(self):
#         print("this is B class")

# class C(A):
#     def show2(self):
#         print("this is  C class")

# class D(B,C):
#     def show3(self):
#         print("this is D class")

# a=A()
# b=B()
# c=C()
# d=D()
# a.show()
# b.show()
# b.show1()
# c.show()
# c.show2()
# d.show()
# d.show1()
# d.show2()
# d.show3()

# # answer 8
# class Father:
#     def show(self):
#         print("father class")

# class Son(Father):
#     def show1(self):
#         print("son class")

    
# class Daughter(Father):
#     def show2(self):
#         print("daughter class")

# f=Father()
# s=Son()
# d=Daughter()
# s.show()
# s.show1()
# d.show()
# d.show2()

# # Section 3: Concurrency in Python

# # answer 9 = multithreading and multiprocessing is almost same in, but the minor difference is multithreading is light weight and multiprocessing is heavy weight

# # answer 10

# import time
# import threading
# from concurrent.futures import ThreadPoolExecutor


# def function1(second):
#     time.sleep(second)
#     print("Function 1 sleeps for ",second)
#     return second

# t1=threading.Thread(target=function1,args=[2])
# t2=threading.Thread(target=function1,args=[4])
# t3=threading.Thread(target=function1,args=[6])

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# with ThreadPoolExecutor() as execuor:
#     f1=execuor.submit(function1,2)
#     f2=execuor.submit(function1,4)
#     f3=execuor.submit(function1,6)
# print(f1.result())
# print(f2.result())
# print(f3.result())

# x=[2,3,4,5,6,7]
# x1=execuor.map(function1,x)
# for i in x1:
#    print(i)

# # answer 11
# import multiprocessing
# import multiprocessing.process

# def square(n):
#     print(f"square of {n} is {n*n}")

# if __name__=="__main__":
#     numbers=[1,2,3,4,5]
#     output=[]
#     for j in numbers:
#      p1=multiprocessing.Process(target=square,args=[j],)
#      output.append(p1)
#      p1.start()

#     for i in output:
#         i.join()

# # answer 12 
# import asyncio
# import time 
# async def sol():
#  for i in range(1,6):
#     time.sleep(1)
#     print(i)
# asyncio.run(sol())

# # Section 4: Python Libraries (NumPy, Pandas, Matplotlib, Seaborn)

# # answer 13 
# import numpy as np
# x=np.array([[1,2,3],[4,5,6]])
# print(x)
# print(x.shape)
# print(x.size)

# # answer 14
# x=np.linspace(3,30,9)
# x1=np.matrix(x)
# print(x1)
# print(x1.reshape(3,3))

# # answer 15
# import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Age': [25, 30, 35, 40],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }
# df = pd.DataFrame(data)
# print(df)
# df.filter(axis="columns")
# print(df)

# # answer 16
# import pandas as pd 
# data1data1 = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Isla', 'Jack'],
#     'Age': [25, 30, 35, 40, 28, 33, 38, 43, 26, 31],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
#     'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Chef', 'Teacher', 'Nurse', 'Musician', 'Architect', 'Scientist']
# }
# df = pd.DataFrame(data1data1)
# print(df)
# df.to_csv("data1data1.csv",index= False)
# y=pd.read_csv("C:\\Users\\Manav\\Downloads\\data1data1.csv")
# print(y)

# # answer 17
# import seaborn as sb
# import matplotlib.pyplot as plt 
# x=sb.load_dataset("iris")
# print(x)
# y=sb.histplot(x)
# print(y)
# plt.show()


# # answer 18
# import matplotlib.pyplot as plt 
# import pandas as pd
# data = {
#     'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
#     'Sales': [25000, 27000, 30000, 32000, 35000, 40000, 42000, 45000, 47000, 50000]
# }
# df = pd.DataFrame(data)
# print(df)
# plt.plot(df)
# plt.xlabel("year")
# plt.ylabel("sales")
# plt.title("analysis")
# plt.show()

# # Section 5: Statistical Concepts (Central Tendency, Dispersion, Percentile, Quartile, IQR, Lower & Upper Fence)

# # answer 19
# import numpy as np
# import statistics as s 
# test_scores = [85, 78, 92, 88, 76, 90, 83, 87, 75, 80, 79, 94, 82, 81, 84, 91, 77, 86, 89, 93]
# x=np.mean(test_scores)
# y=np.median(test_scores)
# z=s.mode(test_scores)
# print(x)
# print(y)
# print(z)
# # mean is the sum of all number in dataset divided by all number of dataset
# # median is the best way to find outlier 
# # mode is the most frequent element

# # answer 20 
# # measure of dispertion has two type varience and standard deviation 
# import numpy as np 
# test_scores = [85, 78, 92, 88, 76, 90, 83, 87, 75, 80, 79, 94, 82, 81, 84, 91, 77, 86, 89, 93]
# x=np.std(test_scores)
# y=np.var(test_scores)
# print(x)
# print(y)

# # answer 21
# import numpy as np 
# test_scores = [85, 78, 92, 88, 76, 90, 83, 87, 75, 80, 79, 94, 82, 81, 84, 91, 77, 86, 89, 93]
# list=[25,50,75]
# x=np.percentile(test_scores,list[0])
# y=np.percentile(test_scores,list[1])
# z=np.percentile(test_scores,list[2])
# print(x)
# print(y)
# print(z)

# # answer 22
# import numpy as np 
# test_scores = [85, 78, 92, 88, 76, 90, 83, 87, 75, 80, 79, 94, 82, 81, 84, 91, 77, 86, 89, 93]
# q1=25
# q3=75
# x=np.percentile(test_scores,q1)
# y=np.percentile(test_scores,q3)
# print(x)
# print(y)
# IQR=q3-q1
# print(IQR)

# # answer 23
# import numpy as np 
# # logic
# # first we have to sort this data 
# # secound is q1 qnd q3 
# # third iqr 
# # fourth lower fence and upper fence 

# heights = [160, 162, 164, 161, 163, 165, 159, 161, 162, 160, 164, 161, 200, 163, 162]
# x=np.sort(heights)
# print(x)
# q1=25
# q3=75

# x1=np.percentile(heights,q1)
# x2=np.percentile(heights,q3)
# print(x1)
# print(x2)
# IQR=x2-x1
# print(IQR)

# lower_fence=x1-1.5*IQR
# upper_fence=x2+1.5*IQR
# print(lower_fence)
# print(upper_fence)
# # so 200 is a outlier  

# # Bonus Section: Miscellaneous Questions

# # answer 24
# # i dont know 

# # answer 25 
# # time module is ised to do any time related function with programm 
# # for example here we are comparing for loop and while loop 
# import time 
# t1=time.perf_counter()
# def for_loop():
#     for i in range (100000000):
#         if(i<=1000000000):
#             i=i+1
#             print(i)
# t2=time.perf_counter()
# print(t2-t1)

# t3=time.perf_counter()
# def while_loop():
#     j=0
#     while(j<=1000000000):
#         print(j)
#         j=j+1
# t4=time.perf_counter()
# print(t4-t3)

# import pandas as pd
# data = {
#     "Name": ["John Doe", "Jane Smith", None, "Chris Lee", "Patricia Brown"],
#     "Age": [30, None, 35, 28, None],
#     "Salary": [75000, 68000, None, 70000, 72000]
# }
# df = pd.DataFrame(data)
# df.to_csv("employee_info_with_none.csv", index=False)
# print(df)


# password = "!@#$%^&*()A B C D E F G H I J K L M N O P Q R S T U V W X Y Za b c d e f g h i j k l m n o p q r s t u v w x y z"  # Set your password here

# entered_password = input("Enter the password: ")

# if entered_password == password:
#     print("Access granted. Running the code...")
#     # Your main code goes here
#     print("Hello, you have successfully entered the correct password!")
# else:
#     print("Access denied. Incorrect password.")

"answer 1 "
# import pandas as pd

# employees = [
#     {
#         "EmployeeID": 101,
#         "Name": "Alice",
#         "Department": "IT",
#         "Salary": 75000,
#         "Join_Date": 2018-6-15,
#         "Performance_Score": 85,
#         "Bonus (%)": 10
#     },
#     {
#         "EmployeeID": 102,
#         "Name": "Bob",
#         "Department": "HR",
#         "Salary": 65000,
#         "Join_Date": 2020-7-20,
#         "Performance_Score": 78,
#         "Bonus (%)": 8
#     },
#     {
#         "EmployeeID": 103,
#         "Name": "Charlie",
#         "Department": "Finance",
#         "Salary": 80000,
#         "Join_Date": 2017-9-10,
#         "Performance_Score": 92,
#         "Bonus (%)": 12
#     },
#     {
#         "EmployeeID": 104,
#         "Name": "David",
#         "Department": "IT",
#         "Salary": 72000,
#         "Join_Date": 2021-3-5,
#         "Performance_Score": 88,
#         "Bonus (%)": 11
#     },
#     {
#         "EmployeeID": 105,
#         "Name": "Emma",
#         "Department": "HR",
#         "Salary": 68000,
#         "Join_Date": 2019-11-25,
#         "Performance_Score": 90,
#         "Bonus (%)": 9
#     }
# ]
# # converting to dataframe

# a=pd.DataFrame(employees)
# print(a)

# # saving to csv 

# a.to_csv("employee.csv")
# b=pd.read_csv("employee.csv")
# print(b)

# # Create a new column "Bonus_Amount"

# a["Bonus_Amount"]=a["Salary"]*a["Bonus (%)"]/100
# print(a)

# # the employee with the highest total compensation (Salary + Bonus_Amount).
# a["employee_highest total compensation"]=a["Salary"]+a["Bonus_Amount"]
# print(a)

# # average salary per department.
# a["Average"]=a["Salary"].mean()
# print(a)


# # 
# a["Performance_Score"]=a["Performance_Score"].sort_values(ascending=False)
# print(a)

# # employees who joined before 

# a(["Join_Date"]<=2020-7-20)
# a.any()
# print(a)

# # 

# a["Experience_Level"]
# if(a["Experience_Level"]>2018-6-15):
#     print("senior")
# elif(a["Experience_Level"]>2018-6-15 and a["Experience_Level"]<2020-7-20):
#     print("mid-level")
# elif(a["Experience_Level"]<2020-7-20):
#     print("junior")
# else:
#     print("not found")


