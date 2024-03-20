"""
Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
"""

#Question Description
def count_upper_lower(string):
    upper_count=0
    lower_count=0

    for char in string:
        if char.isupper():
            upper_count+=1
        elif char.islower():
            lower_count+=1

    return upper_count,lower_count

User_string=input("Enter the string: ")
upper,lower=count_upper_lower(User_string)

print(f"the number of uppercase in '{User_string}' is {upper}")
print(f"the number of lowercase in '{User_string}' is {lower}")

#Output
# Enter the string: SahIL Is A GooD BOy
# the number of uppercase in 'SahIL Is A GooD BOy' is 9
# the number of lowercase in 'SahIL Is A GooD BOy' is 6
