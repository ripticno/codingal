n=int(input("enter the number of rows you want "))
v=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(v ,end=" ")
        v=v+1
    print()