list1=[]
n=int(input("enter how many item do you want in your list "))
for i in range(n):
    i=str(input("enter the items as words or names for your list "))
    list1.append(i)
print(list1)
for item in list1:
    if item[-1]==item[0]:
        print(item)