'''
magic methodsare the special methods which add "magic" to your class. 
they are the methods having double underscores at the biginning and end
of the of their names.they are also called dunder methods.

_init_ method
'''
class person:
# cretaed insidea class wil have self as the first parameter
    
 def __init__ (self,name,age,adress,mobile):
  self.name=name
  self.age=age
  self.address=adress
  self.mobile=mobile
  print("person object created")
  
 def details(self):
  print(f"name:{self.name}")
  print(f"age:{self.age}")
  print(f"address:{self.address}")
  print(f"mobile:{self.mobile}")
  #when you create a object by passing the parameters,the __int__ method is called
  #and the arguments are passed to the __int__method
  
    