from modules.modulemanager import Main as MM
from os import getcwd

class Main:
    
    def __init__(self):
        self.mainpath = getcwd()
        self.MM = MM(self)
        
        self.MM.post_init()
        

if __name__ == "__main__":
    main = Main()

    robot = main.MM.modules["robot"]
    gui = main.MM.modules["gui"]

    while True:
        robot.step()
        gui.step()
