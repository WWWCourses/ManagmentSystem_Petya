from manegments_system.menu import show_menu
from manegments_system.user import User
from manegments_system.user_manager import UserManager
from manegments_system.admin import Admin

def main():
    # admin_name, admin_dob, admin_address = admin_login()
    admin = Admin()
    if admin.logged_in:
        print(admin.name)
    else:
        print('Admin is not loggedin. Buy!')
        exit() # exit the program

    user_manager = UserManager()
    user = User()

    while True:
        show_menu()

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
