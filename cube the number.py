def cube(number):
    return number*number*number
def by3(number):
    if number%3==0:
        return cube(number)
    else:
        return False
a=int(input("enter a number to chick if it is cube or not "))
print(by3(a))
    