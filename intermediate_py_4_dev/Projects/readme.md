#creating functions to register app users

Create a validate_user() function, using some helper validation functions to verify user input.

The function should take in the parameters: name, email, and password.
The function should call each of the helper validation functions (validate_name(), validate_email(), and validate_password()).
If any check fails, raise a ValueError with a descriptive error message about the failing validation.
If all checks pass, return True.
Now that you've validated that all the user details are correct, you want to allow users to register to the app. Create a register_user() function to handle the registration logic.

The function should take in the parameters: name, email, and password.
Inside, it should call validate_user() to ensure that the user input is valid.
If validate_user() raises a ValueError, register_user() should catch the exception and return False.
Otherwise, it should create and return a dictionary with the keys: name, email, and password.
