# Hiding Implementation details
# Separation of concerns

def get_input():
    print("Getting user input")

def valid_input():
    print("Validating the user info")

def save_to_db():
    print("Saving to database")

def register_user():
    get_input()
    valid_input()
    save_to_db()
    print("User registeration complete")

register_user()