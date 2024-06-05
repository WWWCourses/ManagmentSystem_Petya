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
