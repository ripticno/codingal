multpul1=set()
multpul2=set()
n=int(input("enter the limit of how many multpul you want "))
num1=int(input("enter the number you chose as the first number "))
num2=int(input("enter the number you chose as yor second number ")) 
for i in range(n):
    i=int(input("enter the as many multpul as you set above of the number you entered above "))
    multpul1.add(i)
same_input=n
for i in range(n):
    i=int(input("enter the second set of multpul of your second number you entered above "))
    multpul2.add(i)
setour=multpul1.intersection(multpul2)
print(setour,"these are the common factors of",num1,"and",num2 ,"up to",n)
print(multpul1)
print(multpul2)