from os import system
from colorama import Fore, init

class Util:
    def __init__(self) -> None:
        init(convert=True)

    def clear(self) -> None:
        system("cls")

    def splash(self) -> None:
        print(f"""{Fore.LIGHTCYAN_EX}Registry Injector v0.1\n""")

if __name__ == "__main__":
    exit()