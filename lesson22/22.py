#def gen():
#    for i in lst_my:
#        yield i   
#lst_my=['a', 'b', 'c', 'd']
#y=gen()
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))

#def gen():
#    yield
#    print('Первый перебор')
#    yield
#    print('Второй перебор')
#    yield
#    print('Третий перебор')
#    yield
#y=gen()
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))

#def gen(n):
#    a,b = 1,0
#    for i in range(n):
#        yield b
#        a+=b
#        b=a+b
#        yield a
#n=int(input('n= '))
#y=gen(n)
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))
#print(next(y))

#def gen():
#    for i in pr_l:
#        yield i
#pr_l=['Python', 'JavaScript', 'C++', 'C', 'Java']
#for v in gen():
#    print(v)

#def gen():
#    for i in kor:
#        yield i
#y=gen()
#lst_n=[4, 16, 64, 256]
#kor=[item**1/2 for item in lst_n]
#g=0
#while g<len(kor):
#    print(next(y))
#    g+=1

def gen():
    i=1
    while True:
        if i>1:
            for g in range(2, i):
                if i%g==0:
                    break
                else:
                    yield i
        i+=1
for a in gen():
    print(a)
