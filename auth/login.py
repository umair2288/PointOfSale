from models.user import User


def login(username, password, users):
    for user in users:
        if user.username == username:
            if user.password == password:
                return user
            else:
                print("Incorrect username or password!")
                return False
    print("Incorrect username!")
    return False


def login_v2(username, password, file):
    for line in file:
        user_data = line.split(",")
        if user_data[5] == username:
            if user_data[6][0:-1] == password:
                user = User(
                    first_name=user_data[0],
                    last_name=user_data[1],
                    is_admin=user_data[2] == 'True',
                    contact_no=user_data[3],
                    email=user_data[4],
                    username=user_data[5],
                    password=user_data[6][0:-1]
                )
                return user
            else:
                print("Incorrect username or password!")
                return False
        else:
            print("Incorrect username!")
            return False
