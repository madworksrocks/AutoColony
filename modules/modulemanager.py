"""from sys import path.insert as path_insert
from os import path.join as path_join
from importlib import import_module"""

import sys, os, importlib
path_insert = sys.path.insert
path_join = os.path.join
import_module = importlib.import_module

class Main:
    
    def __init__(self, main):
        self.main = main
        modules_path = path_join(self.main.mainpath, "modules")
        path_insert(0, modules_path)  

        self.import_modules()

    def import_modules(self):
        self.modules = []        

        for fname in os.listdir("modules"):
            if fname != "modulemanager.py" and fname[-3:] == ".py":
                mod = import_module(fname[:-3], 
                    package=path_join(self.main.mainpath, "modules"))
                self.modules.append(mod.Main(self.main))

        for module in self.modules:
            if "post_init" in dir(module):
                module.post_init()
    