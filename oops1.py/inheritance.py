#basic inheritance
#parant class
class Animal:
    def __init__(self,name):
      self.name=name

def speak(self):
    raise NotImplementedError("sub class must implement abstact method")

#child class
class Dog(Animal):
    def speak (self):
        return "woof!" 
#child class
class Cat(Animal):
    def speak(self):
        return "meow!"
    
X=Dog("humm")
print(X.name)
