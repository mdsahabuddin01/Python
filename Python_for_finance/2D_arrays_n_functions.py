
prices = [170.12, 93.29, 55.28, 145.3, 171.81, 59.5, 100.5]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# Create a 2D array of prices and earnings
stock_array = np.array([prices, earnings])
print(stock_array)

# Print the shape of stock_array
print(stock_array.shape)

# Print the size of stock_array
print(stock_array.size)


# Transpose stock_array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)

# Print the shape of stock_array
print(stock_array_transposed.shape)

# Print the size of stock_array
print(stock_array_transposed.size)

# Subset prices from stock_array_transposed
#Extract the first column
prices = stock_array_transposed[:, 0]
print(prices)

# Subset earnings from stock_array_transposed
#Extract the second column
earnings = stock_array_transposed[:, 1]
print(earnings)

# Subset the price and earning for first company
company_1 = stock_array_transposed[0, :]
print(company_1)
