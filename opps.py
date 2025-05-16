"1"
# class Bank_account:
#     balance=0.0
#     def __init__(self,ahn,an,bal,bal2,an2):
#         self.account_holder_name=ahn
#         self.account_number=an
#         self.balance=float(bal)
#         self.balance2=float(bal2)
#         self.account_number2=an2

#     def show(self):
#         print(f"The name of account holder is {self.account_holder_name} and his account number is {self.account_number} with {self.balance} balance")
    
#     def deposit(self):
#         print(f"the deposit amount is {self.balance+self.balance2}")

#     def withdraw(self):
#         print(f"you withdraw {self.balance-self.balance2} ")
    
#     def current(self):
#         print(f"the current balance is {self.balance-self.balance2} ")

#     def transfer(self):
#         print(f"you are tranfer is ammont {self.balance} to {self.account_number2}")
    

# class Bank_account2(Bank_account):
#     pass

# b1=Bank_account("manav",177090870,100.0,50.0,177908223)
# b1.show()
# b1.deposit()
# b1.withdraw()
# b1.current()
# b1.transfer()
# b2=Bank_account2("yuvi",789067578,500.0,100.0,475585875)
# b2.show()
# b2.deposit()
# b2.withdraw()
# b2.current()
# b2.transfer()

"2"
# class Doctor:
    
#     def __init__(self):
#         self.name="shiv"
#         self.specialization="cardiologist"
#         self.available=True

#     def showw(self):
#         print(f"the name of doctor is {self.name} and he is {self.specialization}")

#     def change_availability(self): 
#         self.available=12
#         if self.available> 12:
#             print("Doctor is not available ")
#         elif self.available<12:
#             print("Doctor is available")
#         else:
#             print("time out")

# class Patient:
#     def __init__(self):
#         self.name="joy"
#         self.age=67
#         self.illness="cancer"

#     def show(self):
#         print(f"the name of patient is {self.name} and he is suffering from {self.illness}")

# class Appointment:
#     def __init__(self):
#         self.patient=True
#         self.doctor=True
#         self.appointment_time=6
#     def show2(self):
#         print(f"the time of your treatment is {self.appointment_time}")

# d=Doctor()
# d.showw()
# p=Patient()
# p.show()
# a=Appointment()
# a.show2()
"3"
# class ATM:
#     def __init__(self,ahn,an):
#         self.account_holder_name=ahn
#         self.account_number=an
#         self.balance=50
#         self.balance2=20
        
#     def show(self):
#         print(f"the name of customer is {self.account_holder_name} and his account number is {self.account_number}")

#     def deposit(self):
#         print(f"the deposit amount is{self.balance+self.balance2}")

#     def withdraw(self):
#         print(f"the deposit amount is{self.balance-self.balance2}")

# a=ATM("manav",199803453)
# a.deposit()
# a.withdraw()
# a.show()

"4"
# class vehicle:
#     def __init__(self,ty):
#         self.type=ty
#         self.rental_price=50
#         self.is_rented=False
#     def show(self):
#         print(f"you parked your {self.type} for one day so your total rent is {self.rental_price}")

# class rental_system:
#     def add_vehicle(self):
#         self.vehicle+=1
#         print(f"here is your next vehicle{self.vehicle}")
  
#     def rent_vehicle(self, vehicle_type): 

#         if vehicle_type>50:
#             print("car")
#         else:
#             print("bike")
#     def return_vehicle(self, vehicle_type):
#         if vehicle_type>50:
#             print("car")
#         else:
#             print("bike")
#     def display_available_vehicles(self):
#         print(f"{self.display_available_vehicles}")

# v1=vehicle("car")
# v2=vehicle("bike")
# v1.show()
# v2.show()
# r=rental_system()
# r.add_vehicle(v1)
# r.add_vehicle(v2)

"5"

# class book:
#     def __init__(self,tl,atr,isbn):
#         self.title=tl
#         self.author=atr
#         self.ISBN=isbn
#         self.is_borrowed=False

#     def borrow_book(self):
#         if not self.is_borrowed:
#             self.is_borrowed=True
#             print(f"you have borrowed {self.title}")
#         else:
#             print(f"{self.title} is already borrow")

#     def return_book(self):
#         if self.is_borrowed:
#             self.is_borrowed=False
#             print(f"you have returned {self.title}")
#         else:
#             print(f"{self.title} wasn't returned ")

# class library():
#     def __init__(self):
#         self.books=[]
#     def add_book(self,book):
#         self.books.append(book)
#         print(f"{book.title} by {book.author} added to library")

#     def remove_book(self,book):
#         self.books.remove(book)
#         print(f"{book.title} by {book.author} remove to library")

#     def search_for_book(self,book):
#         self.books.find(book)
#         print(f"{book.title} by {book.author}  is available")


# b1=book("guliver travel1","author1",76895859)
# b2=book("guliver travel2","author2",76895859)
# b3=book("guliver travel3","author3",76895859)
# b4=book("guliver travel4","author4",76895859)

# b1.borrow_book()
# b2.borrow_book()
# b3.borrow_book()
# b4.borrow_book()
    
