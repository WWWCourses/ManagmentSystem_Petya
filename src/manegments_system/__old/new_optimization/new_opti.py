import os




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
