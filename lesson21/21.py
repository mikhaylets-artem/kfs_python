class Bot:
    def __init__(self,name,age,country,city,about_you):
        self.name=name
        self.age=age
        self.country=country
        self.city=city
        self.about_you=about_you
    def form(self):
        print(f'Ваша анкета выглядит так:\n\tИмя: {self.name}\n\tВозраст: {self.age}\n\tСтрана: {self.country}\n\tГород: {self.city}\n\tО себе: {self.about_you}')
while True:
    choice=int(input(f'Введите:\nЦифру `1`, если хотите заполнить анкету\nЦифру `2`, если хотите изменить анкету!\nЦифру `3`, если всё готово!\n~~~'))
    if choice==1:
        print(f'Заполните анкету:')
        inname=str(input('Введите своё имя: '))
        inage=int(input('Введите свой возраст: '))
        incountry=str(input('Введите страну в которой проживаете: '))
        incity=str(input('Введите город в котором вы проживаете: '))
        inaboutyou=input('Расскажите о себе что-то интересное: ')
        info=Bot(inname, inage, incountry, incity, inaboutyou)
        while True:
            view=input(f'Если хотите посмотреть вашу анкету введите `Посмотреть`!\nЕсли не хотите просматривать вашу анкету, введите `Готово`\n~~~')
            if view=='Посмотреть':
                info.form()
                break
            elif view=='Готово':
                print('Ваша анкета сохранена')
                break
            else:
                print('Введите один из вариантов ответа:')
    elif choice==2:
        print(f'Измените свою анкету: \n')
        inname=str(input('Введите своё новое имя: '))
        inage=int(input('Введите свой новый возраст: '))
        incountry=str(input('Введите страну в которой проживаете: '))
        incity=str(input('Введите город в котором вы проживаете: '))
        inaboutyou=input('Расскажите о себе что-то интересное: ')
        info=Bot(inname, inage, incountry, incity, inaboutyou)
        while True:
            view=input('Если хотите посмотреть вашу анкету введите `Посмотреть`! Если не хотите просматривать вашу анкету, введите `Готово`')
            if view=='Посмотреть':
                info.form()
                break
            elif view=='Готово':
                print('Ваша анкета сохранена')
                break
            else:
                print('Введите один из вариантов ответа:')
    elif choice==3:
        print(f'Ваша анкета заполнена')
        break
    else:
        print(f'Ошибка')
