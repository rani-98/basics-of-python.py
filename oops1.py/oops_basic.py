class person:
 
 name="kiran"
 age=36
p1=person()
p2=person()
p3=person()
p4=person()
print(type(p1),type(p2),type(p3))
#print(dir(p1))
print(p1.name,p1.age)
print(p2.name,p2.age)
print(p3.name,p3.age)
print(p4.name,p4.age)

print("changing the name and age of p1")
p1.name="Arun"
p1.age=30
print(p1.name,p1.age)
print(p2.name,p2.age)
print(p3.name,p3.age)


p4.name="kumar"
p4.age=20

print(p4.name,p4.age)