#max of 3 numbers
x=int(input("enter num1: "))
y=int(input("enter num2: "))
z=int(input("enter num3: "))


def large(x,y,z):
    sort=sorted([x,y,z])
    return sort[-1]
a=x
b=y
c=z

largest=large(a,b,c)
print("largest number is", largest)