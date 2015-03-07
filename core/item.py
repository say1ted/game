class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "Name\t:\t{}\t|\tDescription\t:\t{}".format(self.name, self.description)