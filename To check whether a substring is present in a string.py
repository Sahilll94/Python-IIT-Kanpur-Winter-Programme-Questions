#Question Description
"""
Python Program to Check if a Substring is Present in a Given String.
"""

#Solution
def is_substringPRESENT(string,substring):
    return substring in string

string=input("Enter the string: ")
substring=input("Enter the substring: ")

if is_substringPRESENT(string,substring):
    print("The subtring",substring,"is available in",string)
else:
    print("it is not present.")

#Output
# Enter the string: SAHIL
# Enter the substring: AH
# The subtring AH is available in SAHIL
