# def factorial(x):
#     if(x==0 or x==1):
#      return 1
#     else:
#        return x *factorial(x-1)
# print(factorial(5))



# def docstring (x):
#     '''hlo i am inside in doc'''
#     print(x**5)
# docstring(5)
# print(docstring.__doc__)


# x=int(input("enter the number->"))
# if(x < 0):
#     print("number is negative")
# elif(x > 0):
#     if(x <=10):
#         print("numbner is between 0-10")
#     elif(x > 10):
#         if(x <= 20):
#             print("number is between 10-20")
#         elif(x > 20):
#             if(x<=25):
#                 print("number is between 20-25")
#             else:
#                 print("number is greater than 25")




# for i in range(0,11):
#      if(i==5):
#         print(i)
#         continue
# print("skip the loop")

# for i in range(0,11):
#     if(i==6):
#         continue
#     print(i)

# x=int(input("enter the number-:"))
# match x:
#     case 0:
#         print("x is zero")
#     case 6:
#         print("x is 6")
#     case _ if  x == 90:
#         print("x is 90")
#     case _ if x == 80 :
#         print("x is 80")
#     case _ :
#         print("x does not match")



# def five(x):
#     return x*(5)
# print(five(5))



# def hello(func,x,y):
#     return 2 * func(x,y)+y


# print(hello(lambda x,y:x*y,6,8))



# def hello(func, x, y):
#     return 2 * func(x, y) + y

# print(hello(lambda x, y: x * y, 6, 8))


# def cube(b):
#     return b*b*b
# print(cube(3))

# x=[1,2,3,4,5]
# newx=[]
# for i in x:
#     newx.append(cube(i))
# print(newx)


# newx=list(map(lambda y:y*y*y,x))
# print(newx)

# def f_f (a):
#     return a>2

# newnewx=list(filter(f_f,x))
# print(newnewx)

# from functools import reduce
# x=[6,8,9,4,12]
# y=reduce(lambda a,b:a+b,x)
# print(y)


# class A:
#     name="manav"
#     age=19
#     occupation="Data scientist"
#     def info(self):
#        print(f"{self.name} is a {self.occupation}")

# x=A()
# class B:
#     name="yashnit"
#     age=17
#     occupation="CA"
#     def info(self):
#        print(f"{self.name} is a {self.occupation}")

# y=B()
# class C:
#     name="yashraj"
#     age=18
#     occupation="iitian"
#     def info(self):
#        print(f"{self.name} is a {self.occupation}")

# z=C()


# x.info()
# y.info()
# z.info()



# class person:
#     def __init__(self,n,w):
#         self.name=n
#         self.work=w

#     def info(self):
#         print(f"{self.name} is a {self.work}")
# a=person("manav","data scientist")
# a.info()
# b=person("yuvi","CA")
# b.info()

# class person:
#     name="manav"
#     age=19
#     work="data scientist"
#     def info(self):
#         print(f"{self.name} is a {self.work}")
# a=person()
# a.info()


# import os 
# if(not os . path . exists("data")):
#  os.mkdir("data")
# for i in range(0,1000000000000):
#     os.makedirs(f"data/format{i+1}")


# class A:
#     name="manav"
#     age=19
#     work="data scientist"
#     def info(self):
#         print(f"{self.name} is a {self.work}")
# x=A()
# x.info()

# class mahadev:
#     def __init__(self,n,w):
#        self.name=n
#        self.work=w
#     def info(self):
#         print(f"{self.name} is a {self.work}")
# a=mahadev("manav","data scientist")
# a.info()

# def square(x):
#     return x*2
# print(square(5))
# x=[1,2,3,4,5,]
# xx=[]
# for i in x:
#  xx.append(square(i))
# print(xx)
# xx= list(map(lambda x: x*2,x))
# print(xx)

# def f_f(b):
#     return b>1

# xx=list(filter(f_f,x))
# print(xx)

# from functools import reduce
# x=[1,2,3,4,5,]
# xx=reduce(lambda a,b:a+b,x)
# print(xx)





# for i in range(0,5):
#     for x in  range(0,5):
#         print("*",end="")
#     print()



# r=6
# for i in range(1,r+1):
#     for x in range(1,i+1):
#         print("*",end="")
#     print()


# def greet(x):
#     def y():
#         print("work start")
#         x()
#         print("work end ")
#     return y
# @greet
# def hello1():
#     print("program at mid")
# hello1()




# with open ("comeoo.txt","r") as a :
#   while True :
#     b = a.readlines()
#     if not b :
#         break
#     print(b)

# with open ("comeoo.txt","r+") as a :
#  a.truncate(5)


# with open ("comeoo.txt","r") as a :
#  print(a.read())



    

# class A:
#     name="manav"
#     age=19
#     work="data scientist"
#     def info(self):
#         print(f"{self.name} is a {self.work}")
# x=A()
# x.info()

# class B:
#     name="tanuj"
#     age=19
#     work="doctor"
#     def info(self):
#         print(f"{self.name} is a {self.work}")
# y=B()
# y.info()
# class C:
#     name="yuvi"
#     age=19
#     work="CA"
#     def info(self):
#         print(f"{self.name} is a {self.work}")
# z=C()
# z.info()



# class Z:
#     def __init__(self,n,w):
#         self.name=n
#         self.work=w

#     def info(self):
#         print(f"{self.name} is a {self.work}")
# z=Z("manav","datas scientist")
# z.info()


# def factorial(x):
#     if(x==0 or x==1):
#      return 1
#     else:
#        return x * factorial(x-1)
# print(factorial(5))

# def cube(x):
#     return x>1
# print(cube(3))

# l=[1,2,3,4,5]
# newl=[]

# # newl=list(filter(cube,l))
# # print(newl)



# from functools import reduce
# x=[1,2,3,4,5]
# y=reduce(lambda a,b:a+b,x)
# print(y)

# def Greet(x):
#     def y():
#         print("start")
#         x()
#         print("end")
#     return y

# @Greet
# def hello():
#     print("mid")
# hello()
    

# class A:
#     def __init__(self,v):
#         self._value=v

#     def show(self):
#         print(f"value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10* self._value
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10
        
# x=A(10)
# x.ten_value=9
# print(x.ten_value)
# x.show()
    
# def greet (x):
#     def y():
#         print("start")
#         x()
#         print("end")
#     return y()
# @greet
# def hello1():
#     print("at mid")



# class A:
#     def __init__(self,v):
#         self._value=v

