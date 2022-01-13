like_eat_me=['pizza', 'falafel', 'carrot cake']
morozivo=input("morozivo")
like_eat_friend=like_eat_me[:]
like_eat_friend.append(morozivo)
for i in like_eat_me:
    print("my",i)
for i in like_eat_friend:
    print("friend",i)
print(f"ne my list like eat{like_eat_friend}")
print(f"my list like eat{like_eat_me}")
