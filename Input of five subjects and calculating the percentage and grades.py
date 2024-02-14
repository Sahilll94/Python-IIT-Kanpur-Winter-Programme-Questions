#Question Description
"""
Write a Python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
"""

#Solution
Physics=float(input("Enter the marks you obtained in physics:"))
Chemistry=float(input("Enter the marks you obtained in Chemistry:"))
Biology=float(input("Enter the marks you obtained in Biology:"))
Mathematics=float(input("Enter the marks you obtained in Mathematics:"))
Computer=float(input("Enter the marks you obtained in Computer:"))
s=[Physics,Chemistry,Biology,Mathematics,Computer]
total_marks=sum(s)
percentage=((total_marks/len(s))*100)
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
  elif percentage>=60:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
elif percentage<40:
    print("Grade F")
else:
    print("Enter valid marks of all the subjects")

#Output
# Enter the marks you obtained in physics:40
# Enter the marks you obtained in Chemistry:40
# Enter the marks you obtained in Biology:40
# Enter the marks you obtained in Mathematics:40
# Enter the marks you obtained in Computer:40
# Grade A


