# Import pandas as pd
import pandas as pd

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())

'''
Read in "sales.csv", saving as a pandas DataFrame called sales_df.
Subset sales_df on the "order_value" column, then call the .mean() method to find the average order value.
Subset sales_df on the "order_value" column, then call the .sum() method to find the total value of all orders.
'''

# Read in sales.csv
sales_df = pd.read_csv("sales.csv")

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())