#     def show(self):
#         print(f"value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10* self._value
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10   
# x=A(10)
# x.ten_value=9
# print(x.ten_value)
# x.show()



# a=1
# b=2
# print("a") if a>b else  print("=") if a==b else print("b")

# list=[1,3,4,56,6,65,5544]

# index=0
# for list in list:
#     print(list)
#     if(index==5):
#         print("ohh you got it")



# class A:
#     def __init__(self,n,w):
#         self.name=n
#         self.work=w

#     def show (self):
#         print(f"The name of employee is {self.name} and his work is {self.work}")
# class B(A):
#     def show1(self):

#         print("hlo hy")
# x=B("manav","data scientist")
# x.show1()
# x.show()

# class A:
#     def __init__(self,n,i):
#         self.name=n
#         self.identity=i

#     def show (self):
#         print(f"the name of employee is {self.name} and his identity is {self.identity}")
# class B(A):
#     def show1(self,h,w):
#         self.his=h
#         self.work=w
#         print(f"employee name is {self.his} and his work {self.work}")
# x=B("manav","74793")
# x.show()
# x.show1("manav","data scientist")



# class A:
#     def __init__(self,v):
#         self._value=v

#     def show (self):
#         print(f"value is {self._value}")

#     @property
#     def ten_value (self):
#         return 10* self._value
#     @ten_value.setter
#     def ten_value (self,new_value):
#         self._value=new_value/10
# x=A(10)
# x.ten_value=9
# print(x.ten_value)
# x.show()



# class Employee:
#     def __init__(self):
#         self.__name="manav"
# e=Employee()
# print(e._Employee__name)


# class A:
#     def __init__(self):
#         self._name="manav"

#     def hello (self):
#         return "har har mahadev"
# class B(A):
#     pass 

# x1=A()
# x2=B()

# print(x1._name)
# print(x1.hello())
# print(x2._name)
# print(x2.hello())






# class A:
#     def __init__(self):
#         self.name = "manav"

# x=A()
# print(x._A__name)



# class A:
#     def __init__(self):
#         self._name="hy"
#     def show (self):
#             return "hlo"
# class B(A):
#      def show1(self):
#           pass
# x=A()
# y=B()
# print(x.show())
# print(x._name)
# print(y.show())
# print(y._name)


# class A:
#     def __init__(self,n,i):
#         self.name=n
#         self.identity=i

#     def hello(self):
#         print(f"the name of person is {self.name} and his id is {self.identity}")

# class B(A):
#         def hello1(self):
#            print("hlo")

# x=A("manav","74793")
# x.hello()
# x1=B("manav","data scientist")
# x1.hello1()
# x1.hello()



# class A:
#     def __init__(self,n,w):
#         self.name=n
#         self.work=w
#     def show(self):
#         print(f"The name of employee is {self.name} and his work is {self.work}")

# class B(A):
#     def show1(self,h,i):
#         self.his=h
#         self.id=i
#         print(f"The name of employee is {self.his} and his id is {self.id}")

# x=B("manav","data scientist")
# x.show()
# x.show1("manav","74793")




# class a:
#     def __init__(self,v):
#         self._value=v

#     def show (self):
#         print(f"value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10* self._value
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10
# x=a(10)
# x.ten_value=9
# print(x.ten_value)
# x.show()



# def Greet(x):
#     def y():
#         print("start")
#         x()
#         print("end")
#     return y


# @Greet
# def hello():
#     print("at mid ")
# hello()


# class math:
#     def __init__(self,n):
#         self.num=n
#     def addition(self,i):
#         self.num=self.num+i

#     @staticmethod
#     def add(a,b):
#         return a+b
# a=math(5)
# print(a.num)
# a.addition(5)
# print(a.num)


# import os 
# if( not os.path.exists("data")):
#  os. mkdir("data")
# for i in range(0,100):
#     os.mkdir(f"data/folder{i+1}")





# class employee:
#     def __init__(self,n):
#         self.name=n

#     def showinfo(self):
#         print(f"the name of employee is {self.name}")
# e=employee("mahakaal")
# e.showinfo()
# # employee.showinfo(e)



# class a:
#     def __init__(self,n):
#         self.name=n

#     def show(self):
#         print(f"The name of employee is {self.name}")
# x=a("mahakaal")
# x.show()
# a.show(x)


# class A:
#     def __init__(self,n):
#         self.num=n
#     def addition(self,i):
#         self.num=self.num+i
#     @staticmethod
#     def add (a,b):
#         return (a+b)
# x=A(7)
# print(x.num)
# x.addition(3)
# print(x.num)
    


# class A:
#     def __init__(self,n,w):
#         self.name=n
#         self.work=w
#     def show(self):
#         print(f"The name of employee  is {self.name} and he is {self.work}")
# class B(A):
#     def show1(self,h,i):
#         self.his=h
#         self.identity=i
#         print(f"The name of employee is {self.his} and his id is {self.identity}")
# x=B("manav","data scientist")
# x.show()
# x.show1("manav","74793")



# class A:
#     def __init__(self,v):
#         self._value=v
#     def show(self):
#         print(f"The value is {self._value}")
#     @property
#     def ten_value(self):
#         return 10* self._value
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10
# x=A(10)
# x.ten_value=9
# print(x.ten_value)
# x.show()


# class employee:
#     companyname="google"
#     numberofemployee=0
#     def __init__(self,n):
#         self.name=n
#         self.salaryhike=80
#         employee.numberofemployee +=1
#     def show(self):
#         print(f"The name of employee is {self.numberofemployee} {self.name} and salary hike is {self.salaryhike} in {self.companyname}")

# e1=employee("manav")
# e1.salaryhike=90
# e1.show()
# e2=employee("harsh")
# e2.companyname=("NASA")
# e2.show()




# class A:
#     company="NASA"
#     def show (self):
#         print(f"The name of employee is {self.name} and his company {self.company}")
#     @classmethod
#     def changecompany(cls,newcompany):
#             cls.company=newcompany

# x=A()
# x.name=("manav")
# x.show()
# x.company="google"
# x.show()
# print(x.company)


# class A:
#     company = "NASA"
    
#     def show(self):
#         print(f"The name of employee is {self.name} and his company is {self.company}")
    
#     @classmethod
#     def changecompany(cls, newcompany):
#         cls.company = newcompany

# x = A()
# x.name = "manav"
# x.show()       # This will print: The name of employee is manav and his company is NASA
# x.company = "google"
# x.show()       # This will print: The name of employee is manav and his company is google
# print(x.company)  # This will print: google





