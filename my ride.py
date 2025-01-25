print("1.car")
print("2.bike")
op=str(input("plese enter which one do you want bike or car "))
if op=="car":
    op2=str(input("which type of car would you want a off raoding or sports car "))
    if op2=="off roading car":
        print("your car is onthe way thank you for visiting our wedsite")
    elif op2=="sports car":
        print("your car is on the way thank you for vesiting our wedsite")
    else:
        print("something went wrong you will have to restart")
elif op=="bike":
    op2=str(input("plese enter the type of bike you want sports or dirt bike "))
    if op2=="sports bike":
        print("your bike is on the way thank you for vesiting our wedsite")
    elif op2=="dart bike":
        print("your bike is on the way thank you for vesiting our wedsite")
    else:
        print("something went wrong you will have to restart")
else:
    print("something went wrong you will have to restart")
    
