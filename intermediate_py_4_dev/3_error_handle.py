def snake_case(text):
  # Attempt to clean the text
  try:
    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  # Run this code if an error occurs
  except:
    print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")


#Returning errors

'''
Returning errors
Time to try out the other approach for error handling.

Revise the snake_case() function to intentionally produce an error if an incorrect data type is used.

Instructions
0 XP
Check whether the data type of the text argument is a string str.
Inside the else block, produce a TypeError() to prevent the script running and return a descriptive message.
'''

def snake_case(text):
  # Check the data type
  if type(text) == str:
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
snake_case("User Name 187")
