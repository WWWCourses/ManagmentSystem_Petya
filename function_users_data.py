# Define a dictionary to store user information

users = {}

# Function to see current users

def see_current_users():
    print("Current Users:")
    for username in users:
        print(username)

# Function to register a new user

def add_user():
    print("Welcome to the registration process.")
    name = input("Please enter a name: ")
    surname = input("Please enter user's surname: ")
    date_of_birth = input("Please enter user's DOB: [DD/MM/YYYY] ")
    address_city = input("Please enter user's city: ")
    address_street = input("Please enter user's street: ")
    address_number = input("Please enter user's house number: ")
    pin_code = input("Create a pin code for the user: ")
    username = input("Create a username for the user: ")
    
    # Create a new user dictionary and store it in the users dictionary

    users[username] = {
        'name': name,
        'surname': surname,
        'date_of_birth': date_of_birth,
        'address_city': address_city,
        'address_street': address_street,
        'address_number': address_number,
        'pin_code': pin_code
    }
    print("New user added!")

# Function to delete a user

def delete_user():
    username = input("Enter username of the user to delete: ")
    if username in users:
        del users[username]
        print("User deleted successfully.")
    else:
        print("User not found.")

# Function to view user data

def show_user_data():
    username = input("Enter username of the user to view data: ")
    if username in users:
        user = users[username]
        print(f"Name: {user['name']}")
        print(f"Surname: {user['surname']}")
        print(f"Date of Birth: {user['date_of_birth']}")
        print(f"Address: {user['address_number']}, {user['address_street']}, {user['address_city']}")
    else:
        print("User not found.")

# Function to save user database to a file

def save_user_database():
    filename = input("Enter filename to save user database (e.g., users.txt): ")
    with open(filename, 'w') as file:
        for username, user in users.items():
            file.write(f"Username: {username}\n")
            file.write(f"Name: {user['name']}\n")
            file.write(f"Surname: {user['surname']}\n")
            file.write(f"Date of Birth: {user['date_of_birth']}\n")
            file.write(f"Address: {user['address_number']}, {user['address_street']}, {user['address_city']}\n")
            file.write("\n")
    print("User database saved successfully.")
