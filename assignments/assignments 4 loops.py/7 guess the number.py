#guess the number
import random

a= random.randint(1,30)

tries = 1
while tries <=5 : # true
   u=int(input("guess the number:"))
   if u == a:
      print("guess was correct")
      break
   elif u > a:
      print("your guess is large")
   elif u < a:
      print("your guess is small")

   tries = tries + 1
 
   print("your tries",5-tries,"only")