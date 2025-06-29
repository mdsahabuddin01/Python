
'''
Python allows custom functions to accept any number of positional arguments through the use of "Arbitrary arguments". This flexibility enables functions to be used in a variety of ways while still producing the expected results!

Using this power, you'll build a function that concatenates (joins together) strings, regardless of how many blocks of text are provided!
'''
# Define a function called concat
def concat(*args):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python args tuple
  for arg in args:
    result += " " + arg
  return result

# Call the function
print(concat("Python", "is", "great!"))

'''

Arbitrary keyword arguments
Arbitrary positional arguments are one way to add flexibility when creating custom functions, but you can also use arbitrary keyword arguments.

Your goal is to take the concat function that you created in the last exercise and modify it to accept arbitrary keyword arguments. Good luck!
'''

# Define a function called concat
def concat(**kwargs):
  
  # Create an empty string
  result = ""
  
  # Iterate over the Python kwargs
  for kwarg in kwargs.values():
    result += " " + kwarg
  return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))
