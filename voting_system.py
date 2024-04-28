name=input("Enter your Name:")
age=int(input("Enter your age:"))
if(age>=18):
    print(name,"you are eligible to vote")
    print("Press 1 to Vote for BJP")
    print("Press 2 to Vote for Congrees")
    print("Press 3 to Vote for AAP")
    print("Press 4 to Vote for SP")
    vote=int(input("Enter your Vote:"))
    if(vote==1):
        print("You Voted for BJP")
    elif(vote==2):
        print("You Voted for Congrees")
    elif(vote==3):
        print("You Voted for AAP")
    elif(vote==4):
        print("You Voted for SP")
    else:
        print("Invalid Input!")
else:
    print("You are not eligible to Vote")