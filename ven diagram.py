setu=[]
setme=[]
n=int(input("enter how many item do you want in your list "))
for i in range(n):
    i=int(input("enter numbers of your choice for the list  "))
    setu.append(i)
print(setu)
n=int(input("enter how many item do you want in your list "))
for i in range(n):
    i=int(input("enter numbers of your choice for the list  "))
    setme.append(i)
print(setme,"these are the numbers repted in the list")


setthey={10,9,8,7,6,5,4,3,2,1}
setwe={1,2,3,4,5,6,7,8,9,10}
setour=setthey.intersection(setwe)
print(setour)
