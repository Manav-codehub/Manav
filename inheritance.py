'single inheritance'
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



'hybrid inheritance '

# class A:
#     def show1(self):
#         print("class A")

# class B(A):
#     def show2(self):
#         print("class B")

# class C(A):
#     def show3(self):
#         print("class C")

# class D(B,C):
#     def show4(self):
#         print("class D")

# d=D()

# d.show1()
# d.show2()
# d.show3()
# d.show4()

'hierarchical inheritance'

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


def doc(x):
    '''here is your doc '''
    return x
print(doc(5))
print(doc.__doc__)