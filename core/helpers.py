class SelectionHelper():
    def __init__(self, list):
        self.number_list = {}
        number = 1

        for list_item in list:
            self.number_list[str(number)] = list_item
            number = number + 1

    def print(self):
        #TODO:Иногда порядок номеров путается
       for key, list_item in self.number_list.items():
            print('{} {}'.format(key, list_item))

    def valid(self, number):
        return number in self.number_list

    def get_elem(self, number):
        return self.number_list[number]
