# import threading
# import time #type:ignore
# from concurrent.futures import ThreadPoolExecutor


# def function1(second):
#     time.sleep(second)
#     print(f"sleep for {second} second")
#     return f"{second}"

# def hello():
#    time1=time.perf_counter()
#    function1(3)
#    function1(6)
#    function1(9)
#    time2=time.perf_counter()
#    print(time2-time1)


#    time1=time.perf_counter()

#    t1=threading.Thread(target=function1,args=[3])
#    t2=threading.Thread(target=function1,args=[6])
#    t3=threading.Thread(target=function1,args=[9])


#    t1.start()
#    t2.start()
#    t3.start()

#    t1.join()
#    t2.join()
#    t3.join()

#    time2=time.perf_counter()
#    print(time2-time1)


# with ThreadPoolExecutor() as executor:
#     future1 = executor.submit(function1,3)
#     future2 = executor.submit(function1,6)
#     future3 = executor.submit(function1,9)
    
#     print(future1.result())
#     print(future2.result())
#     print(future3.result())

#    x=[2,4,6,8,10]
#    result=executor.map(function1,x)
#    for i in result:
#     print(i)



# import asyncio
# import requests

# async def function1():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=GvntOdvz&id=CF2F957EE1FCB4E3266BAD63ECBC2A44414F8C3D&thid=OIP.GvntOdvz80txbfbW4rz2kAHaEo&mediaurl=https%3a%2f%2fwww.pixelstalk.net%2fwp-content%2fuploads%2f2016%2f06%2fNature-Wallpaper.jpg&exph=1200&expw=1920&q=images+of+nature&simid=607992551938340317&FORM=IRPRST&ck=1860481B165009D4D5BB66FF00A87D86&selectedIndex=0&itb=0&idpp=overlayview&ajaxhist=0&ajaxserp=0'
#     r = requests.get(url)

#     with open('some_file1.pdf', 'wb') as f:
#       f.write(r.content)
#       print("function1")
# async def function2():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=jHvTOSF7&id=D05A5411EA64B4C5CC975FE2F421AACA3528F5D7&thid=OIP.jHvTOSF7924Ah63W7mozxQHaEo&mediaurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR.8c7bd339217bf76e0087add6ee6a33c5%3Frik%3D1%252fUoNcqqIfTiXw%26riu%3Dhttp%253a%252f%252fthewowstyle.com%252fwp-content%252fuploads%252f2015%252f01%252fnature-images..jpg%26ehk%3D%252fG27fwqbQI%252fi%252bxgGclM1BHuObngpvsp27tc36F59T9c%253d%26risl%3D%26pid%3DImgRaw%26r%3D0&exph=1800&expw=2880&q=images+of+nature&simid=608020001075323423&FORM=IRPRST&ck=87EF591D16C93AA71BE914218AFEE99F&selectedIndex=3&itb=0&cw=1339&ch=666&ajaxhist=0&ajaxserp=0'
#     r = requests.get(url)

#     with open('some_file2.pdf', 'wb') as f:
#       f.write(r.content)
#       print("function2")
# async def function3():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=MCLzVoEx&id=C06EBA7B9EE8E12CF45CA8A219854172E8EABA41&thid=OIP.MCLzVoExgXPyNi_V5gb1AwHaE7&mediaurl=https%3A%2F%2Fwww.pixelstalk.net%2Fwp-content%2Fuploads%2F2016%2F08%2FBackground-Beautiful-Nature-Full-HD.jpg&exph=1728&expw=2600&q=images+of+nature&simid=608015091913999628&FORM=IRPRST&ck=17A8915D18930E2611B87588290E1942&selectedIndex=6&itb=0&cw=1339&ch=666&ajaxhist=0&ajaxserp=0'
#     r = requests.get(url)

#     with open('some_file3.pdf', 'wb') as f:
#       f.write(r.content)
#       print("function3")
# async def function4():
#     url = 'https://www.bing.com/images/search?view=detailV2&ccid=I4X%2FilJ5&id=469DE7E47B417E8C1210EDC2E2D8CBAD186FC602&thid=OIP.I4X_ilJ5O8dMg1yrVXovmQHaEo&mediaurl=https%3A%2F%2Fwallup.net%2Fwp-content%2Fuploads%2F2016%2F01%2F111509-landscape-nature.jpg&exph=1600&expw=2560&q=images+of+nature&simid=608023613127928365&FORM=IRPRST&ck=1D2452E46C1CA9B339C38CFFD771DD88&selectedIndex=11&itb=0&cw=1339&ch=666&ajaxhist=0&ajaxserp=0'
#     r = requests.get(url)

