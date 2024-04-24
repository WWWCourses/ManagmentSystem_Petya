# Administrator Login Function

def admin_login():
    print("Administrator Login")
    name = input("Enter your name: ") 
    dob = input("Enter your date of birth: [DD/MM/YYYY] ") 
    addres = input("Enter your address: ")
    # username = input("Enter your username: ")
    # pin_code = input("Enter your pin code: ")

    if name == "admin" and dob == "20/5/1993" and addres == "Sofia":  # Example username and pin code
        print("\nHello! Welcome, to the user managment system!")
        return True
    else:
        print("Invalid login data. Please try again.")
        return False