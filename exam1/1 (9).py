s1=["j","h","g","u","k","r"]
s2=[7,8,9,10,11,12]
step=int(input("step= "))
s3={key:value**step for key,value in zip(s1,s2)}
for i,h in s3.items():
    print(f"Ya znayu tovy kluch - '{i}',ego znachenie -'{h}'")
print(s3)
