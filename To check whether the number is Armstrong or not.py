#Question DEscription
"""
Write a Python program to check whether a number is Armstrong number or not.
"""

#Solution

def is_armstrong(num):
    original_num=num
    num_digits=len(str(num))
    armstrong_sum=0

    while num>0:
        digit=num%10
        armstrong_sum += digit**num_digits
        num //= 10

    return armstrong_sum == original_num
num=int(input("Enter the number: "))

if is_armstrong(num):
    print("the number",num,"is Armstrong number.")
else:
    print("The number",num,"is not an Armstrong number.")

#Output
# Enter the number: 153
# the number 153 is Armstrong number.


