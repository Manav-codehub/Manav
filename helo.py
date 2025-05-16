# import numpy as np
# x=np.array([1,2,3])
# print(type(x),x)

"using 8 byte integer "
# import numpy as np
# x=np.array([111,222,333],np.int64)
# print(type(x),x)

"index access"
# import numpy as np
# x=np.array([[111,222,333]],np.int64)
# # print(type(x),x)
# print(x[0,1])


"0th row and first column"
# import numpy as np
# x=np.array([[111,222,333]],np.int64)
# print(type(x),x)
# print(x[0,1])


"one row and 3 element"
# import numpy as np
# x=np.array([[111,222,333]],np.int64)
# print(type(x),x)
# print(x.shape)


"dtype of array"
# import numpy as np
# x=np.array([[111,222,333]],np.int64)
# print(type(x),x)
# print(x.dtype)



"changing element"
# import numpy as np
# x=np.array([[111,222,333]],np.int64)
# x[0,1]=45
# print(x)



"difference between list and array "
# import numpy as np
# a=np.array([1,2,3])
# b=np.array([4,5,6])
# # a=[1,2,3]
# # b=[4,5,6]
# print(a*b)

"array creation Conversion from other Python structures (i.e. lists and tuples)"
# import numpy as np 
# listarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(listarray)
# print(listarray.size)
# print(listarray.shape)
# print(listarray.dtype)

# import numpy as np 
# x=np.array({45,45,67})
# print(x,x.dtype)


"Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)"
# import numpy as np 
# zero=np.zeros((2,4))
# print(zero)
# print(zero.shape)
# print(zero.size)
# print(zero.dtype) 

# arg=np.arange(15)
# print(arg)


# lspace=np.linspace(1,50,20)
# print(lspace)


# emp=np.empty((4,6))
# print(emp)

# emp_like=np.empty_like(lspace)
# print(emp_like)


# ide=np.identity(45)
# print(ide)
# print(ide.size)
# print(ide.shape)


# x=np.arange(99)
# print(x.reshape(3,33))
# x.ravel()
# print(x)

"numpy axis"
# x=[[1,2,3],[4,5,6],[7,8,9]]
# arr=np.array(x)
# print(arr)

# print(arr.sum(axis=0))
# print(arr.sum(axis=1))
# print(arr.T)
# arr.flat
# for i in arr.flat:
#     print(i)

# print(arr.ndim)
# print(arr.size)
# print(arr.nbytes)

# x2=np.array([1,2,3,4,5,6])
# print(x2.argmax())
# print(x2.argmin())
# print(x2.argsort())
"argsort give us number in maximum order "

# print(arr.argsort())
# print(arr.argmin(axis=0))
# print(arr.argmax(axis=0))

# print(arr.argmin(axis=1))
# print(arr.argmax(axis=1))

# print(x2.ravel(6,1))
# a=np.array([[2,2],[4,4],[6,6]])
# b=np.array([[1,1],[3,3],[5,5]])

# a=([[2,2],[4,4],[6,6]])
# b=([[1,1],[3,3],[5,5]])

# print(a*b)
# print(np.sqrt(x2))
# arr=x2.sum()
# arr=x2.max()
# print(type(np.where(x2>5)))
# print(np.count_nonzero(x2))
# print(np.nonzero(x2))

"size taken by python and numpy"
# import sys
# py_ar=[1,2,3,4,5]
# np_ar=np.array(py_ar)
# print(sys.getsizeof(1)*len(py_ar))

# print(np_ar.itemsize*np_ar.size)


"practise"

# import numpy as np

# a=np.array([1,2,3,4,5,6,7,8,9,10])
# print(np.max(a))
# print(np.mean(a))
# print(np.sum(a))

import numpy as np
a=np.array([10,20,30,40,50])
mask=a>25
print(a[mask])