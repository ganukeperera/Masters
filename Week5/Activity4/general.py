
from staff import Staff

class General(Staff):
    def __init__(self, id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_info(self):
        super().display_info()
        print(f"General tax_number: {self.rate_of_pay}")