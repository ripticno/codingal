name={"ayaz","suffan","ohon","taamir","amir"}
roll={1,2,3,4,5}
zipp=dict(zip(name,roll))
print(zipp)
user_input=str(input("enter which stunts roll you want to see "))
if user_input in zipp:
    print(user_input,zipp[user_input])
else:
    print("your given name is unvarafide")