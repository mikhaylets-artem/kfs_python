money=int(input('Ваш бюджет '))
years=int(input('через сколько снимите '))
proc=int(input('Какой процент годовых'))

if years>11:
   money+=money*0.2
   print(money)
else:
    print(money)
   

#soum=5000
#percent=20
#year=int(input('Укажите месяц снятия: '))
#if (year>11) and (year<24):
#    soum_one_year=soum+soum*(percent/100)
#    print('Ваша сумма равна: ', soum_one_year)
#elif year>23:
##    soum_one_year_1=soum+soum*(percent/100)
#    soum_two_year=soum_one_year_1+soum_one_year_1*(percent/100)
#    print('Ваша сумма равна: ', soum_two_year)
#else:
#    print('Ваша сумма равна: ', soum)


