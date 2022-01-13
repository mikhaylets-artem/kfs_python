#class Human:
#    pass
#p_1=Human()
#p_1.name='artemka'
#p_1.surname='ne skaju'
#p_1.place_of_birth='Ukraine'
#p_2=Human()
#p_2.name='yarik'
#p_2.surname='gladik'
#p_2.place_of_birth='Ukraine'
#print(f'Human_1:\nИмя: {p_1.name}\nФамилия: {p_1.surname}\nМесто рождение: {p_1.place_of_birth} ')
#print(f'Human_2:\nИмя: {p_2.name}\nФамилия: {p_2.surname}\nМесто рождение: {p_2.place_of_birth} ')

#class Human:
#    def info(self,n):
#        for i in range(n):
#            print(f'\tHuman_1:\nИмя: {self.name}\nФамилия: {self.surname}\nМесто рождение: {self.place_of_birth} ')
#n=int(input('Введите количество выводов для первого человека: '))
#n_1=int(input('Введите количество выводов для второго человека: '))
#p_1=Human()
#p_1.name='artemj'
#p_1.surname='mikhaylets'
#p_1.place_of_birth='Ukraine'
#p_2=Human()
#p_2.name='Yarick'
#p_2.surname='Gladishev'
#p_2.place_of_birth='Ukraine'
#p_1.info(n)
#p_2.info(n_1)

#class Human:
#    def rez_age(self, m):
#        return m-self.year
#year=int(input('Введите год, на сегодняшний момент: '))
#p_1=Human()
#p_1.name='artem'
#p_1.surname='jojo'
#p_1.place_of_birth='Ukraine'
#p_1.year=2006
#p_2=Human()
#p_2.name='Yarick'
#p_2.surname='Gladishev'
#p_2.place_of_birth='Ukraine'
#p_2.year=2005
#print(f'Возраст первого человека: {p_1.rez_age(year)}')
#print(f'Возраст второго человека: {p_2.rez_age(year)}')

class Human:
    def __init__(self, name, surname, place_of_birth, age, year):                #Должна стоять всегда первой
        self.name=name
        self.surname=surname
        self.place_of_birth=place_of_birth
        self.age=age
        self.year=year
    def info(self):
        print(f'Human:\n\tИмя: {self.name}\n\tФамилия: {self.surname}\n\tМесто рождение: {self.place_of_birth}\n\tВозраст: {self.age}\n\tГод рождения:{self.year}')

p_1=Human('Den', 'Dmitriev', 'UA', 24, 1997)

p_2=Human('Oleg', 'Putin', 'UA', 64, 1998)

p_1.info()
p_2.info()
