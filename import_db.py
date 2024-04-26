import db

def get_user_db():
    return db.users_db

def get_user_by_name(name, users_db):
    user = [user for user in users_db if user['name'] == name][0]
    return user


def main():
    users_db = get_user_db()
    print(users_db)

if __name__ == '__main__':
    main()

