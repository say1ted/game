from core.helpers import SelectionHelper


class Inventory():
    def __init__(self):
        self.items = []
        self.selector = SelectionHelper(self.items)

    def drop(self, item):
        self.items.remove(item)
        self.selector = SelectionHelper(self.items)


    #TODO: Если обновили items надо обновлять селектор
    def take(self, item):
        self.items.append(item)
        self.selector = SelectionHelper(self.items)

    def print(self):
        self.selector.print()
