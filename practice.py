from abc import ABC, abstractmethod
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Mandatory(ABC):
    @abstractmethod
    def expiry_date(self):
        pass


class Maligai(Mandatory):
    total_price = 0

    def __init__(self, p_name, p_price, p_quantity, brand, today=None):
        self.p_name = p_name
        self.p_price = p_price
        self.p_quantity = p_quantity
        Maligai.total_price += p_price
        self.brand = brand
        self.today = datetime.today()  

    def expiry_date(self):
        expiry = self.today + relativedelta(months=3)
        return f"Three months from now: {expiry.strftime('%Y-%m-%d')}"

    @staticmethod
    def legal_validation(products):
        is_illegal_product = ["gun", "firearm", "Missile"]
        if products.lower() in [item.lower() for item in is_illegal_product]:
            return "This is an illegal request"
        else:
            return "This is a legal request"

    @classmethod
    def get_total(cls):
        return f"The total value is {cls.total_price}"

    def get_details(self):
        return f"The details of product: {self.p_name}   {self.p_price}  {self.p_quantity}  {self.brand}"
    


    
product1 = Maligai("boost", 50, 54, "sehwag")
product2 = Maligai("Horlicks", 87, 85, "sachin")
product3 = Maligai("Mylo", 23, 10, "dravid")

print(Maligai.get_total())
print(product1.get_details())
print(Maligai.legal_validation("horlicks"))
print(product1.expiry_date())  # This now works correctly
