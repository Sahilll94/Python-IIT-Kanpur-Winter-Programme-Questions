#Question Description
'''
Create a dictionary by extracting the keys from a given dictionary.
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

Given dictionary:

sample_dict = {
    "name": "Ram",
    "age": 25,
    "salary": 8000,
    "city": "Delhi"}

# Keys to extract
keys = ["name", "salary"]
Expected output:

{'name': 'Ram', 'salary': 8000}
'''

#CODE
sample_dict = {
    "name": "Ram",
    "age": 25,
    "salary": 8000,
    "city": "Delhi"}

keys_to_extract = ["name", "salary"]

extracted_dict = {key: sample_dict[key] for key in keys_to_extract}
print(extracted_dict)