#
#  class A:
#     company="Google"
#     numberofemployee=0
#     def __init__(self,n):
#         self.name=n
#         self.salaryhike="70%"
#         A.numberofemployee +=1

#     def show(self):
#         print(f"The name of employee is {self.name} {self.numberofemployee} and he works in {self.company} and his salay hike is {self.salaryhike}")
# x1=A("manav")
# x1.company="NASA"
# x1.show()

# x2=A("yuvi")
# x2.salaryhike="90%"
# x2.show()




# class A:
#     def __init__(self,n):
#         self.num=n

#     def show(self,i):
#         self.num=self.num+i
#     @staticmethod
#     def add (a,b):
#         return (a+b)
# x=A(5)
# print(x.num)
# x.show(5)
# print(x.num)



# class A:
#     company="NASA"

#     def show(self):
#         print(f"The name of employe is {self.name} and his company {self.company}")

#     @classmethod
#     def changecompany(cls,newcompany):
#         cls.company=newcompany

# x=A()
# x.name="manav"
# x.show()
# x.changecompany("Google")
# x.show()
# print(A.company)



# class person:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     @classmethod
#     def fromstr(cls,string):
#         return cls( string.split("-")[0],string.split("-")[1])
# x1=person("manav",500000)
# print(x1.name)
# print(x1.salary)


# string="manav-500000"
# x2=person.fromstr(string)
# print(x2.name)
# print(x2.salary)



# class person:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     @classmethod
#     def fromstr(cls,string):
#         return cls(string.split("-")[0],string.split("-")[1])
    
# x1=person("manav",500000)
# print(x1.name)
# print(x1.salary)

# string="manav-500000"
# x2=person.fromstr(string) 
# print(x2.name)
# print(x2.salary)



# x=input("enter the number:")
# print(f"multiplication table of {x}")
# try:
#    x=int(x)
#    for i in range(1,11):
#        print(f"{x} x {i}={x * i}")
# except ValueError :
#     print("ohh ! some error occur")

# print("ohh ! you got it")



# class A:
#     def __init__(self,v):
#         self._value=v

#     def show (self):
#         print(f"value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10* self._value
#     @ten_value.setter
#     def ten_value(self,new_value):
#          self._value=new_value/10
# x=A(5)
# x.ten_value=9
# print(x.ten_value)
# x.show()



# class A:
#     name="manav"
#     work= "data scientist"
#     salary= 500000
#     def info (self):
#      print(f"the name of employee is {self.name} and he is {self.work} and his salary {self.salary}")
# z=A()
# z.info()

# class B:
#     def __init__(self,n,w):
#       self.name=n
#       self.work=w
#     def info (self):
#        print(f"{self.name} is a {self.work}")
# y=B("manav","data scientist")
# y.info()


# class A:
#     def __init__(self,v):
#         self._value=v

#     def show (self):
#         print(f"The value is {self._value}") 

#     @property
#     def ten_value(self):
#         return 10* self._value
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#          self._value=new_value/10
# x=A(5)
# x.ten_value=9
# print(x.ten_value)
# x.show()



# class A:
#     def __init__(self,n):
#         self.num=n

#     def addition(self,i):
#         self.num=self.num+i
    
#     @staticmethod
#     def add (a,b):
#         return a+b
    
# x=A(5)
# print(x.num)
# x.addition(5)
# print(x.num)



# class A:
#     def __init__(self,n,w):
#         self.name=n
#         self.work=w
#     def show(self):
#         print(f"{self.name} is a {self.work}")
# class B(A):
#     def show1(self,n2,w2):
#         self.name2=n2
#         self.work2=w2
#         print(f"{self.name2} is a {self.work2}")
# x=B("manav ","data scientist")
# x.show()
# x.show1("manav1","data scientist1")



# class A:
#     company="NASA"
#     numberofemployee=0
#     def __init__(self,n):
#         self.name=n
#         self.salaryhike="50%"
#         A.numberofemployee +=1
#     def show(self):
#         print(f"The name of employee is {self.name} {self.numberofemployee} and he works in {self.company} and his salary hike is {self.salaryhike}")
# x1=A("manav")
# x1.show()
# x2=A("yuvi")
# x2.company="google"
# x2.salaryhike="90%"
# x2.show()


# class A:
#     company="NASA"
        
#     def show(self):
#         print(f"The name of employee is {self.name} and he works in {self.company}")
#     @classmethod
#     def changecompany(self,newcompany):
#         self.company=newcompany
# x=A()
# x.name="manav"
# x.show()
# x.changecompany("google")
# x.show()
# print(A.company)



# class A:
#     def __init__(self,n,s):
#         self.name=n
#         self.salary=s

#     @classmethod
#     def fromstr(cls,string):
#         return cls (string.split("-")[0],string.split("-")[1])
    
# x1=A("manav",500000)
# print(x1.name)
# print(x1.salary)

# string="manav-500000"
# x2=A.fromstr(string)
# print(x2.name)
# print(x2.salary)




# class A:
#     company="NASA"

#     def show(self):
#         print(f"The name of employee is {self.name} and he works in {self.company}")

#     @classmethod
#     def changecompany(self,newcompany):
#         self.company=newcompany

# x=A()
# x.name="manav"
# x.show()
# x.changecompany("GOOGLE")
# x.show()
# print(A.company)
        

# def cube(x):
#     return x*x*x
# print(cube(5))
# l=[1,2,3]

# newl=list(filter(cube,l))
# print(newl(1))


# def f_f(a):
#     return a>1
# l=[1,2,3]

# newl=list(filter(f_f,l))
# print(newl)


# from functools import reduce
# def cube(x,y):
#     return x*y
# l=[1,2,3,4,5]
# newl=reduce(lambda x,y:x+y,l)
# print(newl)




# x=input("enter the value-:")
# print(f"multiplication table of {x}")
# try:
#  for i in range(1,11):
#     print(f"{int(x)}x{i}={int(x)*i}")
# except:
#   print("you should be enter only int value ")
# finally:
#   print("i am always executed ")

# print("ohh ! you got it ")




# l=[1,2,3]
# print(dir(l))
# print(l.__class_getitem__)


# print(help(InterruptedError))

# class person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
# p=person("manav",19)
# print(p.__dict__)




# class employee:
#     def __init__(self,n,id):
#         self.name=n
#         self.identity=id

# class programmer(employee):
#     def __init__(self,n,id,l):
#         super().__init__(n,id)
#         self.language=l

# e=employee("yuvi","500")
# e1=programmer("manav","5009","python")
# print(e1.name)
# print(e1.identity)
# print(e1.language)



