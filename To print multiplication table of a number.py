#Question Description
"""
Write a Python program to print multiplication table of any number.
"""

#Solution
n=int(input("Enter the integer for multiplication till 10: "))
print("The multiplication of",n,"is given below:")
for i in range(1,11):
    product=n*i
    print(n,"*",i,"=",product)

#Output
# Enter the integer for multiplication till 10: 4
# The multiplication of 4 is given below:
# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12
# 4 * 4 = 16
# 4 * 5 = 20
# 4 * 6 = 24
# 4 * 7 = 28
# 4 * 8 = 32
# 4 * 9 = 36
# 4 * 10 = 40
