def add():
    a=int(input("enter your first number "))
    b=int(input("enter your second number "))
    print(a+b)
def subtract():
    a=int(input("enter your first number "))
    b=int(input("enter your second number "))
    print(a-b)
def multiply():
    a=int(input("enter your first number "))
    b=int(input("enter your second number "))
    print(a*b)
def divide():
    a=int(input("enter your first number "))
    b=int(input("enter your second number "))
    print(a/b)
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
c=str(input("enter which oparation would you like to use with your number "))
if c=='add':
    add()
elif c=='subtract':
    subtract()
elif c=='multiply':
    multiply()
elif c=='divide':
    divide()
else:
    print("something went wrong you will have to restart")