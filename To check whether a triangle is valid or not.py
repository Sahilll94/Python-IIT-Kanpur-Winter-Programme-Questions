#Question Description
"""
Write a Python program to input all sides of a triangle and check whether triangle is valid or not.
"""

#Solution
Side_1=float(input("Enter the length of first side of the triangle:"))
Side_2=float(input("Enter the length of Second side of the triangle:"))
Side_3=float(input("Enter the length of Third side of the triangle:"))
if Side_1+Side_2>Side_3 and Side_1+Side_3>Side_2 and Side_2+Side_3>Side_1:
    print("The triangle is valid")
else:
    print("The triangle is not valid")

#Output
# Enter the length of first side of the triangle:80
# Enter the length of Second side of the triangle:40
# Enter the length of Third side of the triangle:60
# The triangle is valid
