"""
Trent Varnes
sales_person.py
I certify this is my work
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def get_sales(self):
        sales = 0
        for i in self.sales:
            sales += i
        return sales

    def met_quota(self, quota):
        if self.get_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if self.sales >= other.get_sales():
            return 0
        elif self.sales <= other.get_sales():
            return 1
        else:
            return -1
