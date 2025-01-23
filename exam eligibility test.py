absence=int(input("enter for how many days where you absanct "))
if absence<0:
    print("the number is invalid")
    absence=int(input("enter for how many days where you absenct "))
reason=str(input("do you have any medical reason yes or no "))
if reason!="yes"or"no":
    print("somthing went wrong")
    reason=str(input("do you have any medical reason yes or no "))
other=str(input("if you have any other reason enter "))
if reason=="yes":
    print("your adsance will be consederd")
elif reason=="no":
    if absence<10:
        print("you can give the exam")
    else:
        print("you cannot give the exam")
