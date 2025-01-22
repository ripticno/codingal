cycle1=int(input("enter your speed during the race "))
cycle2=int(input("enter your speed during the race "))
cycle3=int(input("enter your speed during the race "))
cal=(cycle1+cycle2+cycle3)/3
print(cal,"is the avg of the 3 cycilisist")
if cycle1<cal:
    print("cycilists 1 is slow then",cal)
if cycle2<cal:
    print("cycilists 2 is slow then",cal)
if cycle3<cal:
    print("cycilists 3 is slow then",cal)
else:
    print("all cycilists are equal")