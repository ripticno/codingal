a=int(input("enter a number to print 0 to the number in revers order "))
b=int(input("enter a number which you want to skip "))
a=a+1
while (a)>0:
    a=a-1
    if a==b:
        continue
    print(a)