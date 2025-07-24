# Abstraction

# Reduce complexity by Hiding unnecessary details

class EmailService:
    
    def _connect(self):
        print("Connecting to email server")

    def _authonticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authonticate()
        print("Sending Email....")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server....")



email = EmailService()
email.send_email()
