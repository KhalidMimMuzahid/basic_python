# class MyClass:
#     x=5
# p1= MyClass()
# print(p1.x)
class Person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
p1= Person("Khalid",26)
# print(p1.name) #Khalid
# print(p1.age) # 26
del p1.age 
# print(p1.age) # AttributeError: 'Person' object has no attribute 'age'