#Question Description
"""
Write a Python program to sum number of digits in a number.
"""

#Solution
n=int(input("Enter the integer you wish to calculate the sum: "))
if not  isinstance(n,int) or n<0:
    print("Please enter the valid number.")
else:
    sum_of_digits=0
    original_num=n

    while n>0:
        digit=n%10
        sum_of_digits += digit
        n //= 10

    print("The sum of digits of",original_num,"is:",sum_of_digits)

#Output
Enter the integer you wish to calculate the sum: 567
The sum of digits of 567 is: 18

