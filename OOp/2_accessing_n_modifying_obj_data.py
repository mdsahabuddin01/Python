class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    
    def say_hi_to_user(self, user):
        print(
            f"Sending message to user {user.username}: hi, {user.username}! this is {self.username}."
        )

user1 = User("Snowman", "snow@email.com", "123")
"""
user2 = User("rainman", "rain@email.com", "abc")
user1.say_hi_to_user(user2)
"""

print(user1.email)
#modifying object data
user1.email = "snowman@gmail.com"
print(user1.email)
#problem is, we can modify and give any data
