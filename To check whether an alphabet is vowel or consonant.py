#QUESTION DESCRIPTION
"""
Write a Python program to input any alphabet and check whether it is vowel or consonant.
"""

#SOLUTION
a=input("Enter the alphabet: ")
a=a.lower()
if len(a)==1 and a.isalpha():
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        print("The alphabet", a,"is a vowel")
else:
    print("The element is a consonant")

#OUTPUT
# Enter the alphabet: a
# The alphabet a is a vowel
