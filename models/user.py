from .base import BaseModel


def validate_contact_no(contact_no):
    if len(contact_no) != 10:
        raise Exception("Invalid Contact No")
    else:
        return True


def validate_email(email):
    pass


class User(BaseModel):
    # constructor
    def __init__(self, first_name, last_name, is_admin, contact_no,  email, username, password):
        validate_contact_no(contact_no)
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.contact_no = contact_no
        self.email = email
        self.username = username
        self.password = password

    def format_to_save(self, sep=" "):
        return f"{self.first_name}{sep}{self.last_name}{sep}{self.is_admin}{sep}{self.contact_no}{sep}{self.email}{sep}{self.username}{sep}{self.password}\n"
