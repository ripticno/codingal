print("1.car")
print("2.bike")
op=str(input("plese enter which one do you want bike or car "))
if op=="car":
    op2=str(input("which type of car would you want a off raoding or sports car "))    
    if op2=="off roading car":
        print("your offroading car is onthe way thank you for visiting our wedsite")
    elif op2=="sports car":
        print("your sports car is on the way thank you for vesiting our wedsite")
    else:
        print("something went wrong you will have to restart")
elif op=="bike":
    op2=str(input("plese enter the type of bike you want sports or dirt bike "))
    if op2=="sports bike":
        print("your sports bike is on the way thank you for vesiting our wedsite")
    elif op2=="dirt bike":
        print("your dirt bike is on the way thank you for vesiting our wedsite")
    else:
        print("something went wrong you will have to restart")
else:
    print("something went wrong you will have to restart")
    
