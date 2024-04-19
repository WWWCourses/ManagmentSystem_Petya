# Initialize an empty dictionary to store user records
user_records = {}

# Function to add a new user
def add_user():
    name = input("Enter user's name: ")
    dob = input("Enter user's date of birth (YYYY-MM-DD): ")
    address = input("Enter user's address: ")
    user_records[name] = {'Date of Birth': dob, 'Address': address}
    print("User added successfully!")

# Function to delete a user
def delete_user():
    name = input("Enter the name of the user you want to delete: ")
    if name in user_records:
        del user_records[name]
        print("User deleted successfully!")
    else:
        print("User not found.")

# Function to view user data
def view_user_data():
    name = input("Enter the name of the user you want to view: ")
    if name in user_records:
        print("User Data:")
        print("Name:", name)
        print("Date of Birth:", user_records[name]['Date of Birth'])
        print("Address:", user_records[name]['Address'])
    else:
        print("User not found.")

# Function to save user records
def save_records():
    # You can implement the saving mechanism here, such as saving to a file/database
    print("Records saved successfully!")


# if __name__=='__main__':
#     main()


