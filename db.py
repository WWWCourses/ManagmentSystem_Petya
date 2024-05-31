users_db = [
    {
        'name': 'Svetlin',
        'surname': 'Sofroniev',
        'date_of_birth' : '14/1/1976',
        'address_city' : 'Sofia',
        'address_street' : 'Pleven',
        'address_number' : 6,
        'pin_code' : '0001',
        'username' : 'ss'
    },
    {   
        'name': 'Mariya',
        'surname': 'Mersinkova',
        'date_of_birth' : '15/9/1970',
        'address_city' : 'Shumen',
        'address_street' : 'Nancho Popovich',
        'address_number' : 35,
        'pin_code' : '0002',
        'username' : 'mm'
    },      
    {   
        'name': 'Pavel',
        'surname': 'Zlatanov',
        'date_of_birth' : '20/5/1993',
        'address_city' : 'Sofia',
        'address_street' : 'Usmivka',
        'address_number' : 2,
        'pin_code' : '0003',
        'username' : "pz"
    }
]

def get_user_by_key(key, value):
    filtered_user = [user for user in users_db if user[key] == value]
    if filtered_user:
        return filtered_user[0]
    else:
        print(f'No user with {key}={value}')


if __name__=="__main__":
    username = input("Enter username of the user to view data: ")
    user = get_user_by_key(key='username', value=username)
    print(user)


