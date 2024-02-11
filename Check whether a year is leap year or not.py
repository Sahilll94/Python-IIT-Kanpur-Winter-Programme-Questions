#Question Description
"""
Write a Python program to check whether a year is leap year or not.
"""

#SOLUTION
x=int(input("Enter the year you wish to know whether it is Leap Year or not: "))
if (x%4==0):
    print("The year",x,"is a Leap Year")
else:
    print("the year",x,"is not a Leap Year")

#OUTPUT
# Enter the year you wish to know whether it is Leap Year or not: 2024
# The year 2024 is a Leap Year
