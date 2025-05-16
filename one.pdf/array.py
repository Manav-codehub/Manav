# x=int(input("enter the number:-"))
# list=[]

# for i in range(0,x):
#     t=int(input())
#     list+=[t]

# print(list)



# x=int(input("enter the number-:"))
# list=[]
# for i in range(0,x):
#     y=int(input())
#     list+=[y]

# print(list)

# x=int(input("enter the number-:"))
# list=[]
# for i in range(0,x):
#     y=int(input())
#     list+=[y]
# print(list)


# def func(x):
#     i=0
#     n=len(x)
#     while i<n:
#         x[i]=x[i]+1
#         i+=1

# list=[1,2,3,4,5]
# func(list)
# print(list)

# list=[]
# x=int(input("enter the number-: "))

# for i in range(0,x):
#     y=int(input())
#     list.append(y)

# sm=0
# for element in list:
#     sm=sm+element

# print("result is-:",sm)


# x=int(input("enter the numbner-:"))
# list=[]

# for i in range(0,x):
#     y=int(input())
#     list.append(y)

# sm=0
# for element in list:
#     sm=sm+element

# print("result is-:",sm)


# x=int(input("enter the number-:"))
# table=1
# i=1
# while i<=10:
#     table=x*i
#     print(x,"*",i,"=",table)
#     i=i+1


'span of array'
# x=int(input("enter the x:"))
# list=[]
# for i in range(0,x):
#     list.append(int(input()))

# mx=list[i]
# mn=list[i]

# for i in range(0,x):
#     if list[i]>mx:
#         mx=list[i]

#     if list[i]<mn:
#         mn=list[i]

# span=mx-mn
# print("span is ",span)


def rs(lft):
  nt=len(lft)
  ans=[]
  for i in range(0,nt):
    ans.append(0)
    ans[0]=lft[0]
  for i in range(1,nt):
    ans[i]=ans[i-1]+lft[i]
  return ans
      
n=int(input("enter the n"))
list=[]
print("enter the element one by one:")
for i in range(0,n): 
  list.append(int(input()))

sol=rs(list)
print(sol)
