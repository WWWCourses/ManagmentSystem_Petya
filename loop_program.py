# Main program loop
while True:
    print("\nMenu:")
    print("1. Add New User")
    print("2. Delete User")
    print("3. View User Data")
    print("4. Save Records")
    print("5. Exit Program")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        delete_user()
    elif choice == '3':
        view_user_data()
    elif choice == '4':
        save_records()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


if __name__=='__main__':
    main()
