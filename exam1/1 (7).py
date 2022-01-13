k=0
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for i in lst:
    if i<30 and i%3==0:
         print(i)
    else:
        k+=i
print('suma',k)
8
slovar={'a': 2, 'b': 4, 'c': 6, 'd': 8}
for i in slovar.values():
    if i>2:
        print("2<",i)
