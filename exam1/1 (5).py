neprov_user=['user0','user1','user2','user3','user4']
prov_user=[]
while True:
    n=int(input("введите 1 если хотите выйти и 2 чтоб добавить"))
    if n==1:
        break
        print('break')
    elif n==2:
       pop1= neprov_user.pop(0)
       prov_user.append(pop1)
       print(prov_user)
print(prov_user)
