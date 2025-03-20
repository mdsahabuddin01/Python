#Find elements in prices that are greater than price_mean and assign the boolean result to boolean_array.
#Subset prices using boolean_array and assign the result to above_avg

import numpy as np

prices = np.array([ 55.28,  59.5 ,  93.29, 100.5 , 145.3 , 170.12, 171.81])

# Find the mean
price_mean = np.mean(prices)

# Create boolean array
boolean_array = (prices > price_mean)
print(boolean_array)

# Select prices that are greater than average
above_avg = prices[boolean_array]
print(above_avg)

#Find elements in sectors that are equivalent to 'Health Care' and assign the result to boolean_array.
#Subset names using boolean_array and assign the result to health_care.

names  = np.array(['Apple Inc', 'Abbvie Inc', 'Abbott Laboratories',
       'Accenture Technologies', 'Allergan Plc'])

sectors = np.array(['Information Technology', 'Health Care', 'Health Care',
       'Information Technologies', 'Health Care'])

# Create boolean array
boolean_array = (sectors == 'Health Care')
print(boolean_array)

# Print only health care companies
health_care = names[boolean_array]
print(health_care)
