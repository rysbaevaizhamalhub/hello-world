# Aizhamal Rysbaeva
# Oct 8, 2024

# a program that computes MPG for a car

# asking user to enter the number of miles
miles = input("Enter the number of miles driven: ")

# asking user to enter the number of gallons used
gallons = input("enter the number of gallons used: ")

# convert the inputs to numbers
miles = int(miles)
gallons = int(gallons)

# calculate miles per gallon
mpg = miles/gallons

# MPG result
print(f"The car's MPG is {mpg}")
