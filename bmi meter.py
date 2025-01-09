weight=int(input("enter your weight "))
hight=int(input("enter your hight "))
hight=hight*0.3048
cal=hight*hight
BMI=weight/cal
if BMI<=18.5:
    print("you are under weight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight")
elif BMI<=34.9:
    print("you are obese")
else:
    print("you are extremly obese")
