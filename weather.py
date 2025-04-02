print("1=rainy")
print("0=sunny")
a=int(input("enter how was the weather on sunday using 0 or 1 "))
b=int(input("enter how was the weather on monday using 0 or 1 "))
c=int(input("enter how was the weather on tuesday using 0 or 1 "))
d=int(input("enter how was the weather on wednesday using 0 or 1 "))
e=int(input("enter how was the weather on thursday using 0 or 1 "))
f=int(input("enter how was the weather on friday using 0 or 1 "))
g=int(input("enter how was the weather on starday using 0 or 1 "))
weather=(a,b,c,d,e,f,g)
sunny=0
rainy=0 
for i in range(0,7):
    if weather[i]==0:
        sunny+=1
    else:
        rainy+=1
if sunny<rainy:
    print("the week was rainy")
else:
    print("the week was sunny")
print(weather)