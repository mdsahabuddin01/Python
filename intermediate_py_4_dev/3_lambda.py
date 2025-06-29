#Define the add_tax lambda function to multiply the argument provided to it, x, by 1.2.
#Call add_tax() on the sale_price variable.



sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x * 1.2

# Call the lambda function
print(add_tax(sale_price))

#In a single line of code, make a lambda function that multiplies sale_price by 1.2 and returns the results.

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x * 1.2)(sale_price))


#Lambda functions with iterables
'''


Create add_taxes using a lambda function that multiplies each value in sales_prices by 20%.
Create a new list called sales_plus_tax, by converting add_taxes to a list.
Print the sales_plus_tax list.
'''

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x * 1.2, sales_prices)

# Create the updated list, sales_plus_tax
sales_plus_tax = list(add_taxes)

# Print the new list with updated values
print(sales_plus_tax)
