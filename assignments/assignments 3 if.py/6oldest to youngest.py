#6.age of 3 people oldest and youngest
age1 = int(input("person age 1:"))
age2 = int(input("person age 2:"))
age3 = int(input("person age 3:"))
if (age1>age2 and age1>age3):
    print("age1 is oldest")
elif (age2>age3 and age2>age1):
    print("age2 is oldest")
elif (age3>age1 and age3>age2):
    print("age3 is oldest")
if (age1<age2 and age1<age3):
    print("age1 is youngest")
elif (age2<age3 and age2<age1):
    print("age2 is youngest")
elif (age3<age1 and age3<age2):
    print("age3 is youngest")

   
