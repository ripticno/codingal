a=int(input("plese enter your buy rate of any product "))
b=int(input("plese enter your sell rate of the same product "))
if a>b:
    print("it is a loss")
elif a<b:
    print("it is a profit")
else:
    print("it has no profit")