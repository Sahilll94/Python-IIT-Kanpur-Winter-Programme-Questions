'''
Delete a list of keys from a dictionary

Given dictionary:

sample_dict = {
    "name": "Ram",
    "age": 25,
    "salary": 8000,
    "city": "Delhi"}

# Keys to extract
keys = ["name", "salary"]
Expected output:

{'city': 'Delhi', 'age': 25}
'''

#Solution
sample_dict = {
    "name": "Ram",
    "age": 25,
    "salary": 8000,
    "city": "Delhi"}

keys_to_delete = ["name", "salary"]

filtered_dict = {key: value for key, value in sample_dict.items() if key not in keys_to_delete}

print(filtered_dict)

