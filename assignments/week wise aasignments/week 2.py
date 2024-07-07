'''
1
def fun(x):
    return x+1
print(fun(4))
'''
'''
if 10>5:
    print("true")
else:
    print("false")
'''

'''#list
list1={1,2,3,4,5}
list2={2,5,6,7,8}
list3={list1}+{list2}
list3.sort()
print("after sort",list3)

'''
'''
#6  tuple

animals = ("elephant", "lion", "zebra", "hippo", "tiger", "wild boar")
print(type(animals))
print(animals)
#print(dir(animals))
print(animals.count("wild buffalo"))
print(animals.index("lion"))
print(animals[2])

'''
'''
7
#functions
def foo(a,b=4,c=6):
    print(a,b,c)
    
foo(20,c=12)

'''
'''
8
i=[1,2,3,4,5]
if 3 in i:
    print("yes")
else:
    print("no")
    
'''
'''
10
a,b,c=(1,2,3)
print(b)
'''
'''
11
def test(x,y):
    return x*y
print(test(2,y=3))
'''
'''
12
word="hello"
if word=="hello":
    print("hi")
else:
    print("good bye")
            '''
'''
#13 slicing
my_list=[0,1,2,3,4]
print(my_list[1:3])
'''
'''
#14
s1={1,2,3}
s2={3,4,5}
result=s1.intersection(s2)
print(result)
'''
#15
d = {'a': 1,'b': 2}
d['a']=3
d['c']=4
print(d['a'])
print(d['c'])