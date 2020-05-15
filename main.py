from modules.modulemanager import Main as MM
from os import getcwd

class Main:
    
    def __init__(self):
        self.mainpath = getcwd()
        self.MM = MM(self)

if __name__ == "__main__":
    main = Main()
    main = Main()
