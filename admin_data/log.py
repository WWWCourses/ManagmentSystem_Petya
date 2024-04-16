# Function to authenticate the administrator
def main():
    if admin_login():
        print("\nHello! Welcome, to the user managment system!")
    else:
        print("\nLogin failed. Please check the entered data.")
    

def admin_login():
    print("Administrator Login")
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    address = input("Enter your address: ")

    # return True ### Only valid for demonstration proposes

if __name__ == "__main__":
    main()



# I can customize the admin login to the system, add job title for example 
# and does the user have the necessary credentials to log in as adminstrator
   
    
    

 