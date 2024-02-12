#Question Description
"""
Write a Python program to check whether a character is uppercase or lowercase alphabet
"""

#Solution
Alpha=input("Enter the alphabet:")
if len(Alpha)==1:
    if Alpha.isalpha():
        if Alpha.islower():
            print(f"{Alpha} is a lowercase alphabet")
        elif Alpha.isupper():
            print(f"{Alpha} is a uppercase alphabet")
else:
    print(f"{Alpha} is not a valid alphabet or it is not a single alphabet")


#OUTPUT
# Enter the alphabet:S
# S is a uppercase alphabet
