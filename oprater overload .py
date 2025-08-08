class A:
    def __init__(self,a):
        self.a=a 
    def __lt__(self,b):
        if (self.a<b.a):
            return "od 1 is less then ob 2"
        else :
            return "ob 2 is less then ob 1"
    def __eq__(self,b):
        if (self.a==b.a):
            return "bothe are equal"
        else:
            return "not equal"
a1=int(input("enet a number "))
a2=int(input("ente a number "))        
ob1=A(a1)
ob2=A(a2)
print(ob1<ob2)
print(ob1==ob2)


