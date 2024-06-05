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

    def add_user(self):
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
