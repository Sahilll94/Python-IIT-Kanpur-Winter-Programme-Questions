#Question Description
"""
Initialize dictionary with default values In Python, we can initialize the keys with the same values.

Given:
employees = ['Ram', 'Amit']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:
{'Ram': {'designation': 'Developer', 'salary': 8000}, 'Amit': {'designation': 'Developer', 'salary': 8000}}
"""

#Solution
employees = ['Ram', 'Amit']
defaults = {"designation": 'Developer', "salary": 8000}

employee_dict = {employee: defaults.copy() for employee in employees}
print(employee_dict)
