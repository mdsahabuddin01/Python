"""Customizing your NumPy import
What if there are rows, such as a header, that you don't want to import? What if your file has a delimiter other than a comma? What if you only wish to import particular columns?

There are a number of arguments that np.loadtxt() takes that you'll find useful:

delimiter changes the delimiter that loadtxt() is expecting.
You can use ',' for comma-delimited.
skiprows allows you to specify how many rows (not indices) you wish to skip
You can use '\t' for tab-delimited.
usecols takes a list of the indices of the columns you wish to keep.
The file that you'll be importing, digits_header.txt, has a header and is tab-delimited. """

# Import numpy
import numpy as np

# Assign the filename: file
file = 'mnist_kaggle_some_rows.csv'

# Load the data: data
data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0,2])

# Print data
print(data)


