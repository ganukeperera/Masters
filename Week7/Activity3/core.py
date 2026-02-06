class KeeperMeta(type):
    _holders = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._holders:
            instance = super().__call__(*args, **kwargs)
            cls._holders[cls] = instance
        return cls._holders[cls]

class Keeper(metaclass=KeeperMeta):
    def __init__(self):
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)
