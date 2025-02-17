def tips(bill):
    total_bill=bill*0.01
    total_bill=(total_bill)+bill
    print("you have to pay",total_bill)
bill=int(input("enter your bill for the food "))
tips(bill)