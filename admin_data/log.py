# Start main program
def main():
    if admin_login():
        print("\nHello! Welcome, to the user managment system!")
    else:
        print("\nLogin failed. Please check the entered data.")
    

# Function to authenticate the administrator

def admin_login():
    print("Administrator Login")
    name = input("Enter your name: ") ### adding a dictionary with keys for first name, last name, last name
    dob = input("Enter your date of birth (YYYY-MM-DD): ") 
    address = input("Enter your address: ") ### add dict for city, str., nomber, ZIP code

    # return True ### Only valid for demonstration proposes

if __name__ == "__main__":
    main()



# I can customize the admin login to the system, add job title for example 
# for date of birth I can adding a button with a drop-down menu to select date, month, year
# and does the user have the necessary credentials to log in as adminstrator
   
    
    

 