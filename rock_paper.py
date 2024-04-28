import random
computer_score=0
user_score=0
while True: 
 print("Enter 1 for Rock,2 for paper and 3 for scissor")
 n=int(input("Enter your Choice:"))
 if n>3:
    print("Enter valid input!")
 else:  
  choice={1:"Rock",2:"Paper",3:"Scissor"} 
  a=random.randint(1,3)
  if n==1 and a==1:
    print("Computer also chose Rock")
  elif n==1 and a==2:
    print("Computer chose Paper")
    print("You lose")
    computer_score+=1
  elif n==1 and a==3:
    print("Computer chose scissor")
    print("You Won")
    user_score+=1
  elif n==2 and a==1:
    print("Computer chose Rock")
    print("You Won")
    user_score+=1
  elif n==2 and a==2:
    print("Computer also chose Paper")
  elif n==2 and a==3:
    print("Computer chose scissor")
    print("You lose")
    computer_score+=1
  elif n==3 and a==1:
    print("Computer chose Rock")
    print("You Lose")
    computer_score+=1
  elif n==3 and a==2:
    print("Computer chose Paper")
    print("You Won")
    user_score+=1
  elif n==3 and a==3:
    print("Computer also chose scissor") 
  play_again=input("Do you want to play again(yes/no)?:")
  if play_again.lower()=="no":
   break
  elif play_again.lower()!="yes" and play_again.lower()!="no":
      print("Enter valid input!")
      play_again=input("Do you want to play again(yes/no)?:")
print("Final Scores:")
print("Your Score:",user_score)
print("Computer's Score:",computer_score)