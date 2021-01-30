import os
import json

GENERIC_DATA_FILE = {
    "last_opened": ""
}

LAST_OPENED_SAVE_PROMPT = """Last opened save found.
Loading last opened save file. (n to cancel): """

NO_SAVES_PROMPT = """No save present.
1) Create new save.
2) Exit.
Choose option(1 or 2): """

SAVES_PROMPT = """Save(s) found.
1) Load save.
2) Create new save.
3) Exit.
Choose option(1, 2 or 3): """


class Main:
    def __init__(self, main):
        self.main = main
        self.all_saves_path = os.path.join(self.main.mainpath, "saves")
        self.save_name = None
        self.data_path = os.path.join(self.all_saves_path, "data.json")
        self.data = None

    def post_init(self):
        self.load()

    def load(self):
        self.load_data_file()
        if os.path.isdir(os.path.join(self.all_saves_path, self.data["last_opened"])): 
            if prompt(LAST_OPENED_SAVE_PROMPT) == "n":
                self.prompt_load()
            else:
                self.quick_load()
        else:
            self.data["last_opened"] = ""
            self.save_data_file()
            self.prompt_load()

    def save_data_file(self):
        with open(self.data_path, "wb") as file_handle:
            json.dump(self.data, file_handle)

    def load_data_file(self):
        if "data.json" not in os.listdir(self.all_saves_path):
            self.data = GENERIC_DATA_FILE
            self.save_data_file()

        with open(self.data_path, "rb") as file_handle:
            self.data = json.load(file_handle)

    def quick_load(self, data):
        pass
    
    def prompt_load(self):
        if len(os.listdir(self.all_saves_path)) > 1:
            msg = SAVES_PROMPT
            required = ["1", "2", "3"]
        else:
            msg = NO_SAVES_PROMPT
            required = ["1", "2"]

        action = prompt(msg, required)

        if action == "1" and len(required) == 3:
            msg = ""
            required = []
            msg = "Available saves: "
            for savef in os.listdir(self.all_saves_path):
                if os.path.isdir(savef):
                    msg += f"\n{savef}"
                    required.append(savef)
            msg += "\nChoose save name: "
            save_name = prompt(msg, required)
            self.save_name = safef
            self.save_path = os.path.join(self.all_saves_path, self.save_name)
            self.load()
        
        elif action == "2" and len(required) == 3 or action == "1" and len(required) == 2:
            msg = "Enter save name: "
            save_name = prompt(msg)
            while not save_name.isalpha:
                print("Save name must only contain alphabets. Retry.")
                save_name = prompt(msg)
            self.save_name = save_name
            self.save_path = os.path.join(self.all_saves_path, self.save_name)
            os.mkdir(self.save_path)
            self.create()

        else:
            self.main.quit()
        
    def create(self):
        pass

    def load_game(self):
        self.load_data_file()

    def save(self):
        self.save_data_file()
        
    def end(self):
        self.save()

def prompt(msg, required=None):
    if required is None:
        return(input(msg))
    reply = input(msg)
    while reply not in required:
        print("Invalid choice. Retry.")
        reply = input(msg)
    return reply
