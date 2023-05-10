from auth.login import login_v2
from models.user import User
from decimal import Decimal
from models.product import Product


def create_user():

    username = input("Username : ")
    password = input("Password : ")

    first_name = input("First Name : ")
    last_name = input("Last Name : ")
    contact_no = input("Contact No : ")
    email = input("Email : ")

    user = User(first_name, last_name, False,
                contact_no, email, username, password)

    user.save_to_file("users.txt")
    return user


def create_product():
    product_code = input("Product Code : ")
    product_name = input("Name : ")
    price = Decimal(input("Price : "))

    product = Product(product_code=product_code,
                      name=product_name, price=price)
    product.save_to_file("products.txt")


def list_products():
    print("------- LIST OF PRODUCTS -----------")
    file = open("products.txt")

    for line in file:
        data = line.split(",")
        print(f"Code: {data[0]} | Name : {data[1]} | Price : {data[2][0:-1]}")


def get_user_choices(is_admin=False):
    if is_admin:
        print("1. Create User")
        print("2. Create Product")

    print("3. List Products")
    print("0. Exit")
    print("-1. Logout")
    return input("Your Choice : ")


def main():

    print("Login!!!")
    users_file = open("users.txt")

    username = input("Username : ")
    password = input("Password : ")

    user = login_v2(username, password, users_file)  # false

    while not user:
        print("Login failed! please enter your login credentials")
        username = input("Username : ")
        password = input("Password : ")
        user = login_v2(username, password, users_file)

    print("logged in!!")

    print("Choose your action!")
    choice = get_user_choices(user.is_admin)
    if choice == "1":
        create_user()
    if choice == "2":
        create_product()
    if choice == "3":
        list_products()


main()
