"""
Write a python program to enter marks of five subjects and calculate total, average and percentage.
"""

#SOLUTION
a=float(input("Enter the marks of first subject: "))
b=float(input("Enter the marks of second subject: "))
c=float(input("Enter the marks of third subject: "))
d=float(input("Enter the marks of fourth subject: "))
e=float(input("Enter the marks of fifth subject: "))
Total=a+b+c+d+e
Average=Total/5
Maximum_marks_per_subject=100
Total_possible_marks=500
percentage=(Total/Total_possible_marks)*100
print("The total marks obtained in Five subjects are:", Total)
print("The average of the Five subjects are:", Average)
print("The total percentage obtained in Five subjects are:", percentage,"%")

#OUTPUT
# Enter the marks of first subject: 78
# Enter the marks of second subject: 90
# Enter the marks of third subject: 84
# Enter the marks of fourth subject: 92
# Enter the marks of fifth subject: 94
# The total marks obtained in Five subjects are: 438.0
# The average of the Five subjects are: 87.6
# The total percentage obtained in Five subjects are: 87.6 %
