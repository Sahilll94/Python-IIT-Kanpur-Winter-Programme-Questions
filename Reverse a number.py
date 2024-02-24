#Question Description
"""
Write a Python program to enter a number and print its reverse.
"""

#Solution
def reverse():
    num=int(input("Enter a number: "))

    reversed_num=0

    while num>0:
        digit=num%10
        reversed_num=reversed_num*10+digit
        num=num//10

    print("Reverse number is",reversed_num)

reverse()

#Output
Enter a number: 345678
Reverse number is 876543
