#Question Description
"""
Write a Python program to check whether a number is palindrome or not.
"""

#Solution
def palindrome(num):
    original_num=num
    reversed_num=0
    while num>0:
        digit=num%10
        reversed_num=reversed_num*10+digit
        num=num//10

    return original_num==reversed_num

num=int(input("Enter the number: "))

if palindrome(num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")

#Output
# Enter the number: 121
# 121 is a palindrome
