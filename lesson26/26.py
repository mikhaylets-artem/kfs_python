#1
import math
#x=int(input("x= "))
#if x>(-math.pi) and x<math.pi/4:
#    y=-math.cos(x-math.pi)**2
#elif x>=math.pi/4 and x<=1:
#    y=math.sqrt(abc(x+1))
#elif x>1:
#    y=1/(x-1)
#else:
#    print("error")
#print(y)
#2
#z=0
#x=int(input("x= "))
#y=int(input("y= "))
#if abs(x*y)<1 and x<0:
#    z=(x+y)/(math.e**x*y)
#elif 2<x and y<=0:
#    z=-(math.log(x))**2
#elif y>0 and x>=0 and x<=2:
#    z=math.log10(math.sqrt(y))
#else:
#    print("error")
#print(z)
#3
#x=int(input("y= "))
#if x>=0 and x<2:
#    y=math.sqrt(abs(x-5.4))
#elif x>=2 and x<8:
#    y=math.atan(x**2)
#elif x>=8:
#     y=math.log10(abs(x-7.8))
#else:
#    print(error)
#print(y)
class Human:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        print("Human created")
    def hello(self):
        print(f"{self.name} hello")
class Student(Human):
    def study(self):
        print(f"{self.name} study")
class Teacher(Human):
    def teach(self):
        print(f"{self.name} teach web")
s1=Teacher("Renat","Dmitriev")
s1.teach()
s2=Student("misha","rjopa")
s2.study()
