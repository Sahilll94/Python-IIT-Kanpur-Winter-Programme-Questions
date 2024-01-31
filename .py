#QUESTION DESCRIPTION
"""
Write a Python  program to Swapping Two Number
"""

#SOLUTION
a=int(input("Enter the first number to swap: "))
b=int(input("Enter the second number to swap: "))
print("Before swapping the numbers are:", a,b)
(a,b)=(b,a)
print("After swapping the numbers are:", a,b)

#OUTPUT
# Enter the first number to swap: 10
# Enter the second number to swap: 20
# Before swapping the numbers are: 10 20
# After swapping the numbers are: 20 10
