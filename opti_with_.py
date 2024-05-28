class UserDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                users = [line.strip().split(',') for line in file.readlines()]
                return users
        except FileNotFoundError:
            return []
        
# Function to see current users 
      
    def see_current_users(self):
        if not self.users:
            print("No users in the database.")
        else:
            print("Current Users:")
            for user in self.users:
                print(', '.join(user))

# Function to register a new user

    def add_user(self, new_user):
        for user in self.users:
            if user[4] == new_user[4]:
                print("Username already exists.")
                return
        self.users.append(new_user)
        self.save_users()
        print("User added successfully.")

# Function to delete a user

    def delete_user(self, username):
        for user in self.users:
            if user[4] == username:
                self.users.remove(user)
                self.save_users()
                print("User deleted successfully.")
                return
        print("User not found.")

# Function to view user data

    # def show_user_data(self, username):
    #     username = input( 'Enter username of the user to view data:')
    #     for user in self.users:
    #         if user[4] == username:
    #             self.users.show_user_data(user)
    #             print()

        
# Function to save user database to a file

    def save_users(self):
        with open(self.file_path, 'w') as file:
            for user in self.users:
                file.write(','.join(user) + '\n')

    
    
    
    def run(self):
        while True:
            print("\n1. See current users")
            print("2. Add new user")
            print("3. Delete user")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_users()
            elif choice == '2':
                name = input("Enter name: ")
                surname = input("Enter surname: ")
                dob = input("Enter date of birth (DD/MM/YYYY): ")
                address = input("Enter address: ")
                username = input("Enter username: ")
                pin_code = input("Enter pin code: ")
                new_user = [name, surname, dob, address, username, pin_code]
                self.add_user(new_user)
            elif choice == '3':
                username = input("Enter username to delete: ")
                self.delete_user(username)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


# Example usage
if __name__ == "__main__":
    db = UserDatabase("user_database.txt")
    db.run()
