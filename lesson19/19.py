import random
#1
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for i in a:
#    if i<5:
#        print(i)
#    else:
#        print('-')
#2
#k=1
#n=int(input("n= "))
#a=[random.randint(1,15) for i in range(n)]#если от нуля то ноль будет я поставил 1 хотя в условии с нуля это так задумано
#for i in a:
#    k*=i
#print(a,k,a[0],a[-1])
#3
#numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
#for i in numbers:
#    if i%2==0:
#        print(i)
#    elif i==237:
#        print('stop-237')
#        break
#4
#age=int(input("n= "))
#if age<2:
#    print("mladenec")
#elif age>=2 and age<4:
#    print("malish")
#elif age>=4 and age<13:
#    print("rebenok")
#elif age>=13 and age<20:
#    print("podrostok")
#elif age>=20 and age<65:
#    print("vzrozly")
#elif age>=65:
#    print("ded")
#elif age<=0:
#    print('s nachala rodis`')
#5
#neprov_user=['user0','user1','user2','user3','user4']
#prov_user=[]
#while True:
#    n=int(input("введите 1 если хотите выйти и 2 чтоб добавить"))
#    if n==1:
#        break
#        print('break')
#    elif n==2:
#       pop1= neprov_user.pop(0)
#       prov_user.append(pop1)
#       print(prov_user)
#print(prov_user)
#6
#like_eat_me=['pizza', 'falafel', 'carrot cake']
#morozivo=input("morozivo")
#like_eat_friend=like_eat_me[:]
#like_eat_friend.append(morozivo)
#for i in like_eat_me:
#    print("my",i)
#for i in like_eat_friend:
#    print("friend",i)
#print(f"ne my list like eat{like_eat_friend}")
#print(f"my list like eat{like_eat_me}")
#7
#k=0
#lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
#for i in lst:
#    if i<30 and i%3==0:
#         print(i)
#    else:
#        k+=i
#print('suma',k)
#8
#slovar={'a': 2, 'b': 4, 'c': 6, 'd': 8}
#for i in slovar.values():
#    if i>2:
#        print("2<",i)
#9
#s1=["j","h","g","u","k","r"]
#s2=[7,8,9,10,11,12]
#step=int(input("step= "))
#s3={key:value**step for key,value in zip(s1,s2)}
#for i,h in s3.items():
#    print(f"Ya znayu tovy kluch - '{i}',ego znachenie -'{h}'")
#print(s3)
#10
#a={'kr':125,'kiyv':234,'hz':560,'mumba':340}
#del a['kr']
#del a['mumba']
#print(a)
#11
#dic ={'a': 1, 'b': 2, 'c': 3, 'd': 4}
#dic1={i:"event" if dic[i]%2==0 else "odd" for i,j in dic.items()}
#print(dic1)
#12
n=int(input("stroka "))
m=int(input("stolb"))
diap_1=int(input("diapazon random chisel s "))
diap_2=int(input("diapazon random chisel do "))
r=int(input("kakoi hatiti element po stroke "))
t=int(input("kakoi hatiti element po stolbu "))
matrix=[[random.randint(diap_1,diap_2) for j in range(m)] for i in range(n)]
#diagonal=[matrix[i][j] for i in range(n) for j in range(m) if i==j]
#for i in matrix:
#    print("jo"*16,i,"jo"*15)
#print("glav dig",diagonal)
#print("ukazaniy element",matrix[r][t])