# b1.return_book()
# b2.return_book()
# b3.return_book()
# b4.return_book()


# l1=library()
# l2=library()
# l3=library()
# l4=library()

# l1.add_book(b1)
# l2.add_book(b2)
# l3.add_book(b3)
# l4.add_book(b4)

# l1.remove_book(b1)
# l2.remove_book(b2)
# l3.remove_book(b3)
# l4.remove_book(b4)

"6"

# class product:
#     def __init__(self,nm,pr,sq):
#         self.name=nm
#         self.price=pr
#         self.stock_quantity=sq

# class shopping_cart(product):
#     def add_product(self):
#         self.product+=1
#         print(f"this product {self.product} is added to cart with {self.price} price with {self.stock_quantity}")

#     def remove_product(self):
#         self.product-=1
#         print(f"this product {self.product} is removed from cart and reduce {self.price} price {self.stock_quantity}")

#     def total_result(self):
#         self.stock_quantity+=1
#         self.price+=self.price
#         print(f"you choose {self.name} to order with {self.stock_quantity} with {self.price}")

# p1=product("macbookair",500,1)
# p2=product("mavbookpro",600,1)
# s1=shopping_cart()
# s2=shopping_cart()

# s1.add_product(p1)
# s2.add_product(p2)

"7"
# class student:
#     def __init__(self,nm,rn):
#         self.name=nm
#         self.roll_number=rn
#         self.list_of_marks={}

#     def percentage(self):
#         self.percentage=0
#         if self.percentage>80:
#             print("A grade")
#         elif self.percentage>60:
#             print("B grade")
#         else:
#             print("C grade")

#         print(f"the name of student is {self.name} and he scores {self.percentage}")
#     try:
#       def total_marks(self):
#           i=0
#           i=i+1
#           self.marks=self.marks+[i]
#     except Exception as e:
#         raise ValueError("you entered wrong value ")
    
# s=student("manav",45,"emglish:78,hindi:93,sst:98,it:89,evs:90")
# s.percentage()
          
"8"
# class movie:
#     def __init__(self,nm,gn,dt):
#         self.name=nm
#         self.genre=gn
#         self.duration=dt
#         self.available_seat=False

# class booking_system(movie):
#     def book_ticket(self):
#         if not self.available_seat:
#             self.available_seat=True
#             print(f"{self.available_seat} seats are available ")
#         else:
#             print(f"{self.available_seat} are already booked")

#     def cancel_ticket(self):
#         if self.available_seat:
#             self.available_seat=False
#             print(f"{self.available_seat} seats are canceled ")
#         else:
#             print(f"{self.available_seat} are still booked ")

#     def available_movie(self,me):
#         self.movie=me
#         if me in (capital"A-Z"):
#             print("movie available")
#         else:
#             print ("not available")

"9"

# class bank:
#     def __init__(self,nm,an,an2,my,ln):
#         self.loan=ln
#         self.name=nm
#         self.account_number=an
#         self.money=my
#         self.account_number2=an2
#     def show(self):
#         print(f"the name of customer is {self.name} and his account number is {self.account_number} and in account {self.account_number2} also with {self.money} and he taken {self.loan}")

#     def tranfer_money(self):
#         print(f"{self.money} in {self.account_number} is tranfered in {self.account_number2}")
    
#     def interest_in_saving_account(self,int1):
#         self.interest=int1
#         if self.loan>1000:
#             print(f"{self.interest}% is your interest")
#         elif self.loan>100000:
#             print(f"{self.interest}% is your interest")

# b1=bank("manav",67397,874874,"27972974324",49483498)
# b2=bank("manav1",68997,3663876,"79432974",8784747)
# b3=bank("manav2",697697,327477,"386387673",83278478)

# b1.show()
# b2.show()
# b3.show()
# b1.tranfer_money(50000,3287632876,898329)

"10"

# class employee:
#     bonus="20%"
#     def __init__(self,nm,sly,dpmt):
#         self.name=nm
#         self.salary=sly
#         self.department=dpmt

#     def yearly_bonus(self):
#         print(f"{self.name}'s yearly bonus is {self.bonus} from {self.department} department ")

#     def yearly_promotion(self):
#         self.promotion=False
#         if not self.promotion:
#             self.promotion=True
#             print("congratulation ! now you are promoted junior to senior ")
#         else:
#             print("sorry ! this year you not get promoted ")

# class manager(employee):
#     def __init__(self):
#         self.managing_team=False
#         super().__init__()
#     def show(self):
#         if not self.managing_team:
#             self.managing_team=True
#             print(f"you are good to manage {self.managing_team} team")

# e1=employee("manav",15,"data science")
# e2=employee("manav1",18,"machine learning")
# e3=employee("manav2",20,"artificial intelligence")

# e1.yearly_bonus()
# e2.yearly_bonus()
# e3.yearly_bonus()

# e1.yearly_promotion()
# e2.yearly_promotion()
# e3.yearly_promotion()

# m1=manager()
# m2=manager()
# m3=manager()

