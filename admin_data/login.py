# Start main program
# def main():
#     if admin_login():
#         print("\nHello! Welcome, to the user managment system!")
#     else:
#         print("\nLogin failed. Please check the entered data.")
    

# # Function to authenticate the administrator

# def admin_login():
#     print("Administrator Login")
#     name = input("Enter your name: ") ### adding a dict with keys for first name, last name, last name
#     dob = input("Enter your date of birth (YYYY-MM-DD): ") 
#     address = input("Enter your address: ") ### adding a dict for city, str., nomber, ZIP code

#     # return True ### Only valid for demonstration proposes

# if __name__ == "__main__":
#     main()



# I can customize the admin login to the system, add job title for example 
# for date of birth I can adding a button with a drop-down menu to select date, month, year
# does the user have the necessary credentials to log in as adminstrator?- how to make it?
   

# Start main orogram

def main():
    if admin_login():
        print("\nHello! Welcome, to the user managment system!")
    else:
        print("\nLogin failed. Please check the entered data.")

   # Define a dictionary to store admin information

users = {}

# Function to register a new user

def register():
    print("Welcome to the registration process.")
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    address_city = input("Enter your city: ")
    address_street = input("Enter your street: ")
    address_number = input("Enter your house number: ")
    pin_code = input("Create a pin code: ")
    username = input("Create a username: ")
    
    # Store the user information in the dictionary
    users[username] = {
        'name': name,
        'surname': surname,
        'dob': dob,
        'address': {
            'city': address_city,
            'street': address_street,
            'number': address_number
        },
        'pin_code': pin_code
    }
    print("Registration successful!")

# Function to log in

def admin_login():
    username = input("Enter your username: ")
    pin_code = input("Enter your pin code: ")
    
    # Check if the username exists and if the pin code is correct

    if username in users and users[username]['pin_code'] == pin_code:
        print("Hello! Welcome to the management system!")
    else:
        print("Invalid username or pin code. Please try again.")

# Main program loop

while True:
    print("\nChoose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        admin_login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
 
    
    
if __name__ == '__main__':
    main()
    

 