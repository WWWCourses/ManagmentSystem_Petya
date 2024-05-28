import os

class User:
    def __init__(self, name, surname, dob, address, username, pin_code):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.address = address
        self.username = username
        self.pin_code = pin_code

    def __str__(self):
        return f'{self.name} {self.surname}, {self.dob}, {self.address}, {self.username}, {self.pin_code}'

class UserManager:
    def __init__(self, db_file='user_db.txt'):
        self.users = []
        self.db_file = db_file
        self.load_users()

    def load_users(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 6:
                        self.users.append(User(*data))

    def save_users(self):
        with open(self.db_file, 'w') as file:
            for user in self.users:
                file.write(f'{user.name},{user.surname},{user.dob},{user.address},{user.username},{user.pin_code}\n')

    def add_user(self, name, surname, dob, address, username, pin_code):
        if self.find_user_by_username(username):
            print("Error: Username already exists.")
            return
        if self.find_user_by_pin(pin_code):
            print("Error: Pin code already taken.")
            return
        new_user = User(name, surname, dob, address, username, pin_code)
        self.users.append(new_user)
        print("User added successfully.")

    def delete_user(self, username):
        user = self.find_user_by_username(username)
        if user:
            self.users.remove(user)
            print("User deleted successfully.")
        else:
            print("Error: User not found.")

    def show_user(self, username):
        user = self.find_user_by_username(username)
        if user:
            print(user)
        else:
            print("Error: User not found.")

    def list_users(self):
        for user in self.users:
            print(user)

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def find_user_by_pin(self, pin_code):
        for user in self.users:
            if user.pin_code == pin_code:
                return user
        return None

def admin_login():
    name = input("Enter administrator name: ")
    dob = input("Enter administrator date of birth (YYYY-MM-DD): ")
    address = input("Enter administrator address: ")
    print(f"Hello {name}! Welcome to the management system.")
    return name, dob, address

def main():
    admin_name, admin_dob, admin_address = admin_login()
    user_manager = UserManager()

    while True:
        print("\nWould you like to --")
        print("1. See current Users")
        print("2. Add User")
        print("3. Delete User")
        print("4. Show a User")
        print("5. Save Database")
        print("6. More Options")
        print("7. Quit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            user_manager.list_users()
        elif choice == 2:
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            address = input("Enter address: ")
            username = input("Enter username: ")
            pin_code = input("Enter pin code: ")
            user_manager.add_user(name, surname, dob, address, username, pin_code)
        elif choice == 3:
            username = input("Enter username to delete: ")
            user_manager.delete_user(username)
        elif choice == 4:
            username = input("Enter username to show: ")
            user_manager.show_user(username)
        elif choice == 5:
            user_manager.save_users()
            print("Database saved successfully.")
        elif choice == 6:
            print("More options are not implemented yet.")
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
