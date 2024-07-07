#rock, paper, sessior game
print("welcome to rock, paper, scissor game : ")
import random
a=("rock,paper,scissor")
guess=input("guess the one : ")

players = 0
computer =0 


while True:
 b=random.randint("rock,paper,scissor")
 if (guess == computer):
  print("tie",b)
 
 elif guess == "scissor":
  computer == "rock"
  print("wrong,the answer is ",computer)
 elif guess == "paper":
    computer == "scissor"
    print("the  ", computer)
 elif guess == "rock":
     computer == "paper"
 print("")

 
