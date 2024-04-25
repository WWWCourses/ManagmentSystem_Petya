# Importing functions from admin_login.py and function_user_data.py

# from admin_data import register

from admin_login import admin_login
from function_users_data import see_current_users
from function_users_data import add_user
from function_users_data import delete_user
from function_users_data import show_user_data
from function_users_data import save_user_database


# Main program loop

def main():
    logged_in = False
    while not logged_in:
        logged_in = admin_login()  # Call the login function from admin_login.py
        if not logged_in:
            continue

    
    while True:
        print("\nWould you like to__")
        print("1 - See Current Users")
        print("2 - Add User")
        print("3 - Delete User")
        print("4 - Show a User")
        print("5 - Save Database")
        print("6 - More Options")  # Placeholder for additional options
        print("7 - Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            see_current_users()
        elif choice == '2':
            add_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            show_user_data()
        elif choice == '5':
            save_user_database()
        elif choice == '6':
            print("More Options")
        elif choice == '7':
            print("Quit")
        else:
            print('Invalid choise.Try agen!')
    

if __name__ == "__main__":
    main()
