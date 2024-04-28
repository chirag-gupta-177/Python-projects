a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("Enter 1 for addition 2 for subtraction 3 for multiplication and 4 for division")
inp=int(input("Enter your input:"))
if inp==1:
    print(a+b)
elif inp==2:
    print(a-b)
elif(inp==3):
    print(a*b)
elif(inp==4):
    print(a/b)
else:
    print("Enter valid Input!")