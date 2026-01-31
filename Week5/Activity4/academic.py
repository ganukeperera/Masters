from staff import Staff

class Academic(Staff):
    def __init__(self, id, name, staff_id, tax_num, publications):
        super().__init__(id, name, staff_id, tax_num)
        self.publications = publications

    def display_info(self):
        super().display_info()
        print(f"Acedemic publications: {self.publications}")