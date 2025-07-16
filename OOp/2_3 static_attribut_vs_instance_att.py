# Static Attributes

# A static att ( sometime called a class att) is an att
# that belongs to the class, not to any specific instance 
# of the class
# itself, not to any specific instance of the class

#KEEP track of the user obj created from user class
class User:
    #creating static att
    user_count = 0

    #instance att
    def __init__(self, username, email):
        self.username = username
        self.email = email

        User.user_count += 1

    #method for displaying user acc
    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


user1 = User("Tiger", "igtre@hot.com")
user2 = User("Lion", "onil@hot.com")
user3 = User("Deer", "eedr@hot.com")

#print(User.user_count)
print(user1.user_count)
print(user2.user_count)
