from dataclasses import dataclass
from datetime import datetime


@dataclass
class Daily_sales:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime
    quantity: int
    unit_price: float
    unit_sale_price: float

def __eq__(self, other):
    return self.Retailer_code == other.Retailer_code and self.Product_number == other.Product_number and self.Order_method_code == other.Order_method_code and self.Date == other.Date
def __hash__(self):
    return hash((self.Retailer_code, self.Product_number, self.Order_method_code, self.Date))
def __str__(self):
    return f""
