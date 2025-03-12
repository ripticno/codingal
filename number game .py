import random
x=int(input("enter the range you want to play the game 0 to what "))
number=str(random.randint(0,x))
player=True
attempt=0
while player:
    guss=str(input("enter your numder to guss the right number from 0 to 7 "))
    attempt+=1
    if guss==number:
        print('you won the game')
        print('you attempted',attempt,'times')
        print('the number was',number)
        player=False
        break
    else:
        print('your guss is not corect')