# class rectangle:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def area(self):
#         return self.x*self.y
    
# class circle(rectangle):
#     def __init__(self,r):
#         self.radius=r
#         super().__init__(r,r)
#     def area(self):
#         return 3.14*super().area()

    
# r=rectangle(5,5)
# print(r.area())

# c=circle(6)
# print(c.area())



# class A:
#     def __init__(self,n,i):
#         self.name=n
#         self.id=i
        
# class B(A):
#     def __init__(self,n,i,l):
#         super().__init__(n,i)
#         self.lang=l
# a=A("manav","9090",)
# a1=B("yuvi","8989","c")
# print(a.name)
# print(a.id)
# print(a.lang)



'''import pyttsx3
crax = pyttsx3.init()
crax.say(Paagal ye paagal woh
Paagal karde
Jahaan bhi ye jaaye
Dekho karta hai kaisa deewana sabko

SHINCHAN....

Mera naam bhi Shinchan hai
Main shararat se bhara
Badi mushkil mein padi
Meri family nohara

Come on baby, come on baby
Aayo karein dance shuru
# Zor se ghume hum tum jhume
# Nacho, Nacho
# Aur dekho sabko hilado

# OH SHINCHAN.....

# Kabhi uchhalta hai
# Kabhi ye machalta hai
# Har dum bekabooRoz ye karta hai
# Nayi nayi gadbad
# Tumko hasadega SHINCHAN.....)crax.runAndWait()'''


# class Rectangle:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def area(self):
#         return self.x*self.y
    
# class Circle(Rectangle):
#     def __init__(self,r):
#         self.radius=R
#         super().__init__(r,r)
#     def area(self):
#         return 3.14*super().area()

    
# R=Rectangle(5,5)
# print(R.area())

# C=Circle(5)
# print(C.area())




'multiple inheritance'
# class A:
#     company="NASA"
#     name="manav"
#     def show(self):
#         print(f"The name of employee is {self.name} and he works in {self.company}")

# class B:
#     def show2(self):
#         print("this programming language is very good")

# class C(A,B):
#     def show3(self):
#         print(f"The name of employee is {self.name} and he works in {self.company}")
# a=A()
# b=B()
# c=C()

# c.show()
# c.show2()
# c.name="yuvi"
# c.show3()



'multi-level inheritance'
# class A:
#     name="manav"
#     def show1(self):
#         print(f"The name of employee is {self.name}")

# class B(A):
#     def show2(self):
#         print("and he earns 1000000 per months  ")

# class C(B):
#     def show3(self):
#      print("and he is data science master ")

# a=A()
# b=B()
# c=C()
# c.show1()
# c.show2()
# c.show3()



# class A:
#     name="manav"
#     work="data scientist"
#     def show(self):
#             print(f"The name of employee is  {self.name} and he is {self.work}")
    
# class B(A):
#     def show1(self):
#          print("ohh so you are doing single inheritance")
     

# a=A()
# b=B()

# b.show1()
# b.show()




# class A:
#     name="manav"
#     work="data scientist"
#     def showdetail(self):
#         print(f"The name of employee is {self.name} and he is {self.work}")

# class B:
#     company="NASA"
#     def showcompany(self):
#         print(f"The name of company is {self.company}") 

# class C(A,B):
#     language="python"
#     def showlanguage(self):
#         print(f"The employee 9078 is happy with his language {self.language}")

# x=A()
# x.showdetail()

# y=B()
# y.showcompany()

# z=C()

# z.showdetail()
# z.showcompany()
# z.showlanguage()




# class A:
#     def show1(self):
#         print("manav is a data scientist")

# class B(A):
#     def show2(self):
#         print("and he earns 1000000 per month ")

# class C(B):
#     def show3(self):
#         print("and he master's python langyuage")

# a=A()
# a.show1()

# b=B()
# b.show1()
# b.show2()

# c=C()
# c.show1()
# c.show2()
# c.show3()




# for i in range(100):
#     if (i==50):
#         continue
#     print(i)
# print("skip the loop")



# def average (a,b):
#     '''hello world'''
#     print((a+b)/2)

# average(5,5)
# print(average.__doc__)




# def factorial(x):
#     if(x==0 or x==1):
#       return 1
#     else:
#        return x * factorial(x-1)
    
# print(factorial(4))



# a=int(input("enter the value between between 5-10-:"))

# if(a<5 or a>10):
#     raise ValueError("value should be between 5-10 ")



# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def area(self):
#         return self.x*self.y
    
# class circle(shape):
#     def __init__(self,r):
#         self.radius=r
#         super().__init__(r,r)

#     def area(self):
#         return 3.14 * super().area()

# rec=shape(5,5)
# print(rec.area())
# c=circle(5)
# print(c.area())


# from PyPDF2 import PdfMerger

# merger = PdfMerger()

# for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()


# class A:
#     def __init__(self,A1,B,C):
#         self.a=A1
#         self.b=B
#         self.c=C
#     def __str__(self):
#         return f"{self.a}a + {self.b}b + {self.c}c"
    
#     def __add__(self,y):
#         return A (self.a+y.a, self.b+y.b, self.c+y.c)
    

# x=A(5,10,15)
# print(x)

# x1=A(6,11,16)
# print(x1)

# print(x+x1)
# print(type(x+x1))



# import time 
# x=time.time()

# i=0
# while i<10:
#     print("hello")
#     i+=1
# print("while loop ran in ",time.time()-x,"second")


# for i in range (0,10):
#     print("hello")
# print("for  loop ran in ",time.time()-x,"second")

# print(5)
# time.sleep(5)
# print("wait for 5 seconds")







# from ohh import *
# hello()
# print(x)

# import math as m
# x=m.sqrt(100)
# print(x)


# from math import sqrt,pi
# x=sqrt(100)*pi
# print(x)

# import math
# print(dir(math))
# print(type(math.lcm))



# list=[1,2,3,4,5,6,7]

# for index,i in enumerate(list,start=1):
#     print(i)
#     if(index==4):
#         print("hello")





# class hello:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def __str__(self):
#         return f"{self.a}a + {self.b}b + {self.c}c"
    
#     def __add__(self,x):
#         return hello(self.a+x.a,self.b+x.b,self.c+x.c)
    
# h=hello(5,10,15)
# print(h)

# h1=hello(6,11,16)
# print(h1)
# print(h+h1)



# import argparse
# import sys

