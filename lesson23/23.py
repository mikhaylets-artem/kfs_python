#def fun(x):
#    return x
#x=int(input('Введите занчение: '))
#t=fun(x)

#print(t)
#u = lambda x:x
#x=int(input('Введите значение: '))
#print(u)

#x=int(input('Введите число и получите следующее: '))
#fun=lambda x:x+1
#print(fun(x))

#a=int(input('Введите число: '))
#b=int(input('Введите второе число: '))
#s=lambda a,b:a*b
#print(s(a,b))

#a=int(input('Введите первое число: '))
#b=int(input('Введите второе число: '))
#s=lambda a,b:a+b
#s_0=lambda a,b:a-b
#s_1=lambda a,b:a*b
#s_2=lambda a,b:a/b
#print(f'Сумма: {s(a,b)}')
#print(f'Разница: {s_0(a,b)}')
#print(f'Произведение: {s_1(a,b)}')
#print(f'Деление: {s_2(a,b)}')

#lst=[1, 5, 78, 21, 66, 59, 60]
#h=list(filter(lambda x:x%2==0, lst))
#print(h)

lst=['Renatik', 'Yaroslavchik', 'Mishania', 'Danochka', 'Nellochka', 'Denchik']
end=list(filter(lambda n:len(n)<8, lst))
print(end)
