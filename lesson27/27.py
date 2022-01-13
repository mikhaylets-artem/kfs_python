class Machin:
    def __init__(self,manufacturer,name,mark,maxspeed,fuel,price,):
        self.manufacturer = manufacturer
        self.name= name
        self.mark= mark
        self.maxspeed = maxspeed
        self.fuel=fuel
        self.price=price
        print('machine created')
class Car(Machin) :
    def info_a(self):
        print(f"\n\t\t Manufacturer: {self.manufacturer}\n\t\t Name car: {self.name}\n\t\t Mark: {self.mark}\n\t\t Maxspeed: {self.maxspeed}\n\t\t Fuel: {self.fuel}\n\t\t Price: {self.price} ")
class Yacht(Machin):
    def info_b(self):
        print(f"\n\t\t Manufacturer: {self.manufacturer}\n\t\t Name car: {self.name}\n\t\t Mark: {self.mark}\n\t\t Maxspeed: {self.maxspeed}\n\t\t Fuel: {self.fuel}\n\t\t Price: {self.price}")    
while True :
    n  = int(input('enter 1-car 2-yacht'))
    if n == 1 :
       f = Car("Ilon Mask","Tesla","X",'360 km/h',"electro","140,000$")
       f.info_a()
    elif n ==2 :
       f = Yacht("Nastya Poroshenko","Lodka","Podlodka",'-4 km/h na dno',"Vesla","100$ maximum ")
       f.info_b()
