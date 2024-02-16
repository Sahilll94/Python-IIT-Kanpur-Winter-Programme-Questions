#Question Description
"""
Write a Python program to print all alphabets from a to z. - using  loop.
"""

#Solution
print("Alphabets from a to z are:")
for char in range(ord("a"),ord("z")+1):
    print(chr(char),end="")

#Output
Alphabets from a to z are:
abcdefghijklmnopqrstuvwxyz
