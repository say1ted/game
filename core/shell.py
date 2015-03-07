import cmd, getpass, sys


class UserShell(cmd.Cmd):
    def set_core(self, core):
        self.core = core

    prompt = "(%s)-> " % (getpass.getuser())
    intro = "For help using '?'. " \
            "For manual to something command use 'help command'."

    # User commands

    def do_go(self, arg):
        'go 1. Using for moving to smth environment '
        selector = self.core.current_location.directions_selector
        if selector.valid(arg):
            next_location = selector.get_elem(arg)
            self.core.go(next_location)
            return

        print("# You can't go there #")

    def do_attack(self, arg):
        'attack 1. Using for attack whom'
        selector = self.core.current_location.units_selector
        if selector.valid(arg):
            unit = selector.get_elem(arg)
            self.core.attack(unit)
            return

        print("# You can't attack it. #")

    def do_info(self, arg):
        'info for current location'
        self.core.info()

    def do_inventory(self, arg):
        self.core.inventory()

    def do_drop(self, arg):
        selector = self.core.player.inventory.selector
        if selector.valid(arg):
            self.core.drop(selector.get_elem(arg))
        else:
            print("# NO. GO TO HELL. #")

    def do_take(self, arg):
        selector = self.core.current_location.items_selector
        if selector.valid(arg):
            self.core.take(selector.get_elem(arg))
        else:
            print("# NO. GO TO HELL. #")

    def do_exit(self, arg):
        'exit. Do not use this command.. please...'
        print("Goodbye!")
        sys.exit(0)