# m1.show(e1)
# m2.show(e2)
# m3.show(e3)

"11"

# class vehicle:
#     def __init__(self,sd):
#         self.speed=sd

#     def move(self):
#         return(f"vehicle is moving from {self.speed}kmph")
        
# class car(vehicle):
#     def move(self):
#         return(f"car is moving from {self.speed}kmph")
    
# v=vehicle(80)
# c=car(50)
# print(v.move())
# print(c.move())

"12"

# class bank_amount:
#     def __init__(self,blc):
#         self.__balance=blc
    
#     def deposit(self):
#         self.deposit+=1
#         print(f"you deposit {self.__balance}")

#     def withdraw(self):
#         self.withdraw-=1
#         if self.money>500:
#            print(f"you are able to  withdraw {self.__balance}")
#         else:
#             print("insufficient balance")

# b=bank_amount(500)
# print(b.deposit(100))
# print(b.withdraw(100))

"13"
# class engine:
#     def __init__(self):
#         self.start=False
   
#     def start_engine(self):
#      if self.start:
#         self.start=True
#         print(f"engine is started")
#      else:
#         print(f"engine is off")

# class car(engine):
#     def engine_1(self):
#        self.engine=float(input("entyer the true or false"))
#        if self.engine==True:
#           print(f"engine ios started ")
#        else :
#           print(f"engine is off")

# e=engine(True)
# print(e.start_engine())


"14"
# class person :
#     def __init__(self,nm,ag):
#         self.name=nm
#         self.age=ag

# class employee:
#     def salary(self,sly):
#       self.salary=sly
#     def show_detail(self):
#        print(f"the name of employee is {person.self.name} and he is {person.self.age} with {self.salary}lpa package")

# class manager(person,employee):
#     def software_team(self):
#         self.performance="50%"
#         self.salary_hike="12%"
    
    
#     def AI_team(self):
#         self.performance="40%"
#         self.salary_hike="18%"

# p=person("manav",100)
# e=employee()
# # m=manager()

# print(e.show_detail())
# # m.show_detail("manav",100,99)

"15"

# class shape:
#     def __init__(self) -> None:
#         pass

# class Circle(shape):
#     def __init__(self,Πr2):
#         self.radius=Πr2
#     def show(self):
#         print(f"the area of circle is{self.radius*self.radius}")

# class Square(Circle):
#     def __init__(self, Πr2,s1,s2):
#         super().__init__(Πr2)
#         self.side1=s1
#         self.side2=s2
#     def show2(self):
#         print(f"the area of circle is {self.side1*self.side2}")
    
# class Rectangle(Square):
#     def __init__(self, Πr2, s1,s2,lh,wh):
#         super().__init__(Πr2, s1, s2)
#         self.length=lh
#         self.width=wh
#     def show3(self):
#         print(f"the area of rectangle is {2*self.length+self.radius}")

# c=Circle(6)
# s=Square(5,5,5)
# r=Rectangle(6,6,6,6,6)
# c.show()
# s.show2()
# r.show3()

"16"

# class bank_account:
#     def __init__(self,initial_balance):
#         self.__balance=initial_balance
#         self.__account_number=55893459

#     def deposit(self,amount):    
#         self.__balance>amount
#         print(f"deposit amount{self.__balance+amount}and current balance is {self.__balance}")

#     def withdraw(self,amount):    
#         self.__balance<amount
#         print(f"withdraw amount{self.__balance-amount}and current balance is {self.__balance}")

#     def checking_balance(self):
#         print(f"the current balance is {self.__balance}")

# b=bank_account(500)
# b.deposit(100)
# b.withdraw(100)
# b.checking_balance()

"17"

# class Author:
#     author="ogggy"
#     def __init__(self,nm,el):
#         self.name=nm
#         self.email=el
#     def show(self):
#         print(f"the name of student is {self.name} and his email is {self.email} ")

# class book(Author):
#     def __init__(self,tl,pc):
#         self.title=tl
#         self.price=pc

#     def book1(self):
#         self.book1
#         if not self.book1:
#             if self.book1==False:
#                 print(f"the name of book is {self.book1} by {self.author} is issued by {self.name}with this email address {self.email}")

#         else:
#             print(f"book is already issued")

# a=Author("manav","xxx@gmail.com")
# a.show()

# b=book("guliver travel","500")
# print(b.book1())

"18"

# class Employee:
#     company_name=0
#     employee_count=0
#     def __init__(self,nm,id,sly):
#         self.name=nm
#         self.id=id
#         self.salary=sly

#     def increment_salary(self,salary2):
#         self.salary>salary2
#         print(f"the name of employee is {self.name} and his salary inrement is {salary2}")

#     def get_employee_info(self):
#         company_name+=1
#         employee_count+=1
#         print(f"the name of employee is {self.name} and his id is {self.id} with {self.salary}package {self.employee_count} os {self.company_name}")
        
# e=Employee("manav",500000,500000)
# # print(e.increment_salary())
# e.get_employee_info("manav",463537,500000,1,1)

"19"


from practice import add,sub,mul

add()
sub()
mul()




        