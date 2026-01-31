
class Person:
    def __init__(self, id, name):
        self.id = id
        self._name = name

    def display_info(self):
        print(f"id = {self.id}, id = {self._name}")

    def greet(self):
        print(f"Greeting and feliitation from the mastro {self._name}")
