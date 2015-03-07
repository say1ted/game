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
        if arg.isdigit():
            arg = int(arg)
            if self.core.current_location.valid_next(arg):
                next_location = self.core.current_location.next(arg)
                self.core.go(next_location)
                return

        print("# You can't go there #")


    def do_attack(self, arg):
        'attack goblin. Using for attack whom'
        if arg.isdigit():
            arg = int(arg)
            if self.core.current_location.valid_units(arg):
                unit_name = self.core.current_location.unit_name(arg)
                self.core.attack(unit_name)
                return

        print("# You can't attack it. #")


    def do_exit(self, arg):
        'exit. Do not use this command.. please...'
        print("Goodbye!")
        sys.exit(0)