# def calc(args):
#    if args.o =="add":
#       return args.a + args.b
#    elif args.o =="sub":
#       return args.a - args.b
#    elif args.o =="mul":
#       return args.a * args.b
#    elif args.o =="div":
#       return args.a / args.b
#    else:
#       return "something went wrong "


# if __name__=="main":
#    parser=argparse.ArgumentParser()
#    parser.add_argument("--a",type=float,default=1.0,
#                        help= "enter the first number.This is utility calculation . please contact to programmer")
#    parser.add_argument("--b",type=float,default=3.0,
#                        help= "enter the second number.This is utility calculation . please contact to programmer")
#    parser.add_argument("--a",type=str,default="add",
#                        help= "enter the number.This is utility calculation . please contact to programmer")
#    args=parser.parse_args()
#    sys.stdout.write(str(calc(args)))





# foods=list()
# while True:
#    food=input("enter your  favorite food:-")
#    if food=="quit" :
#       break
#    foods.append(food)

# print(foods)




# class employee:
#    def __init__(self,n,s):
#       self.name=n
#       self.salary=s
#    @classmethod
#    def fromstr(cls,x):
#       return cls(x.split("-")[0],x.split("-")[1])

# e1=employee("manav",500000)
# print(e1.name)
# print(e1.salary)



# x=("manav-500000")
# e2=employee.fromstr(x)
# print(e2.name)
# print(e2.salary)


# car=list()
# while True:
#     car=input("enter your favorite car:-")
#     if car=="5":
#         break



# cars=list()
# while (car:=input("enter your favorite car:- "))!= "quit" :
#     cars.append(car)




# import time

# def usingwhile():
#     i = 0
#     while i < 1000:  # Corrected the loop condition
#         print("hello")
#         i += 1

# def usingfor():
#     for i in range(1000):
#         print("world")

# # Measure time for usingwhile()
# start_time = time.time()
# usingwhile()
# end_time = time.time()
# print("Time taken for usingwhile:", end_time - start_time)

# # Measure time for usingfor()
# start_time = time.time()
# usingfor()
# end_time = time.time()
# print("Time taken for usingfor:", end_time - start_time)




# from PyPDF2 import PdfReader, PdfWriter
# import os

# merger = PdfWriter()

# # List all PDF files in the current directory
# files = [file for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
#     # Open each PDF file as a PdfReader object
#     with open(pdf, "rb") as f:
#         reader = PdfReader(f)
#         merger.append(reader)

# # Write the merged PDF to a file
# with open("merged-pdf.pdf", "wb") as f:
    # merger.write(f)


# import shutil as s
# s.copy("work.py","work2.py")
# s.copytree("__pycache__","hello")
# s.move(".cpython-312.pyc/one.file","two22.file")


# def my_generator():
#     for i in range(10):
#         yield i

# gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# class A:
#     def __init__(self,v):
#         self._value=v

#     def show(self):
#         print(f"value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10 *self._value
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#          self._value=new_value/10
    
# a=A(5)
# print(a.ten_value)
# a.ten_value=9
# print(a.ten_value)
# a.show()


# import requests 
# from bs4 import BeautifulSoup
# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r = requests.get(url)
# # print(r.text)


# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)
# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'hello',
#     "body": 'world',
#     "userId": 748993,
#   }
# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }
# response = requests.post(url, headers=headers, json=data)

# print(response.text)


# import requests
# from bs4 import BeautifulSoup
# url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
# r = requests.get(url)
# # # print(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# for heading in soup.find_all("h2"):
#   print(heading.text)

# url="https://jsonplaceholder.typicode.com/guide/"

# data={
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
#   }

# headers={
#     'Content-type': 'application/json; charset=UTF-8',
#   }


# responce=requests.post(url,headers=headers,json=data)
# print(responce.text)



# from functools import lru_cache
# import time
# @lru_cache(maxsize=5)
# def run(x):
#     time.sleep(10)
#     return x*10


# print(run(6))
# print("here is 10 * of 6")
# print(run(10))
# print("here is 10 * of 10")
# print(run(210))
# print("here is 10 * of 210")


# print(run(6))
# print("here is 10 * of 6")
# print(run(10))
# print("here is 10 * of 10")
# print(run(210))
# print("here is 10 * of 210")



# foods=list()
# while True:
#     food=input("enter the food")
#     if food=="quit":
#         break
# print(foods)

# foods=list()
# while (food:=input("enter the food"))!="quit":
#     foods.append(food)



# import re 

# pattern=r"[A-Z]ahadev"
# text='''The Alpine ibex (Capra ibex), Mahadev Bahadev also known as the steinbock, 
# is a species of goat that lives in the Alps of Europe. 
# Its closest living relative is the Iberian ibex. 
# They have brownish-grey coats and sharp hooves adapted to steep, rough terrain.
# Found at elevations as high as 3,300 metres (10,800 ft), 
# they are active throughout the year '''

# x=re.finditer(pattern,text)
# print(x)
# for y in x:
#     print(y.span())
#     print(text[y.span()[0]:y.span()[0]])


# from PyPDF2 import PdfMerger

# merger = PdfMerger() 
# for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
#     merger.append(pdf)

# merger.write("merged-pdf.pdf")
# merger.close()



# class helloo:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
   
#     def __str__(self):
#         return f"{self.a}a + {self.b}b+ {self.c}c"
    
#     def __add__(self,z):
#         return helloo (self.a+z.a,self.b+z.b,self.c+z.c)
    
# h1=helloo(5,6,7)
# print(h1)

# h2=helloo(8,9,10)
# print(h2)

# print(h1+h2)




# import asyncio
# import requests


# async def function1(): 

#    url = 'https://example1.com/file.zip'
#    response = requests.get(url)

#    with open('file.zip', 'wb') as file:
#       file.write(response.content)
#       print("func1")



# async def function2():
#     url = 'https://example2.com/file.zip'
#     response = requests.get(url)

#     with open('file.zip', 'wb') as file:
#       file.write(response.content)
#       print("func2")


# async def function3():
#     url = 'https://example3.com/file.zip'
#     response = requests.get(url)

#     with open('file.zip', 'wb') as file:
#       file.write(response.content)
#       print("func3")
    

# async def main():
 
#       await function1()
#       await function2()
#       await function3()


# import asyncio
# import requests

# async def download_file(url):
#     response = requests.get(url)
#     return response.content

# async def function1():
#     url = 'https://example1.com/file.zip'
#     content = await asyncio.to_thread(download_file, url)
#     with open('file1.zip', 'wb') as file:
#         file.write(content)
#     print("func1")

