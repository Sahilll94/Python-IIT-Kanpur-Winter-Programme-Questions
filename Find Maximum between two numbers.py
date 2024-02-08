"""
Write a Python program to find maximum between two numbers.
"""

#SOLUTION:
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
if (x>y):
    maximum_number=x
else:
    maximum_number=y
print("The maximum number between first and second number is", maximum_number)

# OUTPUT:
# Enter the first number: 9
# Enter the second number: 4
# The maximum number between first and second number is 9
