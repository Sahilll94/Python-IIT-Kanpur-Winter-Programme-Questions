# Question Description
"""
Write a Python program to find sum of all even numbers between 1 to n.
"""

# Solution
n=int(input("Enter the positive integer: "))
if not isinstance(n,int) or n<=0:
    print("Enter a positive number")
else:
      sum_even_numbers=0
    for i in range(2,n+1,2):
        sum_even_numbers += i

    print("the sum of even numbers from 2 to", n, "is", sum_even_numbers)

# Output
# Enter the positive integer: 4
# the sum of even numbers from 2 to 4 is 6

  
