a=int(input("enter an number to find is it prime or not "))
if a<2:
    print("sorry you will have to restart")
else:
    for b in range (2,a):
        if a%b==0:
            print("it is not a prime number")
            break
        
    else:
        print("it is a prime number")    