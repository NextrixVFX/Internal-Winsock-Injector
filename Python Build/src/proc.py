from psutil import Process, process_iter
from threading import Thread
from time import sleep
from colorama import Fore, init
from json import loads

class ProceessManager:
    def __init__(self, proc: str) -> None:
        init(convert=True)
        self.proc: str = proc
        try:
            self.__config__ = loads(open("config\\config.json", "r+").read())
            self.delay: float = float(self.__config__["find-delay"])
        except Exception as e:
            print(f"{Fore.RED}Error reading config: {e}")
            input("Press any key to continue")
            exit()
    
    def waitForProcess(self, function: Thread):
        procFound: bool = False
        while procFound == False:
            process: str = self.getProcess(self.proc)
            if process != "":
                print(f"{Fore.LIGHTCYAN_EX}Found: {Fore.LIGHTBLUE_EX}{process}")
                procFound: bool = True
                function.start()
                function.join()
            else:
                print(f"{Fore.LIGHTYELLOW_EX}Not found")
                sleep(self.delay)

    def getProcess(self, proc: str) -> str:
        processes = process_iter()
        for process in processes:
            if process.name() == proc:
                return process.name()
        return ""
    
if __name__ == "__main__":
    exit()