try:
    num1=int(input('enter your first number '))
    num2=int(input('enter tour second number  '))
    cal= num1/num2
    print(cal)
except ValueError as e:
    print(e)
except ZeroDivisionError as x:
    print(x)
except NameError as z:
    print(z)