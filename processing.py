"1"
# import multiprocessing

# def number_square(n):
#     print(f"Square of {n} is {n*n}")

# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]

#     # Create a process for each number
#     processes = []
#     for number in numbers:
#         process = multiprocessing.Process(target=number_square, args=(number,))
#         processes.append(process)
#         process.start()

#     # Wait for all processes to complete
#     for process in processes:
#         process.join()

#     print("Processes finished")

"2"
# import multiprocessing

# def square(x):
#     print(f"square of {x} is{x*x}")

# if __name__=="__main__":
#     numbers=[1,2,3,4,5]
#     output=[]
#     for number in  numbers:
#        p=multiprocessing.Process(target=square,args=(number,))
#        output.append(p)
#        p.start()

#     for p in output:
#        p.join()

# print("programm finished")
       

# import multiprocessing
# import time

# def funtion1():
#     print("hello from process 1 start ")
#     time.sleep(2)
#     print("hello from process 1 complete")

# def funtion2():
#     print("hello from process 2 start ")
#     time.sleep(4)
#     print("hello from process 2 complete")

# def funtion3():
#     print("hello from process 3 start ")
#     time.sleep(6)
#     print("hello from process 3 complete")


# def funtion4():
#     print("hello from process 4 start ")
#     time.sleep(8)
#     print("hello from process 4 complete")

# if __name__=="__main__":
#     p1=multiprocessing.Process(target=funtion1)
#     p2=multiprocessing.Process(target=funtion2)
#     p3=multiprocessing.Process(target=funtion3)
#     p4=multiprocessing.Process(target=funtion4)

#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()

#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()

# print("all process completed")
    

# import multiprocessing

# def factorial(c):
#     print(f"factorial of c is {c*c}")
# c=[1,2,3,4,5]
# if __name__=="__main__":
#     processes=[]
#     for i in c:
#         p=multiprocessing.Process(target=factorial,args=(i,))
#         processes.append(p)
#         p.start()
#     for process in processes:
#         p.join()

import os 
print(os.remove("numpy.py"))