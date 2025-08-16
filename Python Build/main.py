from colorama import Fore, init
from pyuac import isUserAdmin, runAsAdmin
from src.inject import InjectDLL
from src.util import Util

class Main:
    def __init__(self) -> None:
        init(convert=True)
        util: Util = Util()
        util.splash()
        self.proc: str = input(f"{Fore.GREEN}Enter Process Name:{Fore.WHITE}\t")
        assert self.proc != '', f"{Fore.RED}Invalid Process Name!"

        if ".exe" not in self.proc:
            self.proc += ".exe"

        self.InjectDLL: InjectDLL = InjectDLL(self.proc)

    def start(self):
        self.InjectDLL.inject()
        input("Press any key to continue...")

if __name__ != "__main__":
    exit()

if not isUserAdmin():
    print(f"{Fore.RED}Admin Required!\n{Fore.YELLOW}Relaunching as Admin.{Fore.WHITE}")
    try:
        runAsAdmin()
    except Exception as e:
        print(f"Cannot Elevate Permissions: {e}")
else:
    main: Main = Main()
    main.start()
