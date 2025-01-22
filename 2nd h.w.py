unit=int(input("plese enter your unit of electry usage in the month "))
if unit<0:
    print("somethint went wrong try again")
    unit=int(input("plese enter your unit of electry usage in the month"))
elif unit>=101 and unit<300:
    resulta=100*5+(unit-100)*8
    print(resulta)
elif unit<=100 and unit>1:
    resultb=(unit*5)
    print()
else:
    resultd=100*5+(unit-100)*8+(unit-300)*10

