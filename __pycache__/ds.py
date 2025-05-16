import numpy as np
# a=np.array([[1,2,3,4,5]])
# x=np.array([1,2,3])
# y=np.array([4,5,6])
# print(x+y)

"setting dtype"
# a=np.array([1,2,3],np.int8)
# print(a)

"element acessing"
# a=np.array([[1,2,3,4,5]])
# print(a[1,2])

"shape"
# x=np.array([[1,2,3,4,5]])
# print(x.shape)

"checking dtype"
# print(a.dtype)

"changing element"
# a[0,1]=45
# print(a)

"Conversion from other Python structures (i.e. lists and tuples)"
# hello=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(hello)
# print(hello.shape)
# print(hello.size)
# print(hello.dtype)

"Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)"
# hello=np.zeros((2,10))
# print(hello)
# hello1=np.arange(20)
# print(hello1)
# hello2=np.linspace(1,5,10)
# print(hello2)
# hello3=np.empty((4,6))
# print(hello3)
# hello4=np.empty_like(a)
# print(hello4)
# hello5=np.identity(45)
# print(hello5)
# print(hello5.shape)
# hello6=np.arange(90)
# print(hello6)
# hello6.reshape(3,30)
# print(hello6)
# print(hello6.ravel)
"asix"
# x=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
# x1=np.array(x)
# print(x1.sum(axis=0))
# print(x1.sum(axis=1))
# print(x1.T)
# print(x1.flat)
# for i in x1.flat:
#     print(i)
# print(x1.ndim)
# print(x1.nbytes)
# x2=np.array([1,2,3444,55])
# print(x2.argmax())
# print(x2.argmin())
# print(x2.argsort())
# x3=np.array([[3232,45,6],[764,67,5666],[123,346768,5]])
# print(x3)
# print(x3.argmin())
# print(x3.argmax())
# print(x3.argsort())
# x4=np.array([[233,34,422],[3123,654,345],[233,675,745]])
# print(x4-x3)
# print(type(np.where(a>4)))

"practice"
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A*B)
