#Question Description
'''
Check if a value exists in a dictionary We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
Write a Python program to check if value 200 exists in the following dictionary.
Given:
sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
200 present in a dict
'''

#Solution
sample_dict = {'a': 100, 'b': 200, 'c': 300}
target_value = 200

if target_value in sample_dict.values():
    print(f"{target_value} present in dict")
else:
    print(f"{target_value} not present in dict")

#Output
200 present in dict

