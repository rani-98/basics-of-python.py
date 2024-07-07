'''tuple'''

x=(1,2,3,4,5,6,7)
for i in x:
    print(i)
    
k=0
for j in x:
    k=k+j
    print(k)
    
y=(8,9,10)  
print(x+y)  #merging two tuples

# sum of two tuples using function
def add_tuples(tuple1, tuple2):  # Check if the tuples have the same length
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length")
    result = tuple(x + y for x, y in zip(tuple1, tuple2)) 
    # Use a list comprehension to add corresponding elements
    return result
tuple1 = (1, 2, 3)
tuple2= (4, 5, 6)

sum_result = add_tuples(tuple1, tuple2)

print("Sum of the tuples:", sum_result)

#sum of tuples
# Example tuples
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
if len(tuple_a) != len(tuple_b):
    print("Tuples must have the same length.")
else:
    sum_tuple = () # Initialize an empty tuple to store the sum
    # Use a loop to add corresponding elements
    for i in range(len(tuple_a)):
        sum_tuple= sum_tuple+(tuple_a[i] + tuple_b[i],)
    print("Sum of the tuples:", sum_tuple)  # Printing the result

x=(1,2,3,4,5,6,7,7,6)
t=[]
for i in x:
    if i not in t:
        t.append(i)
print(tuple(t))