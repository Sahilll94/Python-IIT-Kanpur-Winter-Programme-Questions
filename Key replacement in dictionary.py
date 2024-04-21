#Question Description
'''
Rename key of a dictionary Write a program to rename a key city to a
location in the following dictionary.
Given:
sample_dict = {
  "name": "Ram",
  "age":25,
  "salary": 8000,
  "city": "Delhi"
}

Expected output:

{'name': 'Ram', 'age': 25, 'salary': 8000, 'location': 'Delhi'}
'''

#Solution
sample_dict = {
  "name": "Ram",
  "age": 25,
  "salary": 8000,
  "city": "Delhi"
}

# Renaming the key
sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)


#If you wish to rename the value in a dict, then you can use the same eg. sample_dict["city"] = "Mumbai"
#Always remember to target the key always to rename key or value.
