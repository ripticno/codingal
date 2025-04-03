student_data={"sid1":
              {'name':['taamir'],
               'class':[5],
               'suject':["english","math","science"]},
               "sid2":
              {'name':['ayaz'],
               'class':[5],
               'suject':["english","math"]},
               "sid3":
              {'name':['taamir'],
               'class':[5],
               'suject':["english","math","science"]},
               "sid4":
              {'name':['wasfi'],
               'class':[5],
               'suject':["math","science"]},}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)