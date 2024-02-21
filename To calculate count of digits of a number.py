#Question Description
"""
Write a Python program to calculate count of digits of a number.
"""

#Solution
n=int(input("Enter the number you wish to calculate the counting: "))
if not isinstance (n,int) or n<0:
    print("Please enter the valid number")
else:
    count_digit=0
    original_num=n

    while n>0:
        count_digit += 1
        n //=10

    print("The counting of the given number",original_num,"is:",count_digit)

#Output
Enter the number you wish to calculate the counting: 456789
The counting of the given number 456789 is: 6
