# Import numpy as np
import numpy as np

# Lists
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# NumPy arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Print the arrays
print(prices_array)
print(earnings_array)

# Create PE ratio array
pe_array = prices_array/earnings_array

# Print pe_array
print(pe_array)

# Subset the first three elements
prices_subset_1 = prices_array[0:3]
print(prices_subset_1)

# Subset last three elements 
prices_subset_2 = prices_array[-3:]
print(prices_subset_2)

# Subset every third element
prices_subset_3 = prices_array[0:7:3]
print(prices_subset_3)
