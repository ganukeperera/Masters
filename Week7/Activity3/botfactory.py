from abc import ABC, abstractmethod

class Unit(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def action(self):
        pass

class Helper(Unit):
    def action(self):
        print(f"{self.id} is assisting humans")

class Friend(Unit):
    def action(self):
        print(f"{self.id} is keeping company")

class Maker:
    @staticmethod
    def produce(unit_type, id):
        if unit_type == "helper":
            return Helper(id)
        elif unit_type == "friend":
            return Friend(id)
        else:
            raise ValueError("Unknown type")
