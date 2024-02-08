"""
Write a Python program to check whether a number is negative, positive or zero.
"""

#SOLUTION:
x=int(input("Enter the number you wish to check whether it is positive, negatvie or zero: "))
if x>0:
    print(x,"is a positive number")
elif x<0:
    print(x,"is a negative number")
else:
    print(x,"is zero")

# OUTPUT:
# Enter the number you wish to check whether it is positive, negatvie or zero: 10
# 10 is a positive number
