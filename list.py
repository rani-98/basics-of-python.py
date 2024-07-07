
'''list'''

x=[1,2,3,4,5,6,7]
print(type(x))

#adding items in a list
x.insert(7,8)
x.append(9)
x.extend([10])

#removing items in a list
x.remove(10)
x.pop()

for i in x:        #print all elements
    print(i)
    
k=0
for j in x:        #sum of items in a list
    k=k+j
print(k)

k=1
for r in x:        #product of items in a list
    k=k*r
print(k)

for l in x:        #square of items in a list
    print(l**2)
    
for m in x:        #power of items in a list
    m=m**m
    print(m)

k=0
for n in x:         
    k=k-n
    print(k)
    
for t in x:          #square root of items in a list
    print(t**0.5)
    
    
list_a = [1, 2, 3]
list_b = [4, 5, 6]              #sum of two lists
if len(list_a)!= len(list_b):
    print("Lists must have the same length.")
else:
    sum_list = []
    for i in range(len(list_a)):
        sum_list.append(list_a[i]+list_b[i])
    print("Sum of the lists:", sum_list)


def find_duplicates(lst):     #dublicates
    duplicates = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates
my_list = [1, 2, 3, 4, 2, 5,5,4,6]
result = find_duplicates(my_list)
print("Duplicates:", result)


def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
original_list = [1, 2, 3, 4, 2, 5, 6, 7, 8, 1]
unique_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)



