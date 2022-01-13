age=int(input("n= "))
if age<2:
    print("mladenec")
elif age>=2 and age<4:
    print("malish")
elif age>=4 and age<13:
    print("rebenok")
elif age>=13 and age<20:
    print("podrostok")
elif age>=20 and age<65:
    print("vzrozly")
elif age>=65:
    print("ded")
elif age<=0:
    print('s nachala rodis`')
