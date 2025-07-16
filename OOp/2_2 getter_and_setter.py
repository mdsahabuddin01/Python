#1. The traditional way: make the data private and use getters and setters
from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username

        # prefixing _ to make data att protected
        # when it's protected we shouldn't read att outside of classes
        # or any of its subclassess
        self._email = email
        self.password = password


    #to get access of private att, convention is to use getters and setters
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email.lower().strip()

    def set_email(self, new_email):
        if "@" in new_email:
            self._email = new_email



user1 = User("Snowman", " Snow@email.com ", "123")

# we shouldn't use _email as a responsible py dev
#print(user1._email)

print(user1.get_email())

# we could set a value directly like below
# user1._email = "123123"
# we shouldn't do that cause 

#by convention, used within class, above

user1.set_email("md@email.net")

print(user1.get_email())
