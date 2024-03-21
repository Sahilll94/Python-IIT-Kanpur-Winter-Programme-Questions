#Question Description
"""
Python Program to Check if a String is a Palindrome or Not.
"""

#Solution
def is_palindrome(string):
    cleaned_string= ''.join(string.split()).lower()
    return cleaned_string==cleaned_string[::-1]

User_string=input("Enter a string: ")

if is_palindrome(User_string):
    print(f"The given String '{User_string} is a palindrome")
else:
    print(f"The given String '{User_string} is not a palindrome")

#Output
Enter a string: aha
The given String 'aha is a palindrome


