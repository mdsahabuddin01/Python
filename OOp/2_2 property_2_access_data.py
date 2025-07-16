class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

#getter property
    @property
# creating method same, as we are decorating property for 
    def email(self):
        print("Email Accessed!")
        return self._email.lower().strip()
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email



user1 = User("Snowman", " Snow@email.com ", "123")
user1.email = "123@123.123"
print(user1.email)
