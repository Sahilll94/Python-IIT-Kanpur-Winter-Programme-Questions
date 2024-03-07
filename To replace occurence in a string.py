#Question Description
"""
Python Program to Replace all Occurrences of ‘a’ with $ in a String.
"""

#Solution
def replace(string):
    modified_string = string.replace('a','$')

    return modified_string

string=input("Enter the string: ")

modified_string=replace(string)
print("modified string is", modified_string)


#Output
# Enter the string: Sahil
# modified string is S$hil
