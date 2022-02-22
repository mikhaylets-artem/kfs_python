import random
# 9.4
# class Restaurant:
#    def __init__(self,restaurant_name,cuisine_type,number_served=0):
#        self.restaurant_name=restaurant_name
#        self.cuisine_type=cuisine_type
#        self.number_served=number_served
#    def describe_restaurant(self):
#        print(f"Название ресторана: {self.restaurant_name}\nНаправление кухни: {self.cuisine_type}")
#    def open_restaurant(self):
#        print("Ресторан открыт!")
#    def set_number_served(self,n1):
#        self.number_served=n1
#        print(self.number_served)
#    def increment_number_served(self,n2):
#        self.number_served+=n2
#        print(self.number_served)
# restaurant=Restaurant("Avrora","Italy")
# restaurant.number_served=3
# 5print(restaurant.number_served)
#n1=int(input("n= "))
#n2=int(input("n= "))
# restaurant.set_number_served(n1)
# restaurant.increment_number_served(n2)
# 9.5
#class User:
#    def __init__(self, first_name, last_name, floor, age, status, user,login_attempts):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.floor = floor
#        self.age = age
#        self.status = status
#        self.user = user
#        self.login_attempts = login_attempts
#   def describe_user(self):
#       print(
#           f"\t\tBIO:\n\tfirst name: {self.first_name.title()}\n\tlast name: {self.last_name.title()}\n\tfloor: {self.floor.title()}\n\tage: {self.age}\n\tstatus: {self.status.title()}")

#    def greet_user(self):
#        print(f"hello,{self.user}!")
#    def increment_login_attempts(self):
#        self.login_attempts+=1
#        print(self.login_attempts)
#    def reset_login_attempts(self):
#        self.login_attempts=0
#        print(self.login_attempts)
#x=User(1,1,1,1,1,1,13)
#x.increment_login_attempts()
#x.increment_login_attempts()
#x.increment_login_attempts()
#x.reset_login_attempts()
#x.increment_login_attempts()
#x.increment_login_attempts()
#9.6
#class Restaurant:
#    def __init__(self,restaurant_name,cuisine_type,number_served=0):
#        self.restaurant_name=restaurant_name
#        self.cuisine_type=cuisine_type
#        self.number_served=number_served
#    def describe_restaurant(self):
#        print(f"Название ресторана: {self.restaurant_name}\nНаправление кухни: {self.cuisine_type}")
#    def open_restaurant(self):
#        print("Ресторан открыт!")
#    def set_number_served(self,n1):
#        self.number_served=n1
#        print(self.number_served)
#    def increment_number_served(self,n2):
#        self.number_served+=n2
#        print(self.number_served)

#class IceCreamStand(Restaurant):
#    def __init__(self, restaurant_name, cuisine_type, number_served=0,flavors=[]):
#        self.flavors=flavors
#        super().__init__(restaurant_name, cuisine_type, number_served)
#    def jojo(self):
#        for i in self.flavors:
#            print(i)
#restaurant=IceCreamStand("Avrora","Italy",13,["jojo","soso",'bobo'])
#restaurant.jojo()
#9.7
#class User:
#    def __init__(self, first_name, last_name, floor, age, status, user,login_attempts):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.floor = floor
#        self.age = age
#        self.status = status
#        self.user = user
#        self.login_attempts = login_attempts
#    def describe_user(self):
#        print(f"\t\tBIO:\n\tfirst name: {self.first_name.title()}\n\tlast name: {self.last_name.title()}\n\tfloor: {self.floor.title()}\n\tage: {self.age}\n\tstatus: {self.status.title()}")
#    def greet_user(self):
#        print(f"hello,{self.user}!")
#    def increment_login_attempts(self):
#        self.login_attempts+=1
#        print(self.login_attempts)
#    def reset_login_attempts(self):
#        self.login_attempts=0
#        print(self.login_attempts)
#class Admin(User):
#    def __init__(self, first_name, last_name, floor, age, status, user, login_attempts,privileges=[]):
#        self.privileges=privileges
#        super().__init__(first_name, last_name, floor, age, status, user, login_attempts)
#    def show_privilegas(self):
#       for i in self.privileges:
#           print(i)
#x=Admin(1,1,1,1,1,1,1,["jojo",'jojo','jojo'])
#x.show_privilegas()
#9.8
class User:
    def __init__(self, first_name, last_name, floor, age, status, user,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.floor = floor
        self.age = age
        self.status = status
        self.user = user
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"\t\tBIO:\n\tfirst name: {self.first_name.title()}\n\tlast name: {self.last_name.title()}\n\tfloor: {self.floor.title()}\n\tage: {self.age}\n\tstatus: {self.status.title()}")
    def greet_user(self):
        print(f"hello,{self.user}!")
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)
class Privileges():
    def __init__(self):
        pass
    def show_privileges(self,privileges):
        self.privileges=privileges
        for i in self.privileges:
            print(i)

class Admin(User):
    def __init__(self, first_name, last_name, floor, age, status, user, login_attempts):
        super().__init__(first_name, last_name, floor, age, status, user, login_attempts)
        self.privileges=Privileges()
x1=Admin(1,1,1,1,1,1,1)
n=int(input('n= '))
x1.privileges.show_privileges([random.randint(-10,10) for i in range(n+1)])

#class Privileges():
#    def __init__(self):
#        self.privileges=[1,2,3]
#    def show_privileges(self):
#        for i in self.privileges:
#            print(i)

#class Admin(User):
#    def __init__(self, first_name, last_name, floor, age, status, user, login_attempts):
#        super().__init__(first_name, last_name, floor, age, status, user, login_attempts)
#        self.privileges=Privileges()
#x1=Admin(1,1,1,1,1,1,1)
#x1.privileges.show_privileges()
