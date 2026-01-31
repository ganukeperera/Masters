from animal import Animal

class Bird(Animal):
    def __init__(self, name, feature: str):
        super().__init__(name, feature)