# async def function2():
#     url = 'https://example2.com/file.zip'
#     content = await asyncio.to_thread(download_file, url)
#     with open('file2.zip', 'wb') as file:
#         file.write(content)
#     print("func2")

# async def function3():
#     url = 'https://example3.com/file.zip'
#     content = await asyncio.to_thread(download_file, url)
#     with open('file3.zip', 'wb') as file:
#         file.write(content)
#     print("func3")

# async def main():
#     await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )

# if __name__ == "__main__":
#     asyncio.run(main())


# import requests
# import asyncio

# async def func1():

#   url = 'https://wallpapercave.com/wp/wp2852124.png/fileio1.zip'
#   response = requests.get(url)

#   with open('fileio1.zip', 'wb') as file:
#     file.write(response.content)
#     print("func1")

# async def func2():
    
#   url = 'https://wallpapers.com/images/hd/4d-black-polygon-v9gcqfoyg33nnv82.jpg/fileio2.zip'
#   response = requests.get(url)

#   with open('fileio2.zip', 'wb') as file:
#     file.write(response.content)
#     print("func2")


# async def func3():
    
#   url = 'https://autodeskmagazine.com/image?img=var/uploads/videos/gsm15cawHbY.jpg&w=540&h=0/fileio3.zip'
#   response = requests.get(url)

#   with open('fileio3.zip', 'wb') as file:
#     file.write(response.content)
#     print("func3")

# async def main():
#     l=await asyncio.gather(
#         func1(),
#         func2(),
#         func3(),
#     )
#     print(l)

#     x=asyncio.create_task(func1())
#     # await func1()
#     await func2()
#     await func3()

# asyncio.run(main())


# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def main(seconds):
#     print(f"sleeping for {seconds}")
#     time.sleep(seconds)
# def demo():
#   time1=time.perf_counter()
#   t1=threading.Thread(target=main,args=[5])
#   t2=threading.Thread(target=main,args=[6])
#   t3=threading.Thread(target=main,args=[7])
#   t4=threading.Thread(target=main,args=[8])

#   time2=time.perf_counter()
#   print(time2-time1)

#   t1.start()
#   t2.start()
#   t3.start()
#   t4.start()

# def helo():
#    with ThreadPoolExecutor() as executor:
# #     future1 = executor.submit(demo)
# #     print(future1.result())
# #     future2 = executor.submit(demo)
# #     print(future2.result())
# #     future3 = executor.submit(demo)
# #     print(future3.result())
# #     future4 = executor.submit(demo)
# #     print(future4.result())
#     x=[3,4,5,6]
#     results=executor.map(main,x)
#     for result in results:
#      print(result)

# helo()



# import requests
# import asyncio

# async def function1():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=PEtLUEz6&id=11E5DE0B18360F41F16557697ACD5A13403D519D&thid=OIP.PEtLUEz6VEKv477AsU4ytwHaDT&mediaurl=https%3a%2f%2fwww.greengeeks.com%2ftutorials%2fwp-content%2fuploads%2f2019%2f08%2fcopy-each-image-url-768x342.png&exph=342&expw=768&q=image+url&simid=608013648757789283&FORM=IRPRST&ck=15939D66F4399299735016AB2C78BD26&selectedIndex=31&itb=0&ajaxhist=0&ajaxserp=0'
#     response = requests.get(url)
#     with open('file1111.zip', 'wb') as file:
#       file.write(response.content)
#     print("func1111")

# async def function2():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=BW54Wc2X&id=21E4AB7E87CCF7EA2B388B44CECF115A80C7FDEB&thid=OIP.BW54Wc2X6zBd8PyKkXgDqgHaHa&mediaurl=https%3a%2f%2ffiles.softicons.com%2fdownload%2fsystem-icons%2flozengue-filetype-icons-by-gurato%2fpng%2f512%2fURL.png&exph=512&expw=512&q=image+url&simid=608051788085992773&FORM=IRPRST&ck=15BEBFC12FB24B966BAA0DD3885E161B&selectedIndex=7&itb=1&ajaxhist=0&ajaxserp=0.zip'
#     response = requests.get(url)
#     with open('file2222.zip', 'wb') as file:
#      file.write(response.content)
#     print("func2222")

# async def function3():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=ABxetoZW&id=5334F81E815C511DCB942030AF5A30B9BAEED60D&thid=OIP.ABxetoZWRGN9HRaOLYK-JgHaE5&mediaurl=https%3a%2f'
#     response = requests.get(url)
#     with open('file3333.zip', 'wb') as file:
#      file.write(response.content)
#     print("func3333")

# async def main():
#     # l=await asyncio.gather(
#     #   await  function1(),
#     #   await  function2(),
#     #   await  function3(),
#     # )
#     # print(l)
#     x=asyncio.create_task(function1())
#     # await  function1()
#     await  function2()
#     await  function3()

# asyncio.run(main())




# import requests
# import asyncio

# async def function1():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=C0POIWUy&id=7500D402EEA2A8331EA5B7D88C1F4CBE2C6252E9&thid=OIP.C0POIWUyxTxZ_AeAG2lW3AHaDt&mediaurl=https%3a%2f%2fphotutorial.com%2fwp-content%2fuploads%2f2023%2f04%2fFeatured-image-AI-image-generators-by-Midjourney.png&exph=768&expw=1536&q=image+&simid=607995803178390785&FORM=IRPRST&ck=6D8F08DB6E01A41795210846EC33F49A&selectedIndex=2&itb=0&ajaxhist=0&ajaxserp=0.zip'
#     response = requests.get(url)

#     with open('filebhj.zip', 'wb') as file:
#      file.write(response.content)
#     print("function 1")


# async def function2():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=24T00MDK&id=5F831DE9C1F56B20CF15B4ECEA4B425B7FF2B1D5&thid=OIP.24T00MDK-RUhFnm1Do5PFwHaFj&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.db84f4d0c0caf915211679b50e8e4f17%3frik%3d1bHyf1tCS%252brstA%26riu%3dhttp%253a%252f%252fwww.photo-paysage.com%252falbums%252fPaysages%252fLac-riviere-cascade%252fparadis-lac-cascade-plitvice.jpg%26ehk%3dOMBV2yAjylP5qHUwMS44Of1KzgjCiN%252bqSMBfUEKmzBI%253d%26risl%3d%26pid%3dImgRaw%26r%3d0&exph=1920&expw=2560&q=image+&simid=608004298603849084&FORM=IRPRST&ck=060B5107C6757D46B07411990697F043&selectedIndex=3&itb=0&ajaxhist=0&ajaxserp=0.zip'
#     response = requests.get(url)

