from shell import UserShell


class ConsoleInterface():
    def __init__(self):
        self.__directions = {}
        self.__shell = UserShell()

        print(
        """
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @ Hello! Today you will be a hero @
        @ A hero in Middle Ages. You sho- @
        @ uld be attentive and help girls @
        @ Be lucky.                       @
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        """)

    def get_shell(self):
        self.__shell.cmdloop()

    def print_location(self, name, location):
        print(
            """
            ####################
            %s
            ####################
            %s
            """
            % (name, location['Description'])
        )
        print("You can go to(put location number):")
        number = 1

        for direction in location['Directions']:
            print("%i. %s" % (number, direction))
            self.__directions[number] = direction
            number = number + 1

    def get_direction(self):
        if path.isdigit():
            path = int(path)
            if path in self.__directions:
                return self.__directions[path]

        print("# You can't go there #")
        return self.get_direction()

