# Administrator Login Function

class Admin:
    def __init__(self) -> None:
        self.admin_login()

    def admin_login():
        print("Administrator Login")
        self.name = input("Enter your name: ")
        self.dob = input("Enter your date of birth: [DD/MM/YYYY] ")
        self.addres = input("Enter your address: ")
        self.logged_in = False

        if self.name == "admin" and self.dob == "20/5/1993" and self.addres == "Sofia":  # Example username and pin code
            print("\nHello! Welcome, to the user managment system!")
            self.logged_in = True
        else:
            print("Invalid login data. Please try again.")
