try:
    num=int(input("enter your number "))
    if num>0:
        print(num)
except ValueError as e:
    print('something went wrong',e)
print('a')
print('ererf')