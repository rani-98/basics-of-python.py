
a=1,2,3,4,5
print(len(a))

for i in range(3):
    print(i)


i=3
while i>0:
    print(i)
    i-=1
    
def func(x,y=5):
    return x+y
print(func(2))

#while True:
#    print("Hello")
    

list1=[1,2,3]
list1.extend(4,5)

d={'a':1,'b':2}
del d['a']
print(d)

if not False:
    print("a")
else:
    print("b")
    

def print_numbers(a,b=5,c=10):
    print('a:',a,'b:',b,'c:',c)
    print_numbers(3,7)
    
def func(x):
    return x*x
func(2)

for i in range(2):
    for j in range(2):
        print(i,j)
        
a,b=(1,2)
print(a)
    