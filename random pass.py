import random
possible=("a","b","c","d","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","10","!","@","#","$","%","^","&","*","A","B","C","D","E","F","G","H","I","J","K","L","M","N","0","P","Q","R","S","T","U","V","W","X","Y","Z")
i=0
user=int(input("enter how many letter you want in your password "))
number_of_letter_in_password=user
password=[]
while i<number_of_letter_in_password:
    maker=random.choice(possible)
    password.append(maker)
    i+=1 
print(password)

