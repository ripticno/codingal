class dad:
    def  __init__(self,eye,aggressive):
        self.eye=eye
        self.aggressive=aggressive
    def display(self):
        print(self.eye)
        print("aggressive",self.aggressive)
class son(dad):
    def __init__(self,eye,aggressive,age,skin):
        self.age=age
        self.skin=skin
        dad.__init__(self,eye,aggressive)
    def display2(self):
        print(self.age)
        print(self.skin)
eye=str(input("enter the colour of your eye "))
skin=str(input("enter your skin colour "))
age=int(input("enter your age "))
object2=dad(eye,True)
object=son(eye,True,age,skin)
print("you have inherited from your dad")
object.display()
object.display2()
