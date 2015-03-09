from core.core import Core
from data.builder import Builder
from core.shell import UserShell

if __name__ == '__main__':
    core = Core(Builder())
    shell = UserShell()
    shell.set_core(core)
    shell.cmdloop()
