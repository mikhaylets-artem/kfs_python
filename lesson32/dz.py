#class Restaurant:
 #   def __init__(self,restaurant_name,cuisine_type):
 #       self.restaurant_name=restaurant_name
 #       self.cuisine_type=cuisine_type
 #   def describe_restaurant(self):
 #       print(f"Название ресторана: {self.restaurant_name}\nНаправление кухни: {self.cuisine_type}")
 #   def open_restaurant(self):
 #       print(f"Ресторан открыт!")

#x1=Restaurant("Avrora","Italy")
#x1.open_restaurant()
#x1.describe_restaurant()
#x2=Restaurant("Пивная","Пиво")
#x2.describe_restaurant()
#x3=Restaurant("Каннибальная","Человечки")
#x3.describe_restaurant()
    #2
 
class User:
    def __init__(self,first_name,last_name,floor,age,status,user):
        self.first_name=first_name
        self.last_name=last_name
        self.floor=floor
        self.age=age
        self.status=status
        self.user=user
    def describe_user(self):
        print(f"\t\tBIO:\n\tfirst name: {self.first_name.title()}\n\tlast name: {self.last_name.title()}\n\tfloor: {self.floor.title()}\n\tage: {self.age}\n\tstatus: {self.status.title()}")
    def greet_user(self):
        print(f"hello,{self.user}!")
u=input("u= ")
x1=User("Den","Komarov","Laminat",69,"Zamujem",u.title())
x1.greet_user()
x1.describe_user()
x2=User("Den","Muhov","Derevo",18,"Svoboden",u.title())
x2.greet_user()
x2.describe_user()
x3=User("Den","Shershen","Gay",4,"Linolium",u.title())
x3.greet_user()
x3.describe_user()
