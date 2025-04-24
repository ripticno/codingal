import random
x=100
attenpts=0
maxmum_attenpts=6
print("you have 6 attenpts")
print("the number is chosen from 0 to 100")
number=int(random.randint(0,x))
cal=number%2
if cal==0:
    print("it is a even number")
    print("go ahead")
else:
    print("it is a odd number")
    print("go ahead")
while attenpts<=maxmum_attenpts:
    try:
        userinput=int(input("enter your guss "))
        attenpts+=1
        if userinput==number:
            print("your guss is correct ✔️")
            print("you gussed it in",attenpts,"attenpts")
            break
        elif userinput>number:
            print("your gess is too high try a lower number 👇")
        elif userinput<number:
            print("your guss is too low try a higher number ☝️")
        print("you have",maxmum_attenpts-attenpts,"attenpts")
    except:
        print("you have entered a unvalid character")   
if userinput!=number:
    print("you could not guss the number in 6 attenpts, try again 😭")
    print(number)
