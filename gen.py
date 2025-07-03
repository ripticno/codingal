class dad:
    def  __init__(self,eye,aggressive):
        self.eye=eye
        self.aggressive=aggressive
    def display(self):
        print(self.eye)
        print(self.aggressive)
class son(dad):
    def __init__(self,eye,aggressive,age,skin):
        self.age=age
        self.skin=skin
        dad.__init__(self,eye,aggressive)
    def display2(self):
        print(self.age)
        print(self.skin)
object=son("black",True,19,"brown")
object.display()
object.display2()