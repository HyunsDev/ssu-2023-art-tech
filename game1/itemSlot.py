from atom import Atom


class ItemSlot(Atom):
    def __init__(self):
        self.slot = []

    def useItem(self, item):
        if item in self.slot:
            self.slot.remove(item)
            return True
        return False
