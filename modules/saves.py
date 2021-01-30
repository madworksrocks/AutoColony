import os
import json

class Main:
    save_path = None
    def __init__(self, main):
        self.main = main

    def post_init(self):
        os.chdir(os.path.join(self.main.mainpath, "saves"))
        dir = os.listdir()
        if "data.json" not in dir:
            with open("data.json", "w") as f:
                data = {
                    "last opened": ""
                }
                json.dump(data, f)

        with open("data.json") as f:
            data = json.load(f)

        if data["last opened"] == "":
            if len(dir) > 1:
                msg = """No save recently opened.
1) Load save.
2) Create new save.
3) Exit.
Choose option(1, 2 or 3): """
                required = ["1", "2", "3"]
            else:
                msg = """No saves present.
1) Create new save.
2) Exit.
Choose option(1 or 2): """
                required = ["1", "2"]
            action = prompt(msg, required)

            if action == "1" and len(required) == 3:
                msg = ""
                required = []
                msg = "Available saves: "
                for savef in dir:
                    if os.path.isdir(savef):
                        msg += f"\n{savef}"
                        required.append(savef)
                msg += "\nChoose save name: "
                savef = prompt(msg, required)
                self.savef = savef
                self.save_path = os.path.join(self.main.mainpath, "saves", self.savef)
                self.world_np_path = os.path.join(self.save_path, "world_np.npy")
                self.world_keys_path = os.path.join(self.save_path, "world_keys.json")
                self.world_data_path = os.path.join(self.save_path, "world_data.json")
                self.script_path = os.path.join(self.save_path, "script.py")
                self.load()
            
            elif action == "2" and len(required) == 3 or action == "1" and len(required) == 2:
                msg = "Enter save name: "
                savef = prompt(msg)
                while not savef.isalpha:
                    print("Save name must only contain alphabets. Retry.")
                    savef = prompt(msg)
                self.savef = savef
                self.save_path = os.path.join(self.main.mainpath, "saves", self.savef)
                os.mkdir(self.save_path)
                self.world_np_path = os.path.join(self.save_path, "world_np.npy")
                self.world_keys_path = os.path.join(self.save_path, "world_keys.json")
                self.world_data_path = os.path.join(self.save_path, "world_data.json")
                self.script_path = os.path.join(self.save_path, "script.py")
                self.create()

            else:
                quit()

    def create(self):
        self.main.data = {
            "robots": [{"Name": "Bob", "pos":self.main.MM.modules["worldgen"].world_middle_surface}]
        }

        with open(self.world_np_path, "wb") as wnf:
            with open(self.world_keys_path, "w") as wkf:
                self.main.MM.modules["worldgen"].create(wnf, wkf)

        with open(self.world_data_path, "w") as wdf:
            json.dump(self.main.data, wdf)

        with open(self.script_path, "w") as sf:
            sf.write("""

def init():
    pass

def step(robots_proxy):
    global robots
    robots = robots_proxy

""")

    def load(self):
        with open(self.world_np_path, "rb") as wnf:
            with open(self.world_keys_path, "r") as wkf:
                self.main.MM.modules["worldgen"].load(wnf, wkf)

        with open(self.world_data_path, "r") as wdf:
            self.main.data = json.load(wdf)

        self.main.MM.modules["robot"].load_script(self.save_path, self.script_path)

    def save(self):
        with open(self.world_np_path, "wb") as wnf:
            with open(self.world_keys_path, "w") as wkf:
                self.main.MM.modules["worldgen"].save(wnf, wkf)

        with open(self.world_data_path, "w") as wdf:
            json.dump(self.main.data, wdf)

def prompt(msg, required=None):
    if required is None:
        return(input(msg))
    reply = input(msg)
    while reply not in required:
        print("Invalid choice. Retry.")
        reply = input(msg)
    return reply
