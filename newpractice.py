# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def area(self):
#         return self.x + self.y
    
# class circle(shape):
#     def __init__(self, radius):
#         self.radius=radius
#         super().__init__(radius, radius)

#     def area(self):
#         return 3.14 * super().area()
    


# # s=shape(5,5)
# # print(s.show())

# c=circle(5)
# print(c.area())


# class vector:
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
    
#     def __str__(self):
#         return f"{self.x}x + {self.y}y + {self.z}z"
    
#     def __add__(self,b):
#         return vector (self.x+b.x,self.y+b.y,self.z+b.z)
    
# a1=vector(5,6,7)
# print(a1)


# a2=vector(8,9,4)
# print(a2)

# print(a1+a2)
# print(type(a1+a2))

# tup=(1,2.3,4,5,5,66,)
# x=list(tup)
# x.insert(2,"manav")
# x.append(90)
# tup=tuple(x)
# print(x)

# x={1,2,3,4,5}
# y={6,7,8,9,10}
# print(x.union(y))

# class A:
#     def __init__(self,v):
#         self._value=v

#     def show(self):
#         print(f"value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10 * self._value
    
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value=new_value/10


# a=A(5)
# a.show()
# print(a.ten_value)
# a.ten_value=9
# print(a.ten_value)


# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def demo(x):
#     time.sleep(5)
#     return x*2

# print(demo(6))
# print("its for 6")
# print(demo(7))
# print("its for 7")
# print(demo(8))
# print("its for 8")

# print(demo(6))
# print("its for 6")
# print(demo(7))
# print("its for 7")
# print(demo(8))
# print("its for 8")
# print(demo(2))
# print("its for 2")

# list=[i for i in range(100)if i%2==0]
# print(list)

# dict={i:f"item{i}" for i in range(100)}
# print(dict)


# set={toy for toy in ["toy1","toy2","toy1","toy2","toy1","toy2"]}
# print(set)

# even=(i for i in range(100)if i%2==0)
# # print(even.__next__())
# # print(even.__next__())
# # print(even.__next__())
# for y in even:
#     print(y)

# x=int(int(input("enter the value of x")))
# if x%2==0:
#     print("True")
# else:
#     print("False")

"numpy"

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# print(a.shape)
# print(a.size)
# print(a.dtype)


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# list=[1,2,3,4,5]
# x=np.zeros(list)
# y=np.ones(list)
# print(x)
# print(y)

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr[0:,])

# import numpy as np

# a=np.array([1,2,3,4,5,6])
# print(a[2])

import numpy as np 
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(a.reshape(3,4))
# print(a.reshape(-1, 3))
