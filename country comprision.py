class country2():
    def country_name(self):
        self.name=str(input("enter the name of your country "))
        self.ratting=int(input("enter how nuch will you give your country out of ten "))
    def capital(self):
        self.capital_name=str(input("enter the name of the capital of your country "))
        self.rattingc=int(input("enter how much will you give to the capital of your country "))
        print(self.capital_name)
    def language(self):
        self.languagel=str(input("enter the language which is most used in the country "))
        self.rattingl=int(input("ente hoe much will you give the language of your country "))
    def type(self):
       self.type_name=str(input("enter the type of your country "))
       self.rattingt=int(input("enter how much you will give your country type "))
    def total(self):
        total=self.ratting+self.rattingc+self.rattingl+self.rattingt
        print(total)
class country1():
    def country_name(self):
        print ('now the second player will star to give their country info')
        self.name=str(input("enter the name of your country "))
        self.ratting1=int(input("enter how nuch will you give your country out of ten "))
    def capital(self):
        self.capital_name=str(input("enter the name of the capital of your country "))
        self.rattingc1=int(input("enter how much will you give to the capital of your country "))
    def language(self):
        self.language=str(input("enter the language which is most used in the country "))
        self.rattingl1=int(input("ente hoe much will you give the language of your country "))
    def type(self):
        self.type_name=str(input("enter the type of your country "))
        self.rattingt1=int(input("enter how much you will give your country type "))
    def total(self):
        total=self.ratting1+self.rattingc1+self.rattingl1+self.rattingt1
        print(total)
obj_bangladesh101=country2()
obj_usa=country1()
for country in (obj_bangladesh101,obj_usa):
    country.country_name()
    country.capital()
    country.language()
    country.type()
    country.total()
print("the country with the most points win as the COUNTRY OF THE YEAR") 