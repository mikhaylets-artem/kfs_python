import random
k=1
n=int(input("n= "))
a=[random.randint(1,15) for i in range(n)]#если от нуля то ноль будет я поставил 1 хотя в условии с нуля это так задумано
for i in a:
    k*=i
print(a,k,a[0],a[-1])
