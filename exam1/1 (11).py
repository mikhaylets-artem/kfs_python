dic ={'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic1={i:"event" if dic[i]%2==0 else "odd" for i,j in dic.items()}
print(dic1)
