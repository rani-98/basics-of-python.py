
'''dictionary'''

x={"a":1,"b":2,"c":3,"d":4,"e":5}
print(type(x))

print(x["a"])  #printing a key value
#adding items in dictionary
x.update({"f":6})
print(x)
#removing items in dictionary
x.pop("f")

for i in x:            #print keys
    print(i)
for j in x.values():    #print values
    print(j)

k=0
for j in x.values():   #sum of values in dictionary
    k=k+j
print(k)

def fun():
    k=0
    for r in t.values():    # sum of values in dictionary
        k=k+r
        return k
t={"a":1,"b":2,"c":3,"d":4,"e":5}
fun()

def func(k):
    for r in t.values():     #product of values in dictionary
        k = k * r
    return k
t = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(func(1))

dict1={"a":1,"b":2,"c":3}
dict2={"a":1,"b":2,"c":3}
dict3={}
for key in dict1.keys():
    dict3={key:dict1[key]+dict2[key]}   #sum of two dictionary values= value of third dictionary
    print(dict3)
dict1={"a":1,"b":2,"c":3}
dict2={"d":1,"e":2,"f":3}    
dict4={}
for d in (dict1,dict2):
    dict4.update(d)
print(dict4)


    # Example dictionary with duplicates
original_dict = {"a": 1, "b": 2, "c": 3, "a": 4, "d": 5, "b": 6}
# Create a new dictionary to store unique key-value pairs
unique_dict = {}
# Iterate through the original dictionary and add non-duplicate items to the new dictionary
for key, value in original_dict.items():
    if key not in unique_dict:
        unique_dict[key] = value
# Printing the result
print("Dictionary without duplicates:", unique_dict)


def remove_duplicates(input_dict):
    unique_dict = {}
    for key, value in input_dict.items():# Check if the value is already in the unique_dict values
        if value not in unique_dict.values():
            unique_dict[key] = value
    
    return unique_dict
# Example dictionary with duplicates
original_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2, "f": 4}
# Use the function to remove duplicates
unique_dict = remove_duplicates(original_dict)
# Printing the result
print("Dictionary without duplicates:", unique_dict)

