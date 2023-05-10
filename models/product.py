from .base import BaseModel


class Product(BaseModel):
    def __init__(self, product_code, name, price):
        self.product_code = product_code
        self.name = name
        self.price = price

    def format_to_save(self , sep=" "):
        return f"{self.product_code}{sep}{self.name}{sep}{self.price}\n"
