'''list'''
x=[1,2,3,4,5,6,7,8,9]
'''printing all the items'''
for i in x:
    print(i)
for j in x:
    print(j,end="")
'''adding items in x'''
x.insert(9,10)
x.append(11)
x.extend([12,13])
y=x
print(y)

'''removing items in y'''
y.remove(13)
y.pop(11)          #pop(i) where i is index number y[i]
print(y)

y.append(10)       #adding an item
z=y
print(z)

'''removing dublicates in a list'''
t=[]
for x in z:
    if x not in t:
        t.append(x)
print(t)

'''print dublicates'''
duplicates = []
for i in range(len(z)):
    for j in range(i + 1, len(z)):
        if z[i] == z[j] and z[i] not in duplicates:
                duplicates.append(z[i])
print(duplicates)

from collections import Counter

my_list = [1, 2, 3, 4, 5, 2, 7, 8, 9, 5]

counter_dict = Counter(my_list)
duplicates = [item for item, count in counter_dict.items() if count > 1]
print(duplicates)


duplicates = []
for i in range(len(my_list)):
    item = my_list[i]
    for j in range(i + 1, len(my_list)):
        if item == my_list[j] and item not in duplicates:
            duplicates.append(item)
print(duplicates)

