#Question Description
"""
Python Program to Count the Number of Vowels in a String.
"""

#Solution
def count_vowels(string):
    vowels="AEIOUaeiou"
    vowel_count=0

    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

n=input("Enter a string: ")
result=count_vowels(n)
print("Numbers of vowels in the string are:",result)

#Output
# Enter a string: Sahil
# Numbers of vowels in the string are: 2
