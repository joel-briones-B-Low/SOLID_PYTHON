

# Incorrect

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_db(self, db_connection):
        print(f"Saving {self.name} to the database.")
        pass

    def send_email(self, subject, body):
        print(f"Sending email to {self.email}.")
        pass
# Correct
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
class UserService:
    def save_to_db(self, user, db_connection):
        print(f"Saving {user.name} to the database.")
        pass