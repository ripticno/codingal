def squer(a):
    area=a*a
    print(area,"cm squer")
def tringle(c,f):
    area=(c*f)/2
    print(area,"cm squer")
def circle(r):
    area=(r*r)*3.14
    print(area,"cm squer")
print("what do you want to calclute")
print("1.squer\n2.tringle\n3.circle")
inPUT=int(input("enter which shape you want "))
if inPUT==1:
    side_lenth=int(input("enter your side lenth "))
    squer(side_lenth)
elif inPUT==2:
    hight=int(input("enter your hight lenth of your tringle "))
    base=int(input("enter your base lenth of your tringle "))
    tringle(hight,base)
else:
    redius=int(input("enter your curcle's redius "))
    circle(redius)
    


