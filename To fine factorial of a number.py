#Question Description
"""
Write a Python program to calculate factorial of a number.
"""

#Solution
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

num=int(input("Enter the number: "))

if num<0:
    print("factorial is not defined for negative numbers")
else:
    result=factorial(num)
    print("The factorial of",num,"is",result)


#Output
Enter the number: 4
The factorial of 4 is 24

