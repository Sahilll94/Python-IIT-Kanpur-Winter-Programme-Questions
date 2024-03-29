"""
Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String.
"""

#Solution
User_string=input("Enter the string: ")

if len(User_string)>=2:
    new_string=User_string[:2]+User_string[-2:]
    print(f"The new string is: {new_string} ")
else:
    print("The input string should have atlease 2 char")

#Output
# Enter the string: python
# The new string is: pyon
