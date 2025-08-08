class flashcard:
    def __init__(self,word, meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + "(" + self.meaning + ")"
flash=[]
print("welcome to my applection")
while True:
    word=input("enter word for your flashcard ")
    meaning=input("enter the meaning of your flashcard ")
    flash.append(flashcard(word,meaning))
    option=int(input("enter 0 if you want another flashcard otherwise enter 1 "))
    if (option):
        break
print("your flashcards are")
for i in flash:
    print(">>>",i)
