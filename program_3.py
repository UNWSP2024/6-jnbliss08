# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def sales_tax():
    state_rate = 0.05
    county_rate = 0.025
    state_tax = total_sales * state_rate
    county_tax = total_sales * county_rate
    total_tax = state_tax + county_tax
    return county_tax, state_tax, total_tax


total_sales = float(input("Enter the total sales: "))
county_tax, state_tax, total_tax = sales_tax()
print (f'county sales tax: ${county_tax:.2f}')
print (f'state sales tax: ${state_tax:.2f}')
print (f'total sales tax: ${total_tax:.2f}')