from easygui import fileopenbox
from time import sleep
from threading import Thread
from src.reg import AutodialDLL
from src.proc import ProceessManager
from colorama import Fore, init
from json import loads, dumps

class InjectDLL:
    def __init__(self, proc: str) -> None:
        init(convert=True)
        self.proc: str = proc
        self.AutodialDLL: AutodialDLL = AutodialDLL()
        self.ProcessManager: ProceessManager = ProceessManager(self.proc)
        try:
            self.__config__ = loads(open("config\\config.json", "r+").read())
            self.delay: float = float(self.__config__["delete-delay"])
        except Exception as e:
            print(f"{Fore.RED}Error reading config: {e}")
            input("Press any key to continue")
            exit()
    
    def loadDLL(self) -> str:
        dllFile: list[str] = fileopenbox("", "Select DLL", "*", "*.dll", False)
        assert dllFile != None, f"{Fore.RED}No DLL Selected!"
        assert dllFile.__contains__(".dll") != False, f"{Fore.RED}Invalid DLL Selected!"
        return str(dllFile)
    
    def inject(self) -> None:
        dllPath: str = self.loadDLL()
        preloadThread: Thread = Thread(target=self.preload, args=(dllPath,))
        self.ProcessManager.waitForProcess(preloadThread)

    def preload(self, dllPath: str) -> None:
        addDLL: Thread = Thread(target=self.addDLL, args=(dllPath,))
        removeDLL: Thread = Thread(target=self.removeDLL)

        addDLL.start()
        addDLL.join()

        removeDLL.start()
        removeDLL.join()

    def addDLL(self, dll: str) -> None:
        print(f"{Fore.LIGHTBLUE_EX}Preloading DLL:{Fore.WHITE} {dll}")
        self.AutodialDLL.AddDLL(dll)
        print(f"{Fore.LIGHTGREEN_EX}DLL Injected!")
    
    def removeDLL(self) -> None:
        print(f"{Fore.LIGHTMAGENTA_EX}Waiting {self.delay}s to delete DLL{Fore.WHITE}")
        sleep(self.delay)
        self.AutodialDLL.RemoveDLL()

if __name__ == "__main__":
    exit()
