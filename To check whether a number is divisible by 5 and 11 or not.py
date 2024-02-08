"""
Write a Python program to check whether a number is divisible by 5 and 11 or not.
"""

#SOLUTION:
x=int(input("Enter the number you wish to check whether it is divisible by 5 and 11 or not: "))
if (x%5==0) and (x%11==0):
        print("The number",x,"is divisible by 5 and 11")
else:
    print("The provided number",x,"is not divisible by 5 and 11")

# OUTPUT:
# Enter the number you wish to check whether it is divisible by 5 and 11 or not: 110
# The number 110 is divisible by 5 and 11
