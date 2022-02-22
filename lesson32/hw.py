#from modul import *
#class Rectangle:
#    def __init__(self,width,height):
#        self.width=width
#        self.height=height
#    def mat_operation(self):
#        return self.width*self.height
#x=Rectangle(3,2)
#print(x.mat_operation())
#2
#class Jojo():
#    def __init__(self):
#        pass
#    def receivingx(self):
#        self.name=n
#    def registrx(self):
#        print(f"{self.name.title()}")
#n=input()
#x=Jojo()
#x.receivingx()
#x.registrx()
#3
#class Shop:
#    def __init__(self,shop_name,store_type):
#        self.shop_name=shop_name
#        self.store_type=store_type
#        self.number_of_units=0
#    def open_shop(self): 
#        print(f"Ресторан открыт!")
#    def describe_shop(self):
 #       print(f"{self.shop_name} {self.store_type}")
 #   def set_number_of_units(self):
 #       self.number_of_units=n
 #       print(self.number_of_units)
 #   def increment_number_of_units(self):
 #       self.number_of_units+=g
 #       print(self.number_of_units)
#store=Shop("hjj","jkk")
#store2=Shop("hjj2","jkk2")
#n=int(input())
#g=int(input())
    #a
#print(store.shop_name)
#print(store.store_type)
#store.open_shop()
#store.describe_shop()
    #
#b
#store2.describe_shop()
#
    #c
#print(store.number_of_units)
#store.number_of_units=23
#print(store.number_of_units)
    #
#d
#store.set_number_of_units()
#store.increment_number_of_units()
#
    #e
#class Discount(Shop):
#    def __init__(self,shop_name,store_type,discount_products):
#        super().__init__(shop_name,store_type)
#        self.discount_products=list("product" for i in range(10))
#    def get_discount_ptoducts(self):
#        print(self.discount_products)
#store_discount=Discount(1,2,"")
#store_discount.get_discount_ptoducts()
    #
#4
class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def minm(self):
        print(f"Your balance: {self.balance}")
        minus=int(input("Сколько нужно снять: "))
        if self.balance>=minus:
            self.balance-=minus
        else:
            print("Недостаточно средств!")
        print(f"У вас осталось: {self.balance}")
        
    def plum(self):
        print(f"Your balance: {self.balance}")
        plum=int(input("Насколько нужно пополнить: "))
        self.balance+=plum
        print(f"Your balance: {self.balance}")
x=Bank("Igor",5000)

while True:
    print(f"Здравствуйте,{x.name}!")
    j=int(input("1-Снять 2-Пополнить 3-Выйти с программы "))
    if j==1:
        x.minm()
    elif j==2:
        x.plum()
    elif j==3:
        print("Выход успешно выплонен,хорошего дня!")
        break
    else:
        print("Введите одно из указываемых чисел!")
