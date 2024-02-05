"""
Write a python program to enter Amount, Time, Rate and calculate Simple Interest.
"""

#SOLUTION
Amount=float(input("Enter the Amount in Indian Rupees: "))
Time=float(input("Enter the Time in years: "))
Rate=float(input("Enter the Rate: "))
Simple_interest=(Amount*Time*Rate)/100
print("The Simple Interest for the given Amount:₹",Amount,"Time:",Time," years Rate:",Rate,"is ₹",Simple_interest)

#OUTPUT
# Enter the Amount in Indian Rupees: 1000
# Enter the Time in years: 2
# Enter the Rate: 5
# The Simple Interest for the given Amount:₹ 1000.0 Time: 2.0  years Rate: 5.0 is ₹ 100.0
