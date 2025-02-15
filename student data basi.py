def taamir():
    a="11 year's old"
    s="taamir like's math and science"
    g="taamir is in 6th g"
    print(a)
    print(s)
    print(g)

def ayaz():
    a="12 year's old"
    s="ayaz like's science"
    g="ayaz is in 6th g"
    print(a)
    print(s)
    print(g)

def ohon():
    a="11 year's old"
    s="ohon like's math"
    g="ohon is in 6th g"
    print(a)
    print(s)
    print(g)

print("1.ayaz\n2.taamir\n3.ohon")
cal=str(input("which student are you looking for "))
if cal=="ayaz":
    ayaz()
elif cal=="taamir":
    taamir()
else:
    ohon()
    
    