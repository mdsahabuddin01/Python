#1. The traditional way: make the data private and use getters and setters
class User:
    def __init__(self, username, email, password):
        self.username = username

        # prefixing _ to make data att protected
        # when it's protected we shouldn't read att outside of classes
        # or any of its subclassess
        self._email = email
        self.password = password

    #creating a method
    def clean_email(self):
        return self._email.lower().strip()


user1 = User("Snowman", " snow@email.com ", "123")

"""
user2 = User("rainman", "rain@email.com", "abc")
user1.say_hi_to_user(user2)
"""
print(user1._email)
print(user1.clean_email())
