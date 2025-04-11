r=set()
n=int(input("enter how many item do you want in your set "))
for i in range(n):
    i=int(input("enter numbers of your choice for the set "))
    r.add(i)
print(r)
b=list(map(lambda add: 2*add,r))
print(b)