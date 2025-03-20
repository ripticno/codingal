plain=30
def new_york(day):
    price=day*35
    total=plain+price
    return total
def texas(day):
    price=day*20
    total=plain+price
    return total
def callifornia(day):
    price=day*45
    total=plain+price
    return total
def chicago(day):
    price=day*15
    total=plain+price
    return total 
print("new york per night $35")
print("texas per night $20")
print("callifornia per night $45")
print("chicago $15")
print("for all city plain cost is $ $30")
user=str(input("enter which city do you want to go "))
day=int(input("enter how many days do you want to stay "))
if user=='new york':
    print(new_york(day))
elif user=='texas':
    print(texas(day))
elif user=='callifornia':
    print(callifornia(day))
elif user=='chicago':
    print(chicago(day))
