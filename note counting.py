amount=int(input("enter a amount aof money "))
note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10
print("the 100tk count is", note_100)
print("the 50tk count is", note_50)
print("the 10tk count is", note_10)
