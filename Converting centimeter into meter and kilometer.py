"""
Write a python program to enter length in centimeter and convert it into meter and kilometer.
"""

#SOLUTION
a=float(input("Enter the length in centimeter: "))
b=a/100
c=a/100000
print("conversion of given centimeter", a, "into meter is", b)
print("conversion of given centimeter", a, "into kilometer is", c)

#OUTPUT
# Enter the length in centimeter: 1500
# conversion of given centimeter 1500.0 into meter is 15.0
# conversion of given centimeter 1500.0 into kilometer is 0.015
