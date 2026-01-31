from person import Person

class Staff(Person):
    def __init__(self, id, name, staff_id, tax_num):
        super().__init__(id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        super().display_info()
        print(f"Staff staff_id : {self.staff_id}")