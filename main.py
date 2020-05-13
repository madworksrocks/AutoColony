from modules.modulemanager import Main as MM
import os.getcwd

class Main:
    
    def __init__(self):
        self.mainpath = os.getcwd()
        self.MM = MM(self)

if __name__ == "__main__":
    main = Main()