#     with open('some_file4.pdf', 'wb') as f:
#       f.write(r.content)
#       print("function4")

# async def main():
#     # l=await asyncio.gather(
#     #     function1(),
#     #     function2(),
#     #     function3(),
#     #     function4(),
#     # )
#     # print(l)
#     x=asyncio.create_task(function1())
#         # await function1()
#     await function2()
#     await function3()
#     await function4()

# asyncio.run(main())


# import multiprocessing
# import time
# import math 

# result_a=[]
# result_b=[]
# result_c=[]

# def make_calculation_one(numbers):
#     for number in numbers:
#         result_a.append(math.sqrt(number**5))

# def make_calculation_two(numbers):
#     for number in numbers:
#         result_b.append(math.sqrt(number**10))

# def make_calculation_three(numbers):
#     for number in numbers:
#         result_c.append(math.sqrt(number**15))


# if __name__=='__main__':
    
#     number_list=list(range(5000000))

    
    # p1=multiprocessing.Process(target=make_calculation_one,args=(number_list,))
    # p2=multiprocessing.Process(target=make_calculation_two,args=(number_list,))
    # p3=multiprocessing.Process(target=make_calculation_three,args=(number_list,))
    # start=time.time()
    # p1.start()
    # p2.start()
    # p3.start()
    # end=time.time()
    # print(end-start)


    # tem_a=result_a
    # tem_b=result_b
    # tem_c=result_c



    # start=time.time()
    # make_calculation_one(number_list)
    # make_calculation_two(number_list)
    # make_calculation_three(number_list)
    # end=time.time()
    # print(end-start)

    # print(tem_a==result_a)
    # print(tem_b==result_b)
    # print(tem_c==result_c)




# import multiprocessing
# import time
# import math

# result_a=[]
# result_b=[]
# result_c=[]

# def make_calculation_one(numbers):
#     for number in numbers:
#       result_a.append(math.sqrt(number**5))


# def make_calculation_two(numbers):
#     for number in numbers:
#       result_b.append(math.sqrt(number**10))

# def make_calculation_three(numbers):
#     for number in numbers:
#       result_c.append(math.sqrt(number**15))

# if __name__=='__main__':
   
#    number_list=list(range(5000000))
   
#    p1=multiprocessing.process(target=make_calculation_one,args=(number_list,))
#    p2=multiprocessing.process(target=make_calculation_two,args=(number_list,))
#    p3=multiprocessing.process(target=make_calculation_three,args=(number_list,))
#    start=time.time()
#    p1.start()
#    p2.start()
#    p3.start()
#    end=time.time()
#    print(end-start)

#    tem_a=result_a
#    tem_b=result_b
#    tem_c=result_c




#    start=time.time()
#    make_calculation_one(number_list)
#    make_calculation_two(number_list)
#    make_calculation_three(number_list)
#    end=time.time()
#    print(end-start)

#    print(tem_a==result_a)
#    print(tem_b==result_b)
#    print(tem_c==result_c)

# def add(x,y):
#     return x+y

# if __name__=='__main__':
#   print(add(5,5))
   


# class employee:
#     def __init__(self,n,s,w):
#         self.name=n
#         self.salary=s
#         self.work=w

#     def show_detail(self):
#         print(f"the name of employee is {self.name} and earns {self.salary} with {self.work} role")

#     @classmethod
#     def from_dash(cls,string):
#         x=string.split("-")
#         print(x)
#         return cls(x[0],x[1],x[2])
        

    

# e1=employee("dddw",4849898,"e9e2")
# e2=employee("manav",500000,"ds")

# e3=employee.from_dash("manav-500000-data scientist")
# print(e3)


# Open the file in read mode
with open("data.txt", "r") as f:
    # Initialize a counter
    line_count = 0
    
    # Iterate over each line in the file and increment the counter
    for line in f:
        line_count += 1

# Print the total line count
print("Number of lines:", line_count)

