#     with open('filenkjkj3.zip', 'wb') as file:
#      file.write(response.content)
#     print("function 2")


# async def function3():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=f6nN92PK&id=2C463CF121FF6C58882DDF59CDCBB673171E4891&thid=OIP.f6nN92PKZtocaKcJhARRYQHaLS&mediaurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F19%2Feb%2F67%2F19eb67070ecc3f812cf8e72b39e72b56.jpg&exph=1024&expw=672&q=image+&form=IRPRST&ck=7F2035ED258315BB523186650D537B1C&selectedindex=3&itb=0&ajaxhist=0&ajaxserp=0&pivotparams=insightsToken%3Dccid_24T00MDK*cp_060B5107C6757D46B07411990697F043*mid_5F831DE9C1F56B20CF15B4ECEA4B425B7FF2B1D5*simid_608004298603849084*thid_OIP.24T00MDK-RUhFnm1Do5PFwHaFj&vt=0&sim=11&iss=VSI&ajaxhist=0&ajaxserp=0.zip'
#     response = requests.get(url)

#     with open('fileknn.zip', 'wb') as file:
#      file.write(response.content)
#     print("function 3")

# async def hello():
#     l=asyncio.gather(
#         await function1(),
#         await function2(),
#         await function3(),
#     )
#     print(l)
# #   x=asyncio.create_task(function1())
# # #   await function1()
# #   await function2()
# #   await function3()

# asyncio.run(hello())


# import asyncio

# async def function1():
#     await asyncio.sleep(1)
#     print("function1")

# async def function2():
#     await asyncio.sleep(2)
#     print("function2")

# async def function3():
#     await asyncio.sleep(3)
#     print("function3")

# async def function4():
#     await asyncio.sleep(4)
#     print("function4")


# async def main():
#     y=await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#         function4(),
#     )
#     print(y)
# #    x=asyncio.create_task(function1())
# # #    await function1()
# #    await function2()
# #    await function3()
# #    await function4() 

# asyncio.run(main())






# import asyncio

# async def function1():
#     await asyncio.sleep(2)
#     print("function 1")
#     return "har"

# async def function2():
#     await asyncio.sleep(2)
#     print("function 2")
#     return "har"

# async def function3():
#     await asyncio.sleep(5)
#     print("function 3")
#     return "mahakaal"


# async def main():
#     l=await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )
#     print(l)
# #   x=asyncio.create_task(function1())
# # #   await function1()
# #   await function2()
# #   await function3()

# asyncio.run(main())

# import time
# import  threading
# from concurrent.futures import ThreadPoolExecutor

# def function(seconds):
#     print(f"sleep for {seconds} seconds")
#     time.sleep(seconds)

# def thread():
#   time1=time.perf_counter()
#   function(2)
#   function(4)
#   function(6)
#   time2=time.perf_counter()
#   print(time2-time1)

#   time1=time.perf_counter()
#   t1=threading.Thread(target=function,args=[2])
#   t2=threading.Thread(target=function,args=[4])
#   t3=threading.Thread(target=function,args=[6])

#   t1.start()
#   t2.start()
#   t3.start()

#   t1.join()
#   t2.join()
#   t3.join()
#   time2=time.perf_counter()
#   print(time2-time1)


# with ThreadPoolExecutor() as executor:
#     # future1 = executor.submit(function,2)
#     # print(future1.result())
#     # future2 = executor.submit(function,4)
#     # print(future2.result())
#     # future3 = executor.submit(function,6)
#     # print(future3.result())

    # x=[2,4,6,8]
    # results=executor.map(function,x)
    # for result in results :
    #    print(result)




# import time
# import threading
# from concurrent.futures import ThreadPoolExecutor

# def function(seconds):
#     print(f"sleep for {seconds}")
#     time.sleep(seconds)

# def ok():
#   time1=time.perf_counter()
#   function(2)
#   function(4)
#   function(6)
#   time2=time.perf_counter()
#   print(time2-time1)
#   time1=time.perf_counter()
#   t1=threading.Thread(target=function,args=[2])
#   t2=threading.Thread(target=function,args=[4])
#   t3=threading.Thread(target=function,args=[6])


#   t1.start()
#   t2.start()
#   t3.start()

#   t1.join()
#   t2.join()
#   t3.join()

#   time2=time.perf_counter()
#   print(time2-time1)


# with ThreadPoolExecutor() as executor:
#     future1 = executor.submit(function,2)
#     print(future1.result())
#     future2 = executor.submit(function,4)
#     print(future2.result())
#     future3 = executor.submit(function,6)
#     print(future3.result())

#   x=[2,4,6,8]
#   results=executor.map(function,x)
#   for rersult in results():
#     print(rersult)


# def demo(x,y):
#     def add(x,y):
#         return x+y
#     a=add(x,y)
#     return a+"mahadev"
# b=demo("har","har")
# print(b)

# list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# x=(list1.insert(00,6))
# print(x)


# class A:
#     def __init__(self,v):
#         self._value=v

#     def show(self):
#         print(f"value is {self._value}") 

#     @property
#     def ten_value(self):
#         return 10* self._value
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10

# a=A(5)
# a.show()
# # print(a.ten_value)
# a.ten_value=9
# print(a.ten_value)


# class Father:
#     def __init__(self):
#      print("Father constructor")
#     def show1(self):
#         print("Father")

# class Son(Father):
#     def __init__(self):
#        print("Son constructor")
#        super().__init__()
#     def show2(self):
#         print("Son")

# class Daughter(Father):
#     def __init__(self):
#        print("Daughter constructor")
#        super().__init__()
#     def show3(self):
#         print("Daughter")

# d=Daughter()
# s=Son()


# import threading
# import time # type: ignore
# from concurrent.futures import ThreadPoolExecutor


# def function(seconds):
#     time.sleep(seconds)
#     print(f"sleep for {seconds}")

# def main():
#   time1=time.perf_counter()
#   function(5)
#   function(10)
#   function(15)
#   time2=time.perf_counter()
#   print(time2-time1)


#   time1=time.perf_counter()

#   t1=threading.Thread(target=function,args=[5])
#   t2=threading.Thread(target=function,args=[10])
#   t3=threading.Thread(target=function,args=[15])

#   t1.start()
#   t2.start()
#   t3.start()

#   t1.join()
#   t2.join()
#   t3.join()

#   time2=time.perf_counter()
#   print(time2-time1)

