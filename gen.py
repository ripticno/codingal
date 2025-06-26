class dad:
    def  _init_(self,eye,aggressive):
        self.eye=eye
        self.aggressive=aggressive
    def display(self):
        print(self.eye)
        print(self.aggressive)
class son(dad):
    def _init_(self,eye,aggressive,age,skin):
        self.age=age
        self.skin=skin
        dad._init_(self,eye,aggressive)
    def display2(self):
        print(self.age)
        print(self.skin)
odj=son("black",True,19,"brown")
obj.display()
obj.display2()