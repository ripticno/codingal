def tap_list(r):
    lenth=(len(r)-1)
    random_num=0
    while (random_num<lenth):
        if (r[lenth]!=r[random_num]):
            return False
        random_num+=1
        lenth-=1
    return True
r=[]
n=int(input("enter how many item do you want in your list "))
for i in range(n):
    i=int(input("enter numbers of your choice for the list  "))
    r.append(i)
print(r)
if tap_list(r):
    print('the taple list is flip flop')
else:
    print('the taple list is not flip flop')