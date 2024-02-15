#Question Description
"""
Write a Python program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill.
"""

#Solution
def calculate_bill(units):
    if units<=50:
        rate = 0.50
    elif units<=100:
        rate=0.75
    elif units<=200:
        rate=1.20
    else:
        rate=1.50
    total_cost=units*rate
    total_cost_surcharge=total_cost+(0.20*total_cost)
    return total_cost_surcharge
units=float(input("Enter the electricity units consumed:"))

total_bill=calculate_bill(units)
print(f"Total electricity bill: Rs.{total_bill}")

#Output
# Enter the electricity units consumed:50
# Total electricity bill: Rs.30.0
