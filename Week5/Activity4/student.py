from person import Person

class Student(Person):
    def __init__(self, id, name, student_id):
        super().__init__(id, name)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student student_id: {self.student_id}")

    def greet(self):
        print(f"Hi {self._name}")

