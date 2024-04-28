
def grading_system(a):
 if a>=90:
    return "A+"
 elif a>=80:
     return "A"
 elif a>=70:
     return "B+"
 elif a>=60:
     return "B"
 elif a>=50:
     return "C"
 elif a>=40:
     return "D"
 elif a<40:
     return "F"
 if a>100 or a<0:
     print("Invalid Input")
a=float(input(("Enter the score:")))
grade = grading_system(a)
print(f"The grade for the given score {a} is {grade}")
 