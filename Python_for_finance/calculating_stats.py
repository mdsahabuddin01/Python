import numpy as np

prices = np.array([170.12,  93.29,  55.28, 145.3 , 171.81,  59.5 , 100.5 ])

# Calculate the mean 
prices_mean = np.mean(prices)
print(prices_mean)

# Calculate the standard deviation 
prices_std = np.std(prices)
print(prices_std)
