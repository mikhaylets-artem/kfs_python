import random
n=int(input('Введите количество строк: '))
m=int(input('Введите количество столбцов: '))
matrix=[[random.randint(0, 9) for g in range(m)]for i in range(n) ]
for i in matrix:
    print(f"|{i}|")   
d=[matrix[i][g] for i in range(n) for g in range(m) if i==g]
print(f"Diagonal: {d}")
k=int(input('Введите строку, которую хотите вывести: '))
row=[matrix[k-1][g] for g in range(m)]
print(f"Строка {k} ---> {row}")
p=int(input('Введите столбец, который хотите вывести: '))
column=[matrix[i][p-1] for i in range(n)]
print(f"Столбец {p} ---> {column}")
r=int(input('Введите строку конкретного элемента: '))
t=int(input('Введите столбец конкретного элемента: '))
a=[matrix[r-1][t-1]]
print(f'Ваш элемент: {a}')