# def return1():
#   with ThreadPoolExecutor() as executor:
#       future1 = executor.submit(function,5)
#       print(future1.result())
      
    
#       future2 = executor.submit(function,10)
#       print(future2.result())
      

#       future3 = executor.submit(function,15)
#       print(future3.result())

# def return2():
#     with ThreadPoolExecutor() as executor:
#      l=[10,20,30,40,50]
#     results=executor.map(function,l)
#     for i in results:
#        print(i)

# return1()

# a=6
# b=6

# print("a is greater ")if (a>b)else print("equal")if (a==b)else print("b is greater ")


# marks=[5,6,98,0]
# for index, i in enumerate(marks,start=1):
#     print(i)
#     if(index==2):
#         print("ohh !")



# class math:
#     def __init__(self,num):
#         self.num=num

#     def addtonum (self,n):
#         self.num=self.num+n

#     @staticmethod
#     def add(a,b):
#         return a+b
    
# a=math(6)
# print(a.num)

# a.addtonum(7)
# print(a.num)

# a.add(5,5)
# print(a.add(7,3))
    


# import time #type: ignore
# import asyncio


# async def function1():
#     await asyncio.sleep(3)
#     print("func1")

# async def function2():
#     await asyncio.sleep(3)
#     print("func2")


# async def function3():
#     await asyncio.sleep(6)
#     print("func3")

# async def main():

#     x=await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#       )
#     print(x)
#   l=asyncio.create_task(function1())
# #   await function1()
#   await function2()
#   await function3()
#   print(l)
# asyncio.run(main())



# class employee:
#     company="apple"
#     def show(self):
#         print(f"the name of employee is {self.name} and he works in {self.company}")

#     @classmethod
#     def changecompany(cls,newcompany):
#         cls.company= newcompany


# a=employee()
# a.name="manav"
# a.show()
# a.changecompany("google")
# a.show()
# print(employee.company)


# def Greet(x):
#     def y(*args,**kwargs):
#         print("start")
#         x(*args,**kwargs)
#         print("end")
#     return y

# @Greet
# def hello():
#     print("mid")

# @Greet
# def add(a,b):
#     print(a+b)
# Greet(hello())
# Greet(add(5,6))



# import re

# pattern="machines"

# text='''Artificial Intelligence refers to the intelligence of machines. 
# This is in contrast to the natural intelligence of humans and animals. 
# With Artificial Intelligence, machines perform functions such as learning, planning, reasoning and problem-solving. 
# Most noteworthy, Artificial Intelligence is the simulation of human intelligence by machines. 
# It is probably the fastest-growing development in the World of technology and innovation. 
# Furthermore, many experts believe AI could solve major challenges and crisis situations.'''

# x=re.finditer(pattern,text)
# print(x)


# marks=[1,58,88,86,1,1]
# print(marks[:])

# if "heo" not in "hello":
#     print("yes")

# if 55 in marks:
#     print("yes")
# else:
#     print("no")

# lst=[i*i for i in range(10)if i%2==0]
# print(lst)


# marks.sort(reverse=True)
# marks.append(100)
# l=marks.copy()
# marks.clear()
# l=[5,6,7,8,9]
# marks.extend(l)
# print(marks.index(86))
# print(marks.count(1))
# marks.insert(5,1000)
# marks.pop(1)
# print(marks)

# x=(1,2,3)
# print(dir(x))


# print(help(str))

# class employee:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a

# e=employee("manav",30)
# print(e.__dict__)


# cat=(2,3,4,5,6,7)
# print(type(tuple),(tuple))

# print(tuple[0:])
# tuple2=tuple[2:6]
# print(tuple2)

# x=list(cat)
# x.append(55)
# x.pop(2)
# cat=tuple(x)
# print(cat)


# dict={"name":"manav","id":909090,"roll":"data scientist"}
# dict2={"passion":"coding"}
# print(dict.keys())
# print(dict.values())

# for i in dict.keys():
#     print(i)

# for j in dict.values():
#     print(j)

# dict.update(dict2)
# dict.pop("id")
# dict.popitem()
# dict.clear()
# del dict["roll"]
# print(dict)


# def gen(n):
#     for i in range(n):
#         yield i

# print(gen(100000))
# for i in gen(100):
#     print(i)

# x=gen(5)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# num="pagal"
# for i in num:
#     print(i)

# x=iter(num)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# class test:
#     no_of_cake=6
#     def __init__(self,n,o):
#         self.name=n
#         self.order=o

#     def detail(self):
#         print("the name of customer is",self.name,"and he order",self.no_of_cake,self.order,"cake")

#     @classmethod
#     def new_cake(cls,new_cake):
#         cls.no_of_cake=new_cake


# t1=test("manav","choco")
# t1.new_cake(45)
# test.new_cake(45)
# t1.detail()
# test.detail()

# Python program showing
# abstract base class work
# from abc import ABC, abstractmethod


# class Animal(ABC):

#     def move(self):
#         pass

# class Human(Animal):

#     def move(self):
#         print("I can walk and run")

# class Snake(Animal):

#     def move(self):
#         print("I can crawl")

# class Dog(Animal):

#     def move(self):
#         print("I can bark")

# class Lion(Animal):

#     def move(self):
#         print("I can roar")

# # Driver code
# R = Human()
# R.move()

# K = Snake()
# K.move()

# R = Dog()
# R.move()

# K = Lion()
# K.move()



"type function "
# class mymeta(type):
#     def __new__(cls,name,base,attr):
#         return super().__new__(cls,name,base,attr)
    

# class myclass(metaclass=mymeta):
#     pass

# m=myclass()
# print(m)


"using init"

# class mymetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         return super().__new__(cls,name,bases,attrs)
    
#     def __init__(cls,name,bases,attrs):
#         super().__init__(name,bases,attrs)

# class myclass(metaclass=mymetaclass):
#     pass

# m=myclass()
# print(m)

"dynamically type "

# def mymeta(name,base,attr):
#     return type(name,base,attr)

# myclass=mymeta('myclass',(object,),{'attr':43})

# print(myclass)

# class commonattribute(type):
#     def __new__(cls,name,base,attr):
#         attr['common_attribute']="i am common in all"
#         return super().__new__(cls,name,base,attr)
    
# class baseclass1(metaclass=commonattribute):
#     def __init__(self,value):
#         self.value=value

# class baseclass2(metaclass=commonattribute):
#     def __init__(self,value):
#         self.value=value

# c1=baseclass1(10)
# c2=baseclass1(20)

# print(c1.value)
# print(c2.value)

# print(c1.common_attribute)
# print(c2.common_attribute)







