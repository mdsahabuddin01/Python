#Defining a custom function
'''
Define a function called clean_string, which takes an argument called text.
Inside the function, create a variable called no_spaces, which contains the text with spaces replaced by underscores.
Inside the function, create a variable called clean_text, which converts characters in no_spaces to lowercase.
Finish the function by producing clean_text as an output.
'''

# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  cleaned_text = no_spaces.lower()
  
  # Return the final text as an output
  return cleaned_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)

'''
Define the password_checker function, which should accept one argument called submission.
Check if password is equal to submission.
Add a keyword enabling the conditional printing of "Incorrect password" if password and submission are different.
Call the function, passing "NOT_VERY_SECURE_2023".
'''

password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
  # Check that the password variable and the submission match
  if password == submission:
    print("Successful login!")
  
  # Otherwise, print "Incorrect password"
  else:
    print("Incorrect password")

# Call the function    
password_checker("NOT_VERY_SECURE_2023")
