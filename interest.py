princpal=int(input("enter the amount of money you eant to keep "))
rate=int(input("enter the rate your annual interest "))
rate=rate/100
time=int(input("enter the anountn of time you want to keep your money "))
si=princpal*rate*time
ci=princpal*((1+rate)**time)
print("the simple interest is", si,"your total money will be", si+princpal)
print("the compound interest", ci,"and your total money will be", ci+princpal)
