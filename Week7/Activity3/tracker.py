class Watcher:
    def notice(self, msg):
        pass

class Screen(Watcher):
    def notice(self, msg):
        print(f"[Screen] {msg}")

class Record(Watcher):
    def notice(self, msg):
        print(f"[Record] {msg}")
