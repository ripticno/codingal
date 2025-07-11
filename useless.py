class bangladesh():
    def capital(self):
        print("dhaka is the capital of bangladesh")
        print("dhaka is the oldest city in the world")
    def language(self):
        print("every one in bangladesh speaks banglish")
        print("bangla is the second most hardest language to learn")
    def type(self):
        print("bangladesh is a undevloped country")
class usa():
    def capital(self):
        print("the captial of usa is w.dc")
    def language(self):
        print("every one in the usa speaks brienglish")
    def type(self):
        print("the country usa is devloped")
obj_bangladesh101=bangladesh()
obj_usa=usa()
for country in (obj_bangladesh101,obj_usa):
    country.capital()
    country.language()
    country.type()