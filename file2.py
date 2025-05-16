"1"
# def recursion(arr):
#     new_recusion=[]
#     if(arr==0 or arr==1):
#         return 0
#     else:
#         new_recusion.append(recursion)
# print(recursion([5, 10, 15, 20]))

# import seaborn as sb
# import matplotlib.pyplot as plt
# import pandas as pd

# y=sb.load_dataset("exercise")
# print(y)
# y1=sb.lineplot(x="pulse",y="time",data=y)
# print(y1)
# plt.show()
"2"


# import seaborn as sb
# import matplotlib.pyplot as plt
# y=sb.load_dataset("titanic")
# print(y)
# sb.histplot(x="fare",kde=True,data=y)
# plt.show()



# import time

# def for_loop():
#     i = 0
#     for i in range(10**7):  # 10 million for reasonable timing
#         pass

# def while_loop():
#     i = 0
#     while i < 10**7:
#         i += 1

# # Measure for loop time
# start_for = time.perf_counter()
# for_loop()
# end_for = time.perf_counter()

# # Measure while loop time
# start_while = time.perf_counter()
# while_loop()
# end_while = time.perf_counter()

# # Calculate execution times
# time_for = end_for - start_for
# time_while = end_while - start_while

# # Print results
# print(f"For Loop Execution Time: {time_for:.6f} seconds")
# print(f"While Loop Execution Time: {time_while:.6f} seconds")

# # Compare
# if time_for < time_while:
#     print("For loop is faster!")
# elif time_for > time_while:
#     print("While loop is faster!")
# else:
#     print("Both loops have similar execution times.")


import matplotlib.pyplot as plt

products = ['A', 'B', 'C', 'D']
sales = [150, 200, 300, 250]
plt.bar(products,sales,color=['red', 'blue', 'green', 'orange'])
plt.show()