import random
import math
#1
#a = [1,1,2,3,5,8,13,21,34,55,89]
#b = [i for i in a if i<5]
#print(b)
#2
#n = int(input('Kol-vo chisel'))
#q = [random.randint(0,16) for w in range(n)]
#print(q)
#p = 1
#for w in q:
#    p *= w
#print(w)
#3
#lst=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
#for i in lst:
#    if i==237:
#        break
#    elif i%2==0:
#        print(i)
#4
#users=['user_1', 'user_2', 'user_3', 'user_4']
#ver_users=[]
#print(f'Неверефицированые пользователи: {users}')
#print(f'Верефецированые пользователи: {ver_users}')
#print(f'\t\t\tПроверяем пользователя...')
#while users:
#    ver=users.pop(0)
#    ver_users.append(ver)
#print(f'Неверефицированые пользователи: {users}')
#print(f'Верефецированые пользователи: {ver_users}')
#5
#a=['burger', 'pizza', 'sushi']
#b=a[:]
#print(a)
#print(b)
#c=str(int('Мороженое: '))
#b.append(c)
#print(a)
#print(b)
#6
#lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
#s=0
#for i in lst:
#    if i<30 and i%3==0:
#        print(i)
#    else:
#        s+=i
#print(f"Summa: {s}")
#7
#dct={
#    'a':2,
#    'b':4,
#    'c':8,
#    'd':10
#    }
#dct_g={i:j for i, j in dct.items() if j>2}
#print(dct_g)
#for i in dct.values():
#    if i>2:
#       print(i)
#8
#n=int(input('Введите степень в которую хотите возвести: '))
#key=["a", "d", "c"]
#value=[1, 2, 3]
#dct={k:v**n for k, v in  zip(key, value)}
#print(dct)
#9
#dct = {
#    'a': 1,
#    'b': 2,
#    'c': 3,
#    'd': 4
#    }
#dct_s={k:['even' if v%2==0 else 'odd'] for k, v in dct.items()}
#print(dct_s)
#10
#import random
#n=int(input('Введите количество строк: '))
#m=int(input('Введите количество столбцов: '))
#matrix=[[random.randint(0, 9) for g in range(m)]for i in range(n) ]
#for i in matrix:
#    print(f"|{i}|")
#d=[matrix[i][g] for i in range(n) for g in range(m) if i==g]
#print(f"Diagonal: {d}")
#k=int(input('Введите строку, которую хотите вывести: '))
#row=[matrix[k-1][g] for g in range(m)]
#print(f"Строка {k} ---> {row}")
#p=int(input('Введите столбец, который хотите вывести: '))
#column=[matrix[i][p-1] for i in range(n)]
#print(f"Столбец {p} ---> {column}")
#r=int(input('Введите строку конкретного элемента: '))
#t=int(input('Введите столбец конкретного элемента: '))
#a=[matrix[r-1][t-1]]
#print(f'Ваш элемент: {a}')
