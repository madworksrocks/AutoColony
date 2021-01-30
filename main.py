from modules.modulemanager import Main as MM
from os import getcwd

class Main:
    
    def __init__(self):
        self.mainpath = getcwd()
        self.MM = MM(self)
        
        self.MM.post_init()

    def quit(self):
        for module in self.MM.modules.values():
            if hasattr(module, "end"):
                module.end()
        

if __name__ == "__main__":
    main = Main()
