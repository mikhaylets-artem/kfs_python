import math
import random
#class People :
#    def p(self):    
#        print(f"Name : {p1.name} , age : {p1.age} ,  id : {p1.id}")
#a = (input('введите имя'))
#e = (input('введите возраст'))
#p = (input('введите вашу страну'))
#p1=People()
#p1.name=a
#p1.age=e
#p1.id=p
#p1.p()
#class Staz:
#    def info(self,m):
#        print(m-self.year)
#p1=Staz()         
#a = int(input('введите год с которого вы начали работать'))
#p1.year=a
#p1.info(2021)

#class Circle :
#    p = 3.14
#    Circle_v =0 
#    def __init__(self,r):
#        self.r = r
#        Circle.Circle_v += 1   
#   def len_Circle(self):
#        print(f" l ={2*self.p*self.r}")    
#    def square(self):
#        print(f" S= {self.p*self.r**2}")
#a=int(input("введите r"))
#c1=Circle(a)
#c1.len_Circle()
#print(Circle.Circle_v)
#c2=Circle(a)
#c2.square()
#print(Circle.Circle_v)

#name= input('Введите ваше имя :  ')
#age = (input('введите возраст : '))
#place_of_birth = (input('введите вашу страну'))
#class Anketa :
#    def __init__(self,name,age,place_of_birth):
#        self.name = name
#        self.age = age
#        self.place_of_birth =place_of_birth 
#        name_check = re.search(r'[a]+e[b]+ d +', self.name)
#        if name_check:
#            print ('email valid')
#        else:
#            print ('email no valid')
#            self.email = input("Enter your email: ")            
#            sys.exit(0)


#def y1(x):
#    if x>-math.pi and x<math.pi/4:
#        return math.cos**2(x-math.pi)
#def y2(x):
#    if x>=0 and x<=2:
#        return math.sqrt(math.fabs(x-5.4))
#def y3(x):
#    if x>1 :
#        return 1/(x-1)
#y1(2)    

class Pif :
    def __init__(self,a,b):
        self.a = a
        self.b=b    
    def s_c(self):
        if a >b :
            print(f" if gep a={a} , kat b={b}  kat c = {math.sqrt((self.a**2)-(self.b**2))}")
        else:
            print('a должно быть > b')
    def s_b(self):
        print(f" if kat a={a} ,kat b={b} gep c = {math.sqrt((self.a**2)+(self.b**2))}")         
a=int(input("введите  a"))
b=int(input("введите  b"))
c1=Pif(a,b)
c1.s_c()
c2=Pif(a,b)
c2.s_b()
