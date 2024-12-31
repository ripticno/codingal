print("enter your age")
age=int(input())
if age<18:
    print("sorry your not old enough to vote")
elif age>=18 and age<100:
    print(" you are allowed  to vote")
else:
    print("you are too old to vote")
