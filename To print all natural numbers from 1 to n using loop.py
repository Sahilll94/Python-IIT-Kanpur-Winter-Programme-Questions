#Question Description
"""
Write a Python program to print all natural numbers from 1 to n using loop.
"""

#Solution
n=int(input("Enter the value of n:"))
print("Natural numbers from 1 to",n,"are:")
for i in range(1,n+1):
    print(i,end="")

#Output
# Enter the value of n:2
# Natural numbers from 1 to 2 are:
# 12

