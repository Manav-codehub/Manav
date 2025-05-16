"1"
# x=int(input("enter the number-:"))
# list=[]

# for i in range(0,x):
#     t=int(input())
#     list+=[t]
# print(list)

"2"
# def func(x):
#     i=0
#     y=len(x)
#     while i<y:
#         x[i]=x[i]+1
#         i=i+1

# list=[1,2,3,4,5]
# func(list)
# print(list)


"3"
# x=int(input("enter the number-:"))
# list=[]

# for i in range(0,x):
#     t=int(input())
#     list.append(t)

# sum1=0
# for el in list:
#     sum1=sum1+el

# print(f"sum is {sum1}")

"4"

x=int(input("enter the number-:"))
list=[]
for i in range(0,x):
    list.append(int(input()))

mx=list[i]
mn=list[i]
for i in range(0,x):
   if list[i]>mx:
      mx=list[i]
   if list[i]<mn:
      mn=list[i]

span=mx-mn
print(f"span is {span} ")