#Question Description
"""
Write a Python program to input basic salary of an employee and calculate its Gross salary according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%
"""

#Solution
def Calculate_GS(basic_salary):
    if basic_salary <=10000:
        hrap=0.20
        dap=0.80
    elif basic_salary <=20000:
        hrap=0.25
        dap=0.90
    else:
        hrap=0.30
        dap=0.95
    hra=basic_salary*hrap
    da=basic_salary*dap
    gross_salary=basic_salary+hra+da
    return gross_salary
basic_salary=float(input("enter your basic salary:"))
gross_salary = Calculate_GS(basic_salary)
print(f"Gross Salary:${gross_salary:.2f}")

#Output
# enter your basic salary:20000
# Gross Salary:$43000.00
