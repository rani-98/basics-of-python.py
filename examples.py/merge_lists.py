list1= [3,6,1,8]
list2=[2,6,4,8]
list3=[]
result=[] 
def mas(list1,list2):
   list3 = list1 + list2 
   print("merged lists",list3)
   for i in list3:
    if i not in result:
      result.append(i)
   result.sort()
   return result
mas(list1,list2)
print("after removing sorted eliments: ", result)


   
     