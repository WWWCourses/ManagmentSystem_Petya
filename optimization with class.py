class User:
    def __init__(self, name, surname, date_of_birth, address_city, address_street, address_number, pin_code):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.address_city = address_city
        self.address_street = address_street
        self.address_number = address_number
        self.pin_code = pin_code

# Define a dictionary to store user information
users = {}

# Function to see current users

def see_current_users():
    print("Current Users:")
    for username in users:
        print(username)

# Function to register a new user
def register_user():
    print("Welcome to the registration process.")
    name = input("Enter user's name: ")
    surname = input("Enter user's surname: ")
    date_of_birth = input("Enter user's date of birth (DD/MM/YYYY): ")
    address_city = input("Enter user's city: ")
    address_street = input("Enter user's street: ")
    address_number = input("Enter user's house number: ")
    pin_code = input("Create a pin code for the user: ")
    username = input("Create a username for the user: ")
    
    # Create a new User object and store it in the dictionary
    users[username] = User(name, surname, date_of_birth, address_city, address_street, address_number, pin_code)
    print("User registration successful!")

# Function to delete a user
def delete_user():
    username = input("Enter username of the user to delete: ")
    if username in users:
        del users[username]
        print("User deleted successfully.")
    else:
        print("User not found.")

# Function to view user data
def view_user_data():
    username = input("Enter username of the user to view data: ")
    if username in users:
        user = users[username]
        print(f"Name: {user.name}")
        print(f"Surname: {user.surname}")
        print(f"Date of Birth: {user.date_of_birth}")
        print(f"Address: {user.address_number}, {user.address_street}, {user.address_city}")
    else:
        print("User not found.")

# Function to save user database to a file
def save_user_database():
    filename = input("Enter filename to save user database (e.g., users.txt): ")
    with open(filename, 'w') as file:
        for username, user in users.items():
            file.write(f"Username: {username}\n")
            file.write(f"Name: {user.name}\n")
            file.write(f"Surname: {user.surname}\n")
            file.write(f"Date of Birth: {user.date_of_birth}\n")
            file.write(f"Address: {user.address_number}, {user.address_street}, {user.address_city}\n")
            file.write("\n")
    print("User database saved successfully.")

# Main program loop
while True:
    print("\nChoose an option:")
    print("1. See current users")
    print("2. Register a new user")
    print("3. Delete a user")
    print("4. View user data")
    print("5. Save user database to a file")
    print("6. Additional options")  # Placeholder for additional options
    print("7. Quit")
    choice = input("Enter your choice: ")

    if   choice == '1':
        see_current_users()
    elif choice == '2':
        register_user()
    elif choice == '3':
        delete_user()
    elif choice == '4':
        view_user_data()
    elif choice == '5':
        save_user_database()
    elif choice == '6':
        print("Additional options will be added here.")
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
