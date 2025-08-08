import random
class fruitquiz:
    def __init__(self):
        self.fruit={'apple':'red','orange':'orange','watermalone':'green','banana':'yallow'}
    def quiz(self):
        while(True):
            fruit, colour=random.choice(list(self.fruit.items())) 
            print('what is the colour of the fruit {}'.format(fruit))
            user_answer=str(input("Ans: "))
            if (user_answer==colour):
                print("correct answer")
            else:
                print("wrong answer")
            option=int(input("enter 1 if you want to continue playing otherwise enter 0 "))
            if(option):
                break
print("Welcome to my fruit quiz")
fq=fruitquiz()
fq.quiz ()
