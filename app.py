from auth.login import login


class User():
    #constructor
    def __init__(self, first_name , last_name , is_admin , contact_no ,  email , username , password ):
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.contact_no = contact_no
        self.email = email
        self.username = username
        self.password = password
       

users = []
admin = User("Admin", "Admin" , True ,"0777123456" , "admin@pos.com" , "admin" , "123" )


users.append(admin)


def create_user():
    global users
    username = input("Username : ")
    password = input("Password : ")
    
    first_name = input("First Name : ")
    last_name = input("Last Name : ")
    contact_no = input("Contact No : ")
    email = input("Email : ")

    user = User(first_name, last_name , False ,contact_no , email , username , password)
    
    users.append(user)
    return user




def main():
    global users
    username = input("Username : ")
    password = input("Password : ")
    user = login(username , password , users) #false

    while not user:
        print("Login failed! please enter your login credentials")
        username = input("Username : ")
        password = input("Password : ")
        user = login(username , password , users)

     
    print("logged in!!")

    print("Choose your action!")
    if user.is_admin:
        print("1. Create User")
        choice = input("Choice : ")
        if choice == "1":
            create_user()





main()