#Question Description
"""
Write a Python program to find sum of all natural numbers between 1 to n.
"""

#Solution
n=int(input("Enter the positive integer: "))

if not isinstance(n, int) or n<=0:
    print("Please enter a positive integer.")
else:
    sum_natural_numbers=0
    for i in range(1,n+1):
        sum_natural_numbers += i

    print("The sum of natural numbers from 1 to",n, "is", sum_natural_numbers)

#Output
# Enter the positive integer: 4
# The sum of natural numbers from 1 to 4 is 10
