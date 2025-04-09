product_storage={'prime':'$6','chips':'$2','toys':'$50','books':'$10','gum':'$3','chocolets':'$5'}
print('we have prime, chips, toys, books, gum, chocolates')
user_input=str(input(" welcome to food product limited enter the name of the food of your choise "))
print(product_storage.get(user_input,'not found'))
