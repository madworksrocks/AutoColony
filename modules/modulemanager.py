import os

class Main:
    
    def __init__(self, main):
        self.main = main

    def import_modules(self):
        self.modules = []

        for fname in os.listdir():
            if fname != "modulemanager.py" and fname[-3:] == ".py":
                self.modules.append(__import__(fname[:-3]).Main(self.